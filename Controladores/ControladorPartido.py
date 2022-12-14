from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioCandidato import RepositorioCandidato

from Modelos.Partido import Partido
from Modelos.Candidato import Candidato


class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioPartido.findAll()
    def create(self,infoPartido):
        nuevoPartido=Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    def show(self,id):
        elPartido=Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    def update(self,id,infoPartido):
        partidoActual=Partido(self.repositorioPartido.findById(id))
        partidoActual.lema=infoPartido["lema"]
        partidoActual.nombre_partido = infoPartido["nombre_partido"]
        return self.repositorioPartido.save(partidoActual)
    def delete(self,id):
        return self.repositorioPartido.delete(id)

