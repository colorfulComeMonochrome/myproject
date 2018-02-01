from flask_classy import FlaskView

class Index(FlaskView):
    route_base = '/'

    def index(self):
        return "that's cool"





















