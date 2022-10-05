# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace
from models import Movie, MovieSchema
from flask import request
from setup_db import db


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        movies_schema = MovieSchema(many=True)
        if director_id:
            movie = Movie.query.filter(Movie.director_id == director_id).all()
            if movie:
                return movies_schema.dump(movie), 200
            else:
                return "", 404
        if genre_id:
            movie = Movie.query.filter(Movie.genre_id == genre_id).all()
            if movie:
                return movies_schema.dump(movie), 200
            else:
                return "", 404
        movie = Movie.query.all()
        if movie:
            return movies_schema.dump(movie), 200
        else:
            return "", 404

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        try:
            db.session.add(new_movie)
            db.session.commit()
            return "", 201
        except Exception as e:
            print(e)
            db.session.rollback()
            return "", 500


@movie_ns.route('/<int:gid>')
class MovieView(Resource):
    def get(self, gid):
        movie = Movie.query.get(gid)
        movie_schema = MovieSchema()
        return movie_schema.dump(movie), 200


    def put(self, gid):
        movie = Movie.query.get(gid)
        req_json = request.json
        try:
            movie.title = req_json.get("title")
            movie.description = req_json.get("description")
            movie.trailer = req_json.get("trailer")
            movie.year = req_json.get("year")
            movie.rating = req_json.get("rating")
            movie.genre_id = req_json.get("genre_id")
            movie.genre = req_json.get("genre")
            movie.director_id = req_json.get("director_id")
            movie.director = req_json.get("director")
            db.session.add(movie)
            db.session.commit()
            return "", 204
        except Exception as e:
            print(e)
            db.session.rollback()
            return "", 500

    def delete(self, gid):
        movie = Movie.query.get(gid)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return "", 204
        else:
            return "", 404




