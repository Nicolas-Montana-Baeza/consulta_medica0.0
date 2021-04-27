from medico import Medico
from paciente import Paciente

class Cita ():
    def __inti__(self):
        self.fecha=""
        self.medico= Medico()
        self.paciente=Paciente()
        self.direccion=""
        self.codigo=""
        self.prestacion=""
        self.estado=""
        self.pagado=0
        self.modalidad=""
        self.prioridad=""
        self.estadoTemporal=""

    def setFecha(self,fecha):
        self.fecha=fecha

    def setMedico(self,medico):
        self.medico=medico

    def setPaciente(self,paciente):
        self.paciente=paciente

    def setDireccion(self,direccion):
        self.direccion=direccion

    def setCodigo(self,codigo):
        self.codigo=codigo

    def setPrestacion(self,prestacion):
        self.prestacion=prestacion

    def setEstado(self,estado):
        self.estado=estado

    def setPagado(self,pagado):
        self.pagado=pagado

    def setModalidad(self,modalidad):
        self.modalidad=modalidad
    
    def setEstadoTemporal(self,estadoTemporal):
        self.estadoTemporal=estadoTemporal

    def getFecha(self):
        return self.fecha

    def getMedico(self):
        return self.medico

    def getPaciente(self):
        return self.paciente

    def getDireccion(self):
        return self.direccion

    def getCodigo(self):
        return self.codigo

    def getPrestacion(self):
        return self.prestacion

    def getEstado(self):
        return self.estado

    def getPagado(self):
        return self.pagado

    def getModalidad(self):
        return self.modalidad
    
    def getEstadoTemporal(self):
        return self.estadoTemporal

        



    
    
