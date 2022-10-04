# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)
from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    """
    Модель Director с таблицей director (SQLAlchemy - db)
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    """
    Модель Genre с таблицей genre (SQLAlchemy - db)
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
    Модель GenreSchema для перевода данных в JSON
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()


class DirectorSchema(Schema):
    """
    Модель DirectorSchema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()


class MovieSchema(Schema):
    """
    Модель MovieSchema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)

