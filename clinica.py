import datetime as dt
from math import floor
import re
import shortuuid

class Clinica():

    def __init__(self,_nombre,_tipo,_direccion,_horario,_medicos,_pacientes,_citas):
        self.nombre=_nombre
        self.tipo=_tipo
        self.direccion=_direccion
        self.horario=_horario
        self.medicos=_medicos
        self.pacientes=_pacientes
        self.citas=_citas
    
    def setNombre(self,nombre):
        self.nombre=nombre 

    def setTipo(self,tipo):
        self.tipo=tipo
    
    def setDireccion(self,direccion):
        self.direccion=direccion

    def setHorario(self,horario):
        self.horario=horario

    def setMedicos(self,medicos):
        self.medicos=medicos

    def setPacientes(self,pacientes):
        self.pacientes=pacientes

    def setCitas(self, citas):
        self.citas=citas

    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo

    def getDireccion(self):
        return self.direccion

    def getHorario(self):
        return self.horario
    
    def getMedicos(self):
        return self.medicos

    def getPacientes(self):
        return self.pacientes
    
    def getCitas(self):
        return self.citas
    
    def buscarPaciente(self,buscar):
        coincidencias=[]
        if len(buscar)==0:
            return coincidencias
        for paciente in self.pacientes:

            if paciente.getNombreCompleto().find(buscar.title())!=-1:
                coincidencias.append(paciente)

            elif Paciente.isRut(buscar):

                if paciente.getRut().find(buscar)!=-1:
                    coincidencias.append(paciente)

        return coincidencias
           
    def buscarMedico(self,buscar):
        coincidencias=[]
        buscar=buscar.lower()
        for medico in self.medicos:

            if medico.getNombreCompleto().lower().find(buscar)!=-1:
                coincidencias.append(medico)

            elif Medico.isRut(buscar):

                if medico.getRut().find(buscar)!=-1:
                    coincidencias.append(medico)

            elif medico.getEspecialidad().lower().find(buscar)!=-1:
                coincidencias.append(medico)

        return coincidencias    
    
    def buscarCita(self,buscar):

        for cita in self.citas:

            if cita.getCodigo()==buscar:
                return cita

    
    def agregarPaciente(self, _paciente):
        self.pacientes.append(_paciente) 
        
    def agregarMedico(self, _medico):
        self.medicos.append(_medico)

    def __str__(self):
        return self.nombre+" "+self.direccion+" "+self.tipo+" "+str(self.especialidades)+" "+str(self.horario)+" "+str(self.citas)+" "+str(self.doctores)+" "+str(self.pacientes)

class Cita ():
    
    def __init__(self, fecha_citada, medico, paciente, modalidad):
        #
        self.fecha_citada=dt.datetime(1,1,1)

        self.fecha_actual=dt.datetime.now()
    #
        self.medico= Medico()
    #
        self.paciente=Paciente()
        self.direccion=""
        self.codigo=str(shortuuid.uuid())
    #esta depende del medico
        self.prestacion=""
        self.pagado=False
    #
        self.modalidad=""
    #esto no creo que sea necesaria
        self.prioridad=""
    #fecha citada menos fecha actual
        self.tiempo_restante="s"
        self.confirmada=False

    def setFechaCitada(self,fecha_citada):
        self.fecha_citada = fecha_citada
    
     def setFechaActual(self,fecha_actual):
        self.fecha_actual = fecha_actual

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

    def setPagado(self,pagado):
        self.pagado=pagado

    def setModalidad(self,modalidad):
        self.modalidad=modalidad
    
    def setTiempoRestante(self,tiempo_restante):
        self.tiempo_restante=tiempo_restante

    def setConfirmada(self,confirmada):
        self.confirmada=confirmada

    def getFechaCitada(self):
        return self.fecha_citada

    def getFechaActual(self):
        return self.fecha_actual

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

    def getPagado(self):
        return self.pagado

    def getModalidad(self):
        return self.modalidad
    
    def getTiempoRestante(self):
        return self.tiempo_restante
    
    def getConfirmada(self):
        return self.confirmada

    def actualizarEstado(self):
        fecha_actual=dt.datetime.now()
        fecha_restante=self.fecha_citada-fecha_actual

        if fecha_restante==0:
            self.setEstadoTemporal("Cita en curso...")

        elif fecha_restante>0:
            self.setEstadoTemporal("Quedan "+str(fecha_restante)+" dias para su cita...")

        elif fecha_restante<0:
            self.setEstadoTemporal("su cita fue hace "+str(-1*fecha_restante)+" días")

