from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
import pymongo

from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoDeVotos(self):
        query0 = {
            "$match": {"resultado.$id":1}
        }
        query1 = {
            "$group": {
                "_id": "$Datoscandidato",
                "Numero de Votos:": {
                    "$sum": 1,
                }
            }
        }

        consultapartido = {
            '$lookup': {
                'from': 'candidato',
                'localField': '$id',
                'foreignField': 'candidato',
                'as': 'Datoscandidato',
            },
            '$lookup': {
                'from': 'partido',
                'localField': '$id',
                'foreignField': 'partido',
                'as': 'Datospartido'
            },

        }
        query3 = {
            '$unwind': {
                'path': '$Datospartido'
            }
        }
        consultacandidato = {
            '$lookup': {
                'from': 'candidato',
                'localField': '$id',
                'foreignField': 'candidato',
                'as': 'Datoscandidato'
            }
        }

        query5 = {
            '$unwind': {
                'path': '$Datoscandidato'
            }
        }
        query8 = {
            "$group": {
                "_id": "$partido",
                "Numero de partido:": {
                    "$sum": 1,
                }
            }
        }
        query6 = {
            '$project': {
                'candidato.$id': 0,
                '$id':0,
                'Datoscandidato.cedula':0,
                'Datoscandidato.numero_resolucion': 0,
                'Datospartido._id': 0,
                'Datospartido.partido': 0,
                'Datospartido.lema':0,
                'Datospartido._id':0,
                'Datoscandidato._id': 0,
                'Datoscandidato.partido':0
            }
        }


        pipeline = [query1,consultapartido,query3,consultacandidato,query5,query6]
        return self.queryAggregation(pipeline)

    def sumavotosPorMesa(self,id_mesa):
        query1={
            "$match": {"mesa.$id":ObjectId(id_mesa)}
        }
        query2 = {
            "$group":{
            "_id": "$mesa",
            "Numero de Votos:":{
                "$sum": 1,
                },
            }
        }
        consultamesa = {
            '$lookup': {
                'from': 'mesa',
                'localField': '$id',
                'foreignField': 'mesa',
                'as': 'numero_mesa'
            }
        }

        query5 = {
            '$unwind': {
                'path': '$numero_mesa'
            }
        }
        query6 = {
            '$project': {
                'numero_mesa.cantidad_inscritos': 0,
                'numero_mesa._id': 0,

            }
        }

        pipeLine=[query1,query2,consultamesa,query5,query6]
        return self.queryAggregation(pipeLine)

    def getListadoDeVotosPorCandidato(self):
        query1 = {
           "$lookup":{
               "from":"candidato",
               "localField":"$id",
               "foreignField":"candidato",
               "as":"candidatos",
           },


        }

        query3={
            "$unwind": "$candidatos"
        }

        query2 = {
            "$group": {
                "_id": "$candidato",
                "Numero :": {
                    "$sum": 1,
                },
            }
        }

        pipeLine = [query1, query3]
        return self.queryAggregation(pipeLine)

