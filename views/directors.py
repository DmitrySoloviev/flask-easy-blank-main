# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return "", 200


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        return gid, 200



