from medico import Medico
from paciente import Paciente
import datetime as dt
class Cita ():
    def __inti__(self):
        self.fecha=dt.datetime(1,1,1)
        self.medico= Medico()
        self.paciente=Paciente()
        self.direccion=""
        self.codigo=""
        self.prestacion=""
        self.estado=""
        self.pagado=False
        self.modalidad=""
        self.prioridad=""
        self.estadoTemporal=""
        self.confirmada=False

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

    def setConfirmada(self,confirmada):
        self.confirmada=confirmada

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
    
    def getConfirmada(self):
        return self.confirmada

    def actualizarEstado(self):
        fecha_actual=dt.datetime.now()
        dias_restantes=(self.fecha-fecha_actual).days

        if dias_restantes==0:
            self.setEstadoTemporal("Cita en curso...")

        elif dias_restantes>0:
            self.setEstadoTemporal("Quedan "+str(dias_restantes)+" dias para su cita...")

        elif dias_restantes<0:
            self.setEstadoTemporal("su cita fue hace "+str(-1*dias_restantes)+" días")
        
        else:
            return False
        
        return True

    



    
    
