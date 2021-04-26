from paciente import Paciente
from medico import Medico

class Receta():

    def __init__(self):
        self.paciente= Paciente()
        self.medico= Medico()
        self.medicamentos=""
        self.fecha=""
        self.duracion=""
        self.observaciones=[]
        self.dosis=""
    
    def setPaciente(self,paciente):
        self.paciente=paciente
    
    def setMedico(self,medico):
        self.medico=medico

    def setMedicamentos(self,medicamentos):
        self.medicamentos=medicamentos

    def setFecha(self,fecha):
        self.fecha=fecha

    def setDuracion(self,duracion):
        self.duracion=duracion

    def setObservaciones(self,observaciones):
        self.observaciones=observaciones

    def setDosis(self,dosis):
        self.dosis=dosis
    
    def getPaciente(self):
        return self.paciente

    def getMedico(self):
        return self.medico

    def getMedicamentos(self):
        return self.medicamentos
    
    def getFecha(self):
        return self.fecha

    def getDuracion(self):
        return self.duracion

    def getObservaciones(self):
        return self.observaciones

    def getDosis(self):
        return self.dosis

    
    
    
