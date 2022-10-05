# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace
from models import Genre, GenreSchema
from flask import jsonify
import json


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        genres_schema = GenreSchema(many=True)
        if genres:
            return genres_schema.dump(genres), 200
        else:
            return "Список жанров - пуст", 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        genre_schema = GenreSchema()
        if genre:
            return genre_schema.dump(genre), 200
        else:
            return f"Жанра с id - {gid} нет.", 404


