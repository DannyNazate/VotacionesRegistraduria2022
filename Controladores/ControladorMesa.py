from Repositorios.RepositorioMesa import RepositorioMesa
#from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Mesa import Mesa
#from Modelos.Partido import Partido

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        #self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevaMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    def show(self,id):
        laMesa=Mesa(self.repositorioEstudiante.findById(id))
        return laMesa.__dict__