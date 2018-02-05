from flask_classy import FlaskView, route
from flask import request, json, jsonify
from mono.model.user import User
from mono.model.movie import Movie
from mono.api import ApiView


class MovieView(ApiView):

    def all(self):
        return Movie.query.all()

















