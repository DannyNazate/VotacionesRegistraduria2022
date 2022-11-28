from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa

from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa



class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato=RepositorioCandidato()
        self.repositorioMesa=RepositorioMesa()
    def index(self):
        return self.repositorioResultado.findAll()
### ASIGNACION DE CANDIDATO A MESA
    def create(self, infoResultado, id_candidato, id_mesa):
        nuevoResultado = Resultado(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)
    #######
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    ## ACTUALIZAR CANDIDATO A MESA

    def update(self, id, infoResultado, id_candidato, id_mesa):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        elResultado.reporte = infoResultado["reporte"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa= Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)
    def delete(self,id):
        return self.repositorioResultado.delete(id)


## Listado general de votos por cada candidato
    def listarResultadosDeCandidatos(self,id_resultado):
        return self.repositorioResultado.getListadoDeVotos(id_resultado)

    def totalVotos(self):
        return self.repositorioResultado.getListadoDeVotos()
    def sumaVotosPorMesa(self, id_mesa):
        return self.repositorioResultado.sumavotosPorMesa(id_mesa)

    def VotosPorCandidato(self):
        return self.repositorioResultado.getListadoDeVotosPorCandidato()


