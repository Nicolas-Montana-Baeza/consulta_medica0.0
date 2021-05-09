import clinica
from random import randint
import datetime as dt
def formatoNombres(_nombres):
    nombres_aux=[]
   
    for nombre in _nombres:
        nombre=nombre.title().split()
        nombres_aux.append(nombre)
    
    return nombres_aux

def crearEmails(lista_nombres):
    lista_emails=[]
    
    for i in range(len(lista_nombres)):
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

lista_nombres=["ADRIANA CAROLINA HERNANDEZ MONTERROZA", "MARCELA ADRIANA  REY SANCHEZ","ANDREA CATALINA ACERO CARO","BRIGITE . POLANCO RUIZ","CRISTINA ELIZABETH BARTHEL GUARDIOLA","GLORIA PATRICIA MENDOZA ALVEAR","LAURA . DIAZ MEJIA","MARIANA DEL PILAR SANTOS MILACHAY","PAOLA ANDREA CORREA LARIOS","YURI CATALINA SALAZAR ARISTIZABAL"]
lista_nombres=formatoNombres(lista_nombres)
print(lista_nombres)
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_nombres)
print(lista_emails)
lista_edades=crearEdad(lista_nombres)
print(lista_edades)
lista_especialidades=crearEspecialidades(lista_nombres)
print(lista_especialidades)
lista_medicos=crearMedicos(lista_nombres,lista_ruts,lista_emails , lista_edades , lista_especialidades)
lista_citas=[]
lista_pacientes=[clinica.Paciente("juan", "pedro","perez","gonzales","14077811-7","23","juanito.perez@gmail.com","")]
clinica_objeto= clinica.Clinica("Clinica de la Salud", "Público","Avenida Verdadera #123, Rancagua","", lista_medicos, lista_pacientes, lista_citas)
cita_aux=clinica.Cita()
lista_entry_datos_paciente=[]
color1="#788890"
color2="#28388f"
color3="#accdec"
color4="#6d6e72"
ruts=[]
fecha_actual=dt.datetime.now()
print(fecha_actual)