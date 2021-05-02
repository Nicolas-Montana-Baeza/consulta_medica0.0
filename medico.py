from persona import Persona
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

    def recetarPaciente(self, _receta,_paciente):
        _receta=_paciente.getRecetas.append(_receta)
        _paciente.set(_receta)

    def requerirExamen(self, _examen, _paciente):
        _examen=_paciente.getRequerimientos().append(_examen)
        _paciente.setRequerimientos(_examen)
        return _paciente


    def isDisponible(self, _fecha):
        for disponible in self.disponibilidad:
            if _fecha==disponible: 
                return True
        return False

    def diagnosticarPaciente(self, _diagnostico, _paciente):
        _diagnostico=_paciente.getDiagnosticos().append(_diagnostico)
        _paciente.setDiagnosticos(_diagnostico)
        return _paciente

    def __str__(self) :
        return str(self.disponibilidad)+" "+self.especialidad

