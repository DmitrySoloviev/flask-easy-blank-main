# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201

    def put(self):
        return "", 201

    def delete(self):
        return "", 201


@movie_ns.route('/<int:gid>')
class MoviesView(Resource):
    def get(self, gid):
        return gid, 200



