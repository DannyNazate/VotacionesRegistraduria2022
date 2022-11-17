from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoDeVotos(self, id_candidato,id_partido):
        theQuery = {"candidato.$id": ObjectId(id_candidato),"partido.$id": ObjectId(id_partido)}
        return self.query(theQuery)
    def getMayorNotaPorCurso(self):
        query1={
                "$group": {
                    "_id": "$materia",
                    "max": {
                        "$max": "$nota_final"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)

    def sumavotosPorMesa(self,id_mesa):
        query1={
            "$match":{"mesa.$id":ObjectId(id_mesa)}
        }
        query2 = {
            "$group":{
            "_id":"$mesa",
            "Numero de Votos:":{
                "$sum": 1
            },
                "Numero de Votos:": {
                    "_id":"$mesa"
                }
            }
        }
        pipeLine=[query1,query2]
        return self.queryAggregation(pipeLine)
