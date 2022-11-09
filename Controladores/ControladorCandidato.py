from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self, id, infoCandidato):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual = infoCandidato["mesa"]
        candidatoActual.cantidad_inscritos = infoCandidato["cantidad_inscritos"]
        return self.repositorioCandidato.save(candidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)