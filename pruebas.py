import clinica
from random import randint
def formatoNombres(_nombres):
    nombres_aux=[]
   
    for nombre in _nombres:
        nombre=nombre.title().split()
        nombres_aux.append(nombre)
    
    return nombres_aux

def crearEmails(lista_nombres):
    lista_emails=[]
    lista_doctores=formatoNombres(lista_nombres)
    
    for i in range(len(lista_doctores)):
        lista_emails.append(lista_nombres[i][0].upper()+"."+lista_nombres[i][-2].upper()+"@gmail.com")
    
    return lista_emails

def crearEdad(lista):
    edades=[]
    for i in range(len(lista)):
        edad=randint(25,63)
        edades.append(edad)
    return edades

def crearMedicos(_nombres,_ruts, _emails,_edades,_especialidades):
    personas=[]
    _nombres=formatoNombres(_nombres)
    
    if len(_nombres)==len(_ruts) and len(_ruts) == len(_emails) and len(_emails)==len(_edades):
        
        for i in range (len(_nombres)):
            rut=_ruts[i]
            email=_emails[i]
            print(clinica.Persona.isRut(rut))
            if len(_nombres[i])>=3 and clinica.Persona.isRut(rut) and clinica.Persona.isMail(email):
                persona_aux=clinica.Medico(_nombres[i][0],_nombres[i][1::-2],_nombres[i][-2],_nombres[i][-1],_ruts[i],_edades[i],_emails[i], "",_especialidades[i])
                personas.append(persona_aux)
    
        return personas
    else:
        return False

def crearEspecialidades(lista):
    especialidades=["Medicina General","Kinesiologia","Pediatria", "Odontologia"]
    lista_creada=[]
    
    for i in range(len(lista)):
        lista_creada.append(especialidades[randint(0,3)])
    return lista_creada
"""
def autocompletar_paciente():

    _busqueda=busqueda.get()
    paciente=clinica_objeto.buscarPaciente(_busqueda)[0]
    datos_paciente=[ paciente.getSegundoNombre(),paciente.getPrimerApellido(), paciente.getSegundoApellido(), paciente.getNumeroTelefonico(),paciente.getEmail()]
    prevision_btn.set(paciente.getPrevision())
    nombre1_entry.delete(0)
    nombre2_entry.delete(0)
    apellido1_entry.delete(0)
    apellido2_entry.delete(0)
    tel_contacto_entry.delete(0)
    email_entry.delete(0)
    nombre1_entry.insert(0,paciente.getPrimerNombre())
    nombre2_entry.instert(0,paciente.getSegundoNombre())
    apellido1_entry.instert(0,paciente.getPrimerApellido())
    apellido2_entry.instert(0,paciente.getSegundoApellido())
    tel_contacto_entry.instert(0,paciente.getNumeroTelefonico())
    email_entry.instert(0,paciente.getEmail())
"""

"""def crearMedicos(_lista,_lista_especialidades):
    medicos=[]
    for i in range(len(_lista)):
       medicos.append(Medico(_lista[i],_lista_especialidades))
    return medicos
lista_doctores=["ADRIANA CAROLINA HERNANDEZ MONTERROZA", "MARCELA ADRIANA  REY SANCHEZ","ANDREA CATALINA ACERO CARO","BRIGITE . POLANCO RUIZ","CRISTINA ELIZABETH BARTHEL GUARDIOLA","GLORIA PATRICIA MENDOZA ALVEAR","LAURA . DIAZ MEJIA","MARIANA DEL PILAR SANTOS MILACHAY","PAOLA ANDREA CORREA LARIOS","YURI CATALINA SALAZAR ARISTIZABAL"]
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_doctores)
lista_edades=crearEdad(lista_doctores)
lista_especialidades=crearEspecialidades(lista_doctores)
lista_medicos=crearMedicos(lista_doctores,lista_ruts,lista_emails,lista_edades,lista_especialidades)


if len(lista_doctores)==len(lista_ruts):
    for i in range (len(lista_doctores)):
        print("entre"+str(i))
        if len(lista_doctores[i])>=3:
                print("cree")
                persona_aux=Persona(lista_doctores[i][0],lista_doctores[i][1::-2],lista_doctores[i][-2],lista_doctores[i][-1],lista_ruts[i],lista_edades[i],lista_emails,"")
                lista_personas.append(persona_aux)
print("sali")


for persona in lista_medicos:
    print(persona.getEspecialidad())
"""


lista_doctores=["ADRIANA CAROLINA HERNANDEZ MONTERROZA", "MARCELA ADRIANA  REY SANCHEZ","ANDREA CATALINA ACERO CARO","BRIGITE . POLANCO RUIZ","CRISTINA ELIZABETH BARTHEL GUARDIOLA","GLORIA PATRICIA MENDOZA ALVEAR","LAURA . DIAZ MEJIA","MARIANA DEL PILAR SANTOS MILACHAY","PAOLA ANDREA CORREA LARIOS","YURI CATALINA SALAZAR ARISTIZABAL"]
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_doctores)
lista_edades=crearEdad(lista_doctores)
lista_especialidades=crearEspecialidades(lista_doctores)
lista_medicos=crearMedicos(lista_doctores,lista_ruts,lista_emails , lista_edades , lista_especialidades)
lista_citas=[]
lista_pacientes=[clinica.Paciente("juan", "pedro","perez","gonzales","14077811-7","23","juanito.perez@gmail.com","")]
clinica_objeto= clinica.Clinica("Clinica de la Salud", "Público","Avenida Verdadera #123, Rancagua","", lista_medicos, lista_pacientes, lista_citas)
cita_aux=clinica.Cita()
lista_entry_datos_paciente=[]
color1="#788890"
color2="#28388f"
color3="#accdec"
color4="#6d6e72"
#lista_paciente=clinica_objeto.getPacientes()
ruts=[]
for i in clinica_objeto.getMedicos():
    ruts.append(i.getRut())
rut=clinica_objeto.getPacientes()[0].getRut()

paciente=clinica_objeto.buscarPaciente("14077811-7")
print(type(paciente))

#print(clinica_objeto.buscarPaciente(lista_pacientes[0].getRut()))

