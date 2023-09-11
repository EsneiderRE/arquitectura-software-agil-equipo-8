from sqlalchemy import func
from flask import request
from flask_restful import Resource
from ..modelos import CandidatoSchema, Candidato


candidato_schema = CandidatoSchema()


class VistaGrupos(Resource):
    def get(self):
        candidatos = Candidato.query.order_by(func.random()).limit(3).all()
        return [candidato_schema.dump(candidato) for candidato in candidatos]

    def get(self, candidato_id):
        candidato = Candidato.query.get(candidato_id)
        if candidato:
            return candidato_schema.dump(candidato)
        else:
            return "Candidato no encontrado", 404
        