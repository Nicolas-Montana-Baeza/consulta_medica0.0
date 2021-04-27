from persona import Persona
from receta import Receta
from paciente import Paciente
class Medico(Persona):

    def __init__(self):
        self.pacientes=[]
        self.disponibilidad=[]
        self.especialidad=""

    def setDisponibilidad(self,disponibilidad):
        self.disponibilidad=disponibilidad

    def setEspecialidad(self,especialidad):
        self.especialidad=especialidad
    
    def setPaciente(self,paciente):
        self.paciente=paciente

    def getDisponibilidad(self):
        return self.disponibilidad

    def getEspecialidad(self):
        return self.especialidad

    def getPacientes(self):
        return self.pacientes
    
    def getPacientes(self):
        return self.pacientes

    def recetarPaciente(self, _paciente, _medicamentos, _fecha, _duracion, _observaciones, _dosis):
        receta= Receta()
        receta.setPaciente(_paciente)
        receta.setMedicamentos(_medicamentos)
        receta.setFecha(_fecha)
        receta.setDuracion(_duracion)
        receta.setObservaciones(_observaciones)
        receta.setDosis(_dosis)
        receta.setMedico(self)
    
    def despacharPaciente(self, _cita, _paciente):

        return "not implemented yet"
    
   

    def __str__(self) :
        return str(self.disponibilidad)+" "+self.especialidad

