from math import floor

class Persona():
    def __init__(self):
        self.nombre=""
        self.edad=0
        self.rut=""
        self.contacto=""
      
    def setNombre(self,nombre):
        self.nombre=nombre
        
    def setEdad(self,edad):
        self.edad=edad

    def setRut(self,rut):
        self.rut=rut

    def setContacto(self,contacto):
        self.contacto=contacto

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getRut(self):
        return self.rut

    def getContacto(self):
        return self.contacto
   
    def isRut(self,rut):
        self.rut=rut
        serie="234567"
        recorre_serie=0
        verificador=rut[-1]
        verificando=rut[:-2]
        verificando=verificando[::-1]
        verificar=0
        
        if verificador == "k":
            verificador == 10

        for i in verificando:
        
            if recorre_serie > len(serie)-1:
                recorre_serie=0 

            verificar+=(int(i)*int(serie[recorre_serie]))
            recorre_serie+=1

        verificaraux=floor(verificar/11)
        verificar=verificar-(verificaraux*11)
        verificar=11-verificar

        if verificar==int(verificador):
            return True
        else:
            return False

    def __str__(self) :
        return self.nombre+" "+self.rut+" "+str(self.edad)+" "+self.contacto
