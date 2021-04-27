from cita import Cita

class Clinica():

    def __init__(self):
        self.nombre=""
        self.direccion=""
        self.tipo=""
        self.especialidades=[]
        self.horario=[]
        self.citas=[]
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

    def setCitas(self,citas):
        self.citas=citas

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

