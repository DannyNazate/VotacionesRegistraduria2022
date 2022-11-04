from Repositorios.RepositorioPartido import RepositorioPartido

#from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
#from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        #self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioPartido.findAll()
    def create(self,infoPartido):
        nuevaPartido=Partido(infoPartido)
        return self.repositorioPartido.save(nuevaPartido)
    def show(self,id):
        elPartido=Partido(self.repositorioEstudiante.findById(id))
        return elPartido.__dict__