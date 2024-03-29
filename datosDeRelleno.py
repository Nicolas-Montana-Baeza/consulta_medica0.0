from pandas.core.frame import DataFrame
import clases
from random import randint
import datetime
import calendar
from math import floor
import pandas as pd
from dateutil import parser
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
            
            if len(_nombres[i])>=3 and clases.Persona.isRut(rut) and clases.Persona.isMail(email):
                nombre2=""
                if not(_nombres[i][1::-2]=="."):
                
                    for j in _nombres[i][1::-2]:
                        nombre2+=j+" "
                    
                    nombre2=nombre2[:-1]
                    nombre2=nombre2.replace(".","")
                persona_aux=clases.Medico(_nombres[i][0],nombre2,_nombres[i][-2],_nombres[i][-1],_ruts[i],_edades[i],_emails[i], "",_especialidades[i])
                personas.append(persona_aux)
    
        return personas
    else:
        return False

def crearEspecialidades(lista):
    especialidades=["MedicinaGeneral","Kinesiologia","Pediatria", "Odontologia"]
    lista_creada=[]
    
    for i in range(len(lista)):
        lista_creada.append(especialidades[randint(0,3)])
    return lista_creada

def crearDisponibilidad():
    disponibilidad=[]
    for year in range(2021,2023):
        for month in range(1,13):
            rango=calendar.monthrange(year,month)
            rango=str(rango)
            rango=rango[:-1]
            rango=rango[4:]
            rango=int(str(rango))

            for day in range(1,rango+1) :
                for hour in range(8,22):
                    for minute in [0,30]:
                        fecha=datetime.datetime(year,month,day,hour,minute)
                        if fecha.weekday()in range(0,5):
                            disponibilidad.append(fecha)
    return disponibilidad

"""
#se abren los archivos csv que contienen los datos
medicos_csv = open('./datos/Medicos.csv','r', newline="")
medicos_reader = csv.DictReader(medicos_csv)

pacientes_csv = open('./datos/Pacientes.csv','r',newline="")
pacientes_reader = csv.DictReader(pacientes_csv)

citas_csv = open('./datos/Citas.csv','r',newline="")
citas_reader = csv.DictReader(citas_csv)

for linea in medicos_reader:
    for atributo in medicos_reader.fieldnames:
        print(linea[atributo])
    print("##############")



#hay que agregar datos a la clinica

lista_nombres=["ADRIANA CAROLINA HERNANDEZ MONTERROZA", "MARCELA ADRIANA  REY SANCHEZ","ANDREA CATALINA ACERO CARO","BRIGITE . POLANCO RUIZ","CRISTINA ELIZABETH BARTHEL GUARDIOLA","GLORIA PATRICIA MENDOZA ALVEAR","LAURA . DIAZ MEJIA","MARIANA DEL PILAR SANTOS MILACHAY","PAOLA ANDREA CORREA LARIOS","YURI CATALINA SALAZAR ARISTIZABAL"]
lista_nombres=formatoNombres(lista_nombres)
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_nombres)
lista_edades=crearEdad(lista_nombres)
lista_especialidades=crearEspecialidades(lista_nombres)
disponibilidad=crearDisponibilidad()
lista_medicos=crearMedicos(lista_nombres,lista_ruts,lista_emails , lista_edades , lista_especialidades)
for medico in lista_medicos:
    medico.setDisponibilidad(disponibilidad)
"""
lista_citas=[]
pacientes_csv = pd.read_csv('./datos/Pacientes.csv')
lista_nombres= pacientes_csv["nombre completo"]
lista_ruts=pacientes_csv["rut"]
lista_emails=pacientes_csv["email"]
lista_edad=pacientes_csv["edad"]
lista_prevision=pacientes_csv["prevision"]
lista_numero=pacientes_csv["numero de telefono"]
lista_pacientes=[]
lista_nombres=formatoNombres(lista_nombres)

for i in range (len(lista_nombres)):
    n1=lista_nombres[i][0]
    n2=lista_nombres[i][1]
    ap1=lista_nombres[i][-2]
    ap2=lista_nombres[i][-1]
    if lista_nombres[i][-2]==lista_nombres[i][1]:
        n2=""
        
    paciente=clases.Paciente(n1,n2,ap1,ap2,lista_ruts[i],lista_edad[i],lista_emails[i],lista_numero[i])
    paciente.setPrevision(lista_prevision[i])
    lista_pacientes.append(paciente)

medicos_csv = pd.read_csv('./datos/Medicos.csv')
lista_nombres= medicos_csv["nombre completo"]
lista_ruts=medicos_csv["rut"]
lista_emails=medicos_csv["email"]
lista_edad=medicos_csv["edad"]
lista_especialidad=medicos_csv["especialidad"]
lista_numero=medicos_csv["numero de telefono"]
lista_medicos=[]
lista_nombres=formatoNombres(lista_nombres)