class Persona():

    def __init__(self,_nombre1,_nombre2,_apellido1,_apellido2,_rut,_edad,_email,_numero_telefonico):
        self.nombre1=_nombre1
        self.nombre2=_nombre2
        self.apellido1=_apellido1
        self.apellido2=_apellido2
        self.edad=_edad
        self.rut=_rut
        self.email=_email
        self.numero_telefonico=_numero_telefonico
         
    def setPrimerNombre(self,nombre1):
        self.nombre1=nombre1
        
    def setSegundoNombre(self,nombre2):
        self.nombre2=nombre2
        
    def setPrimerApellido(self,apellido1):
        self.apellido1=apellido1

    def setSegundoApellido(self,apellido2):
        self.apellido2=apellido2
        
    def setNumeroTelefonico(self,numero_telefonico):
        self.numero_telefonico=numero_telefonico
        
    def setEdad(self,edad):
        self.edad=edad

    def setRut(self,rut):
        self.rut=rut

    def setEmail(self,email):
        self.email=email

    def getPrimerNombre(self):
        return self.nombre1

    def getSegundoNombre(self):
        return self.nombre2

    def getPrimerApellido(self):
        return self.apellido1

    def getSegundoApellido(self):
        return self.apellido2

    def getNumeroTelefonico(self):
        return self.numero_telefonico

    def getEmail(self):
        return self.email

    def getEdad(self):
        return self.edad

    def getRut(self):
        return self.rut
    
    def getNumeroTelefonico(self):
        return self.numero_telefonico
    
    def isMail(email):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        
        if(re.search(regex, email)):
           return True
    
        else:
            return False

    def isRut(_rut):
        rut=_rut.replace("-","")
        verificador=rut[-1]
        verificando=rut[:-1]
        verificando=verificando[::-1]
        if len(verificador) ==0 or not(rut.isdigit()):
            return False

        serie="234567"
        recorre_serie=0
    
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

    def agendarCita(self,_cita):
        self.citas.append(_cita)

    def reagendarCita(self, _fecha, _codigo_cita):
        return "not implemented yet"
    
    def confirmarCita(self,_cita):
        _cita.setConfirmada(True)
 
    def getNombreCompleto(self):
        return str(self.nombre1).title()+" "+str(self.nombre2).title()+" "+str(self.apellido1).title()+" "+str(self.apellido2).title()
  


            
        
        
    
    def __str__(self):
        return str(self.apellido1)+" "+str(self.apellido2)+" "+str(self.nombre1)+" "+str(self.nombre2)+" "+self.rut+" "+str(self.edad)+" "+self.email

class Medico(Persona):

    def __init__(self,_nombre1,_nombre2,_apellido1,_apellido2,_rut,_edad,_email,_numero_telefonico,_especialidad):
        super().__init__(_nombre1,_nombre2,_apellido1,_apellido2,_rut,_edad,_email,_numero_telefonico)
        self.pacientes=[]
        self.disponibilidad=[]
        self.especialidad=_especialidad

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

    def isDisponible(self, _fecha):
        for disponible in self.disponibilidad:
            if _fecha==disponible: 
                return True
        return False

    def diagnosticarPaciente(self, _diagnostico, _paciente):
        _diagnostico=_paciente.getDiagnosticos().append(_diagnostico)
        _paciente.setDiagnosticos(_diagnostico)

    def __str__(self) :
        return str(self.apellido1)+" "+str(self.apellido2)+" "+str(self.nombre1)+" "+str(self.nombre2)+" "+" "+str(self.especialidad)

class Paciente(Persona): 
    def __init__(self,_nombre1,_nombre2,_apellido1,_apellido2,_rut,_edad,_email,_numero_telefonico):
        super().__init__(_nombre1,_nombre2,_apellido1,_apellido2,_rut,_edad,_email,_numero_telefonico)
        self.prevision="Sin Prevision"
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

    def pagarCita(self,_cita,_monto_a_pagar):
        if _monto_a_pagar>self.cartera:
            return 
        else:
            _cita.setPagado(True)

    def __str__(self):
        return super().__str__()+" "+str(self.prevision)+" "+str(self.ultima_prestacion)+" "+str(self.requerimientos)+" "+str(self.diagnosticos)+" "+str(self.forma_pago)

class Receta():

    def __init__(self):
        #
        self.paciente= Paciente()
        #
        self.medico= Medico()
        #
        self.farmaco_y_dosis=[]
        #
        self.fecha=""
        #
        self.duracion=""
        #
        self.observaciones=[]
        #
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