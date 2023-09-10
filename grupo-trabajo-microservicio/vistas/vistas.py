from flask import request
from sqlalchemy import func
from flask_restful import Resource
from ..modelos import CandidatoSchema, Candidato

candidato_schema = CandidatoSchema()


class VistaGrupos(Resource):
    def get(self):
        candidatos = Candidato.query.order_by(func.random()).limit(3).all()
        return [candidato_schema.dump(candidato) for candidato in candidatos]