for i in range (len(lista_nombres)):
    n1=lista_nombres[i][0]
    n2=lista_nombres[i][1]
    ap1=lista_nombres[i][-2]
    ap2=lista_nombres[i][-1]
    if lista_nombres[i][-2]==lista_nombres[i][1]:
        n2=""
        
    medico=clases.Medico(n1,n2,ap1,ap2,lista_ruts[i],lista_edad[i],lista_emails[i],lista_numero[i],lista_especialidad[i])
    
    lista_medicos.append(medico)
clinica_objeto= clases.Clinica("Clinica de la Salud", "Público","Avenida Verdadera #123, Rancagua","", lista_medicos, lista_pacientes)

lista_citas=[]
cita_vacia=clases.Cita("","","","")
cita_csv = pd.read_csv('./datos/Citas.csv')
cita_csv=DataFrame(cita_csv)
codigo=cita_csv["codigo"].values
rut_paciente=cita_csv["rut paciente"].values
rut_medico=cita_csv["rut medico"].values
fecha_citada=cita_csv["fecha citada"].values
fecha_creacion=cita_csv["fecha de creacion"].values
modalidad=cita_csv["modalidad"].values
prestacion=cita_csv["prestacion"].values
confirmada=cita_csv["confirmada"].values
tiempo_restante=cita_csv["tiempo restante"].values

for i in range(len(codigo)):
    cita_vacia.setCodigo(codigo[i])
    cita_vacia.setPaciente(clinica_objeto.buscarPaciente(rut_paciente[i])[0])
    cita_vacia.setMedico(clinica_objeto.buscarMedico(rut_medico[i])[0])
    cita_vacia.setFechaCitada(parser.parse(fecha_citada[i]))
    cita_vacia.setFechaCreacion(parser.parse(fecha_creacion[i]))
    cita_vacia.setModalidad(modalidad[i])
    cita_vacia.setPrestacion(prestacion[i])
    cita_vacia.setConfirmada(confirmada[i])
    cita_vacia.actualizarEstado()
    lista_citas.append(cita_vacia)
for paciente in clinica_objeto.getPacientes():
    citas_paciente=[]
    for cita in lista_citas:
        if paciente.getRut()==cita.getPaciente().getRut():
            citas_paciente.append(cita)
    paciente.setCitas(citas_paciente)

for medico in clinica_objeto.getMedicos():
    citas_medico=[]
    for cita in lista_citas:
        if medico.getRut()==cita.getMedico().getRut():
            citas_medico.append(cita)
    medico.setCitas(citas_medico)      
#esto lo use para crear los archivos
"""
medicos_csv = open('./datos/Medicos.csv','w')
medicos_writer = csv.writer(medicos_csv)

medico_atributos= ['nombre completo', 'rut', 'edad', 'email','numero de telefono','especialidad']
medicos_writer.writerow(medico_atributos)

for medico in clinica_objeto.getMedicos():
    medico_info= [medico.getNombreCompleto(), medico.getRut(), medico.getEdad(), medico.getEmail(),medico.getNumeroTelefonico(),medico.getEspecialidad()]
    medicos_writer.writerow(medico_info)

pacientes_csv = open('./datos/Pacientes.csv', 'w')
pacientes_writer = csv.writer(pacientes_csv)
pacientes_reader= csv.DictReader(pacientes_csv)
pacientes_atributos= ['nombre completo', 'rut', 'edad', 'email','numero de telefono','prevision']
pacientes_writer.writerow(pacientes_atributos)

for paciente in clinica_objeto.getPacientes():
    paciente_info= [paciente.getNombreCompleto(), paciente.getRut(), paciente.getEdad(), paciente.getEmail(),paciente.getNumeroTelefonico(),paciente.getPrevision()]
    pacientes_writer.writerow(paciente_info)

citas_csv = open('./datos/Citas.csv', 'w')
citas_writer = csv.writer(citas_csv)
citas_reader= csv.DictReader(citas_csv)
citas_atributos= ['codigo', 'rut paciente', 'rut medico', 'fecha citada','fecha de creacion', 'modalidad','prestacion','confirmada','tiempo restante']
citas_writer.writerow(citas_atributos)

for paciente in clinica_objeto.getPacientes():
    cod_citas=[]
    for cita in paciente.getCitas():
        cod_citas.append(cita.getCodigo())
    for codigo in cod_citas:
        cita = paciente.buscarCita(codigo)
        cita_info= [cita.getCodigo(),cita.getPaciente().getRut(),cita.getMedico().getRut(), cita.getFechaCitada(), cita.getFechaActual(),cita.getModalidad(),cita.getPrestacion(),cita.getConfirmada(),cita.getTiempoRestante()]
        citas_writer.writerow(cita_info)
medicos_csv = open('./datos/Medicos.csv','r')
medicos_reader = csv.DictReader(medicos_csv)
"""