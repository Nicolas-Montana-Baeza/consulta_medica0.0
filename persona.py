from math import floor

class Persona():
    def __init__(self):
        self.primer_nombre=""
        self.segundo_nonmbre=""
        self.apellido_paterno=""
        self.Apellido_materno=""
        self.edad=0
        self.rut=""
        self.email=""
        self.numero_telefonico=[]
      
    def setPrimerNombre(self,primer_nombre):
        self.primer_nombre=primer_nombre
        
    def setSegundoNombre(self,segundo_nombre):
        self.segundo_nombre=segundo_nombre
        
    def setApellidoPaterno(self,apellido_paterno):
        self.apellido_paterno=apellido_paterno

    def setApellidoMaterno(self,apellido_materno):
        self.apellido_materno=apellido_materno
        
    def setNumero_Telefonico(self,numero_telefonico):
        self.numero_telefonico=numero_telefonico
        
    def setEdad(self,edad):
        self.edad=edad

    def setRut(self,rut):
        self.rut=rut

    def setEmail(self,email):
        self.email=email

    def getPrimerNombre(self):
        return self.primer_nombre

    def getSegundoNombre(self):
        return self.segundo_nombre

    def getApellidoMaterno(self):
        return self.apellido_materno

    def getApellidoPaterno(self):
        return self.apellido_paterno

    def getNumeroTelefonico(self):
        return self.numero_telefonico

    def getEmail(self):
        return self.email

    def getEdad(self):
        return self.edad

    def getRut(self):
        return self.rut
   
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
        return self.apellido_paterno+" "+self.apellido_materno+" "+self.primer_nombre+" "+self.segundo_nombre+" "+self.rut+" "+str(self.edad)+" "+self.email
