import datetime as dt
from math import floor
import re
import shortuuid
#clases necesarias para nuestro despacho
class Clinica():

    def __init__(self,_nombre,_tipo,_direccion,_horario,_medicos,_pacientes):
        self.nombre=_nombre
        self.tipo=_tipo
        self.direccion=_direccion
        self.horario=_horario
        self.medicos=_medicos
        self.pacientes=_pacientes
   
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
        return self.medicos.getCitas()

    #funcion para buscar un paciente dentro de los ya ingresados
    def buscarPaciente(self,buscar):
        coincidencias=[]
        buscar=buscar.lower()
        if len(buscar)==0:
            return coincidencias
        for paciente in self.pacientes:

            if paciente.getNombreCompleto().lower().find(buscar.title())!=-1:
                coincidencias.append(paciente)

            elif Paciente.isRut(buscar):

                if paciente.getRut().find(buscar)!=-1:
                    coincidencias.append(paciente)

        return coincidencias

    #funcion para agregar un nuevo paciente      
    def agregarPaciente(self, _paciente):
        for paciente in self.pacientes:
            if paciente.getRut==_paciente.getRut():
                return False
        self.pacientes.append(_paciente)
        return True

    #funcion para eliminar un paciente ya ingresado
    def eliminarPaciente(self,_rut):
        for paciente in self.pacientes:
            if paciente.getRut==_rut:
                self.pacientes.remove(paciente)
                return True
        return False
    
    #funcion para modificar datos del paciente ya ingresado
    def modificarPaciente(self,_paciente):
        for paciente in self.pacientes:
            if paciente.getRut==_paciente.getRut():
                paciente.setPrimerNombre(_paciente.getPrimerNombre())
                paciente.setSegundoNombre(_paciente.getSegundoNombre())
                paciente.setPrimerApellido(_paciente.getPrimerApellido())
                paciente.setSegundoApellido(_paciente.getSegundoApellido())
                paciente.setRut(_paciente.getRut())
                paciente.setEdad(_paciente.getEdad())
                paciente.setEmail(_paciente.getEmail())
                paciente.setNumeroTelefonico(_paciente.getNumeroTelefonico())
                return True
        return False

    #funcion para buscar un medico existente
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

    #funcion para agregar un nuevo medico
    def agregarMedico(self, _medico):
        for medico in self.medicos:
            if medico.getRut==_medico.getRut():
                return False
        self.medicos.append(_medico)
        return True
    #funcion para eliminar un medico existente
    def eliminarMedico(self,_rut):
        for medico in self.medicos:
            if medico.getRut==_rut:
                self.medicos.remove(medico)
                return True
        return False

    #funcion para modificar datos de un medico ya ingresado
    def modificarMedico(self,_medico):
        for medico in self.medicos:
            if medico.getRut==_medico.getRut():
                medico.setPrimerNombre(_medico.getPrimerNombre())
                medico.setSegundoNombre(_medico.getSegundoNombre())
                medico.setPrimerApellido(_medico.getPrimerApellido())
                medico.setSegundoApellido(_medico.getSegundoApellido())
                medico.setRut(_medico.getRut())
                medico.setEdad(_medico.getEdad())
                medico.setEmail(_medico.getEmail())
                medico.setNumeroTelefonico(_medico.getNumeroTelefonico())
                medico.setEspecialidad(_medico.getEspecialidad())
                return True
        return False

    #funcion para mostrar los datos ya recopilados
    def __str__(self):
        return self.nombre+" "+self.direccion+" "+self.tipo+" "+str(self.horario)+" "+str(self.medicos)+" "+str(self.pacientes)

