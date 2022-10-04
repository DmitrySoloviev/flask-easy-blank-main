# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200


@genre_ns.route('/<int:gid>')
class BooksView(Resource):
    def get(self, gid):
        return gid, 200


