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
        self.codigo_cita=""

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

    def getPrevision(self):
        return self.prevision

    def getUltimaPrestacion(self):
        return self.ultima_prestacion

    def getRequerimientos(self):
        return self.requerimientos

    def getDiagnosticos(self):
        return self.diagnosticos

    def getFormapago(self,forma_pago):
        return self.forma_pago
    
   # def pagar(self, dinero):


    def __str__(self):
        return self.prevision+" "+self.ultima_prestacion+" "+self.requerimientos+" "+self.diagnosticos+" "+self.forma_pago
    