class Cita ():
    
    def __init__(self, fecha_citada, medico, paciente, modalidad,fecha_actual=dt.datetime.now()):
        
        self.fecha_citada=fecha_citada
        self.fecha_actual=dt.datetime.now()
        self.medico= medico
        self.paciente= paciente
        self.direccion=""
        self.codigo=str(shortuuid.uuid())
        self.prestacion=medico.getEspecialidad()
        self.pagado=False
        self.modalidad=""
        self.prioridad=""
        self.tiempo_restante=self.fecha_citada-self.fecha_actual
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
    
    def setPrioridad(self,prioridad):
        self.prioridad=prioridad
    
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

    def getPrioridad(self):
        return self.prioridad
    
    def getTiempoRestante(self):
        return self.tiempo_restante
    
    def getConfirmada(self):
        return self.confirmada

    #funcion para actualizar el estado de una cita segun en cual se encuentre
    def actualizarEstado(self):
        fecha_actual=dt.datetime.now()       
        fecha_restante=self.fecha_citada-fecha_actual

        self.tiempo_restante = fecha_restante
    
    #funcion para mostrar los datos ya recopilados
    def __str__(self):
        return self.fecha_citada+" "+ self.codigo+" "+self.fecha_actual+" "+self.medico+" "+self.paciente+" "+self.modalidad+" "+self.prestacion+" "+str(self.pagado)

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

    def setNumero(self,numero):
        self.numero=numero

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
    
    def getEdad(self):
        return self.edad

    def getRut(self):
        return self.rut
    
    def getEmail(self):
        return self.email
    
    def getNumero(self):
        return self.numero
    

    
    #funcion para verificar si un correo es valido o no
    def isMail(email):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        
        if(re.search(regex, email)):
           return True
    
        else:
            return False

    #funcion para verificar si un rut es valido o no
    def isRut(_rut):
        if len(_rut)==0:
            return False
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
        if verificar==11:
            verificar=0
        if verificar==int(verificador):
            return True
        else:
            return False
            
    #funcion para buscar una cita agendada
    def buscarCita(self,buscar):
        for cita in self.citas:
            if cita.getCodigo()==buscar:
                return cita
        return False

    #funcion para agendar una cita
    def agendarCita(self, _agendar):
        for cita in self.citas:
            if cita.getCodigo()==_agendar.getCodigo() or cita.getFechaCitada()==_agendar.getFechaCitada():
                return False
        self.citas.append(_agendar)
        return True

    #funcion para eliminar una cita agendada
    def eliminarCita(self,_codigo):
        for cita in self.citas:
            if cita.getCodigo==_codigo:
                self.citas.remove(cita)
                return True
        return False

    #funcion para modificar una cita agendada
    def modificarCita(self,fecha_citada,codigo):
        for cita in self.citas:
            if cita.getFechaCitada()==fecha_citada:
                return False
            if cita.getCodigo==codigo:
                cita.setfechaCitada(fecha_citada)
                return True
        return False

    #funcion para confirmar una cita
    def confirmarCita(self,codigo):
        for cita in self.citas:
            if cita.getCodigo()==codigo:
                cita.setConfirmada(True)
                return True
        return False

    #funcion para retornar el nombre completo de una persona
    def getNombreCompleto(self):
        return str(self.nombre1).title()+" "+str(self.nombre2).title()+" "+str(self.apellido1).title()+" "+str(self.apellido2).title()

    #funcion para retornar una representacion de todos los atributos del objeto
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
    

    #funcion para entregarle una receta al paciente
    def recetarPaciente(self, _receta,_paciente):
        _receta=_paciente.getRecetas.append(_receta)
        _paciente.set(_receta)

    #funcion para solicitar examen a un paciente
    def requerirExamen(self, _examen, _paciente):
        _examen=_paciente.getRequerimientos().append(_examen)
        _paciente.setRequerimientos(_examen)

    #funcion para verificar la fecha de cita esta disponible
    def isDisponible(self, _fecha):
        for disponible in self.disponibilidad:
            if _fecha==disponible: 
                return True
        return False

    #funcion para diagnosticar a un paciente
    def diagnosticarPaciente(self, _diagnostico, _paciente):
        _diagnostico=_paciente.getDiagnosticos().append(_diagnostico)
        _paciente.setDiagnosticos(_diagnostico)

    #funcion que retorna el nombre completo de un medico junto a su especialidad
    def __str__(self) :
        return str(self.nombre1)+" "+str(self.nombre2)+" "+str(self.apellido1)+" "+str(self.apellido2)+" "+str(self.especialidad)+" "+str(self.pacientes)+" "+str(self.disponibilidad)

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

    def setCartera(self,cartera):
        self.cartera=cartera

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
    
    def getCartera(self):
        return self.cartera
    
    def getCitas(self):
        return self.citas

    def getRecetas(self):
        return self.citas

    #funcion desarrollada para cancelar una cita  
    def cancelarCita(self, _codigo_cita):

        for i in range (len(self.citas)):

            if _codigo_cita==self.citas[i].codigo:
                self.citas.pop(i)

    #funcion realizada para pagar una cita
    def pagarCita(self,_cita,_monto_a_pagar):
        if _monto_a_pagar>self.cartera:
            return 
        else:
            _cita.setPagado(True)

    #funcion para retornar los antecedentes entregados del pacientes
    def __str__(self):
        return super().__str__()+" "+str(self.prevision)+" "+str(self.ultima_prestacion)+" "+str(self.requerimientos)+" "+str(self.diagnosticos)+" "+str(self.forma_pago)

class Receta():

    def __init__(self, paciente, medico, farmaco_y_dosis, fecha, duracion, observaciones, dosis):
        
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

    #funcion que retorna lo recetado por el medico al paciente, junto a sus indicaciones
    def __str__(self):
        return str(self.paciente+" "+ self.medico+" "+ self.farmaco_y_dosis+" "+self.fecha+" "+self.duracion+" "+self.observaciones+" "+self.dosis)
