from persona import Persona
from cita import Cita
class Paciente(Persona): 
    def __init__(self):

        self.prevision=""
        self.ultima_prestacion=""
        self.requerimientos=[]
        self.diagnosticos=[]
        self.forma_pago=""
        #billetera
        self.cartera=0
        self.citas= []
        #self.recetas=[]

    def setPrevision(self,prevision):
        self.prevision=prevision

    def setUltimaPrestacion(self,ultima_prestacion):
        self.ultima_prestacion=ultima_prestacion

    def setRequerimientos(self,requerimientos):
        self.requerimientos=requerimientos

    def setDiagnosticos(self,diagnosticos):
        self.diagnosticos=diagnosticos

    def setFormapago(self,forma_pago):
        self.forma_pago=forma_pago
    
    def setCitas(self,citas):
        self.citas=citas

    def getPrevision(self):
        return self.prevision

    def getUltimaPrestacion(self):
        return self.ultima_prestacion

    def getRequerimientos(self):
        return self.requerimientos

    def getDiagnosticos(self):
        return self.diagnosticos

    def getFormapago(self):
        return self.forma_pago
    
    def getCitas(self):
        return self.citas

    def agendarCita(self,_cita):
        return "not implemented yet"
        
    def cancelarCita(self, _codigo_cita):

        for i in range (len(self.citas)):

            if _codigo_cita==self.citas[i].codigo:
                self.citas.pop(i)
                return True

        return False

    def reagendarCita(self, _fecha):
        return "not implemented yet"
    
    def pagarCita(self,_cita,_monto_a_pagar):
        if _monto_a_pagar>self.cartera:
            return False
        else:
            _cita.setPagado(True)
            return True

    def confirmarCita(self,_cita):
        _cita.setConfirmada(True)

    def __str__(self):
        return self.prevision+" "+self.ultima_prestacion+" "+self.requerimientos+" "+self.diagnosticos+" "+self.forma_pago
    
