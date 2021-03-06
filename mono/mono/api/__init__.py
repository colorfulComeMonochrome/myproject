import functools

from flask import json, request, Response, make_response, jsonify
from flask_classy import FlaskView
from mono.tools.code import Code

class ApiView(FlaskView):

    """
        继承自FlaskView的apiview 实现：
        在API中直接返回对象，或直接返回数据，
        由自定义的jsonify方法来将response加工成标准格式

    """
    @classmethod
    def make_proxy_method(cls, name):
        """Creates a proxy function that can be used by Flasks routing. The
        proxy instantiates the FlaskView subclass and calls the appropriate
        method.

        :param name: the name of the method to create a proxy for
        """

        i = cls()
        view = getattr(i, name)

        if cls.decorators:
            for decorator in cls.decorators:
                view = decorator(view)

        @functools.wraps(view)
        def proxy(**forgettable_view_args):
            # Always use the global request object's view_args, because they
            # can be modified by intervening function before an endpoint or
            # wrapper gets called. This matches Flask's behavior.
            del forgettable_view_args

            if hasattr(i, "before_request"):
                response = i.before_request(name, **request.view_args)
                if response is not None:
                    return response

            before_view_name = "before_" + name
            if hasattr(i, before_view_name):
                before_view = getattr(i, before_view_name)
                response = before_view(**request.view_args)
                if response is not None:
                    return response

            response = view(**request.view_args)
            ##################################################################
            if not isinstance(response, Response):
                if isinstance(response, tuple) and len(response) > 1:
                    info, from_data = response
                    response = jsonify(info_msg=info.name, info_code=info.value, data=from_data)
                else:
                    response = jsonify(info_msg=Code.success.name,
                                       info_code=Code.success.value,
                                        data=response)
                # response = make_response(response)
            ##################################################################
            after_view_name = "after_" + name
            if hasattr(i, after_view_name):
                after_view = getattr(i, after_view_name)
                response = after_view(response)

            if hasattr(i, "after_request"):
                response = i.after_request(name, response)

            return response

        return proxy



















