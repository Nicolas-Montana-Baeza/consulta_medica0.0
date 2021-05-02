from cita import Cita
import datetime as dt
from math import floor
class Clinica():

    def __init__(self):
        self.nombre=""
        self.direccion=""
        self.tipo=""
        self.horario=[]
        self.medicos=[]
        self.pacientes=[]

    def setNombre(self,nombre):
        self.nombre=nombre 

    def setDireccion(self,direccion):
        self.direccion=direccion

    def setTipo(self,tipo):
        self.tipo=tipo

    def setEspecialidades(self,especialidades):
        self.especialidades=especialidades

    def setHorario(self,horario):
        self.horario=horario

    def setDoctores(self,doctores):
        self.doctores=doctores

    def setPacientes(self,pacientes):
        self.pacientes=pacientes

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getTipo(self):
        return self.tipo

    def getEspecialidades(self):
        return self.especialidades

    def getHorario(self):
        return self.horario
    
    def getCitas(self):
        return self.citas
    
    def getDoctores(self):
        return self.doctores

    def getPacientes(self):
        return self.pacientes
    
    def buscarPaciente(self,buscar):
        coincidencias=[]
        buscar=buscar.lower()
        for paciente in self.pacientes:

            if paciente.nombre.lower().find(buscar)!=-1:
                coincidencias.append(paciente)

            elif paciente.isRut(buscar):

                if paciente.rut.find(buscar)!=-1:
                    coincidencias.append(paciente)

        return coincidencias
           
    def buscarMedico(self,buscar):
        coincidencias=[]
        buscar=buscar.lower()
        for medico in self.medicos:

            if medico.nombre.lower().find()!=-1:
                coincidencias.append(medico)

            elif medico.isRut(buscar):

                if medico.rut.find(buscar)!=-1:
                    coincidencias.append(medico)

            elif medico.especialidad.lower().find(buscar)!=-1:
                coincidencias.append(medico)

        return coincidencias    
    
   

    def agregarPaciente(self, _paciente):
        try:
            self.pacientes.append(_paciente)
            return True
        except:
            return False
        
    def agregarMedico(self, _medico):
            try:
                self.medicos.append(_medico)
                return True
            except:
                return False

    def __str__(self):
        return self.nombre+" "+self.direccion+" "+self.tipo+" "+str(self.especialidades)+" "+str(self.horario)+" "+str(self.citas)+" "+str(self.doctores)+" "+str(self.pacientes)

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

    #def asignarCodigo(self, _objeto):

    def buscarCita(self,buscar):
            
            for cita in self.citas:
                coincidencias=[]
                
                if cita.paciente.nombre.lower().find(buscar)!=-1 or cita.medico.nombre.lower().find(buscar)!=-1:
                    coincidencias.append(cita)

                elif cita.isRut(buscar) :

                    if cita.paciente.rut.find(buscar)!=-1 or cita.medico.rut.find(buscar)!=-1:
                        coincidencias.append(cita)

                elif cita.medico.especialidad.lower().find(buscar)!=-1:
                    coincidencias.append(cita)
                
                elif cita.fecha==buscar:
                    coincidencias.append(cita)
                
                elif cita.codigo==buscar:
                    coincidencias.append(cita)

            return coincidencias  
    
    def agendarCita(self,_cita):
        self.citas.append(_cita)

    def reagendarCita(self, _fecha, _codigo_cita):
        return "not implemented yet"
    
    def confirmarCita(self,_cita):
        _cita.setConfirmada(True)

    def __str__(self) :
        return self.apellido_paterno+" "+self.apellido_materno+" "+self.primer_nombre+" "+self.segundo_nombre+" "+self.rut+" "+str(self.edad)+" "+self.email

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
        self.recetas=[]

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

    def setRecetas(self,recetas):
        self.recetas=recetas

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

    def getRecetas(self):
        return self.citas

      
    def cancelarCita(self, _codigo_cita):

        for i in range (len(self.citas)):

            if _codigo_cita==self.citas[i].codigo:
                self.citas.pop(i)
                return True

        return False


    def pagarCita(self,_cita,_monto_a_pagar):
        if _monto_a_pagar>self.cartera:
            return False
        else:
            _cita.setPagado(True)
            return True

    def __str__(self):
        return self.prevision+" "+self.ultima_prestacion+" "+self.requerimientos+" "+self.diagnosticos+" "+self.forma_pago

class Receta():

    def __init__(self):
        self.paciente= Paciente()
        self.medico= Medico()
        self.farmaco_y_dosis=[]
        self.fecha=""
        self.duracion=""
        self.observaciones=[]
        self.dosis=""
    
    def setPaciente(self,paciente):
        self.paciente=paciente
    
    def setMedico(self,medico):
        self.medico=medico

    def setFarmacoYDosis(self,farmaco_y_dosis):
        self.farmaco_y_dosis=farmaco_y_dosis

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

    def getFarmacoYDosis(self):
        return self.farmaco_y_dosis
    
    def getFecha(self):
        return self.fecha

    def getDuracion(self):
        return self.duracion

    def getObservaciones(self):
        return self.observaciones

    def getDosis(self):
        return self.dosis

    def isValida(self):
        """if dt.datetime.now()-self.fecha>self.duracion:
            return True"""
        return "not implemented yet"
  
