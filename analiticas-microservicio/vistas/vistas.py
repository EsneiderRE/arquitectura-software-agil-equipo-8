from flask_restful import Resource
from ..modelos import db, Candidato
from collections import Counter


class VistaAnaliticas(Resource):
    def get(self):
        candidatos = Candidato.query.all()
        cantidad_candidatos = len(candidatos)
        print(cantidad_candidatos)
        profesiones = dict(Counter([x.profesion for x in candidatos]))
        min_edad = min([x.edad for x in candidatos])
        max_edad = max([x.edad for x in candidatos])
        return f"""Total candidatos: {cantidad_candidatos}. Profesiones: {profesiones}. Rango de dad candidatos: {min_edad} - {max_edad}"""

