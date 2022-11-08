from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevaMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    def show(self,id):
        laMesa=Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__