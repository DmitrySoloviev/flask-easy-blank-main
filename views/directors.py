# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace
from models import Director, DirectorSchema


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        directors_schema = DirectorSchema()
        if directors:
            return directors_schema.dump(directors), 200
        else:
            return "Список режиссеров - пуст"


@director_ns.route('/<int:gid>')
class DirectorView(Resource):
    def get(self, gid):
        director = Director.query.get(gid)
        director_schema = DirectorSchema(many=True)
        if director:
            return director_schema.dump(director), 200
        else:
            return f"Режиссера с id - {gid} нет."



