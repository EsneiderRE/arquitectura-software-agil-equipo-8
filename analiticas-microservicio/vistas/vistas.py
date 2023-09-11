from flask_restful import Resource
from ..modelos import db, Candidato
from collections import Counter
import statistics as stats


class VistaAnaliticas(Resource):
    def get(self):
        candidatos = Candidato.query.all()
        cantidad_candidatos = len(candidatos)
        print(cantidad_candidatos)
        profesiones = dict(Counter([x.profesion for x in candidatos]))
        min_edad = min([x.edad for x in candidatos])
        max_edad = max([x.edad for x in candidatos])
        suma_edades = sum([x.edad for x in candidatos])
        promedio_edades = suma_edades/cantidad_candidatos
        edades = [x.edad for x in candidatos]
        desviacion_estandar = stats.stdev(edades)
        return f"""Total candidatos: {cantidad_candidatos}. Profesiones: {profesiones}. Rango de dad candidatos: {min_edad} - {max_edad}. Promedio edad: {promedio_edades}. Desviacion estandar edades: {desviacion_estandar}"""
