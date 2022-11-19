from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoDeVotos(self, id_resultado):
        theQuery = {"candidato.$id": ObjectId(id_resultado)}
        return self.query(theQuery)


    def sumavotosPorMesa(self,id_mesa):
        query1={
            "$match": {"mesa.$id":ObjectId(id_mesa)}
        }
        query2 = {
            "$group":{
            "_id":"$mesa",
            "Numero de Votos:":{
                "$sum": 1,
                },
            }
        }
        pipeLine=[query1,query2]
        return self.queryAggregation(pipeLine)

