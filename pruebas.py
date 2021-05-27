import clases
from random import randint
import datetime as dt
from math import floor
import csv
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
                nombre2=_nombres[i][1::-2]
                nombre2=nombre2[0]
                persona_aux=clases.Medico(_nombres[i][0],nombre2,_nombres[i][-2],_nombres[i][-1],_ruts[i],_edades[i],_emails[i], "",_especialidades[i])
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
#print(lista_nombres)
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_nombres)
#print(lista_emails)
lista_edades=crearEdad(lista_nombres)
#print(lista_edades)
lista_especialidades=crearEspecialidades(lista_nombres)
#print(lista_especialidades)
lista_medicos=crearMedicos(lista_nombres,lista_ruts,lista_emails , lista_edades , lista_especialidades)
lista_citas=[]
lista_pacientes=[clases.Paciente("juan", "pedro","perez","gonzales","14077811-7","23","juanito.perez@gmail.com","")]
clases_objeto= clases.Clinica("Clinica de la Salud", "Público","Avenida Verdadera #123, Rancagua","", lista_medicos, lista_pacientes)

lista_entry_datos_paciente=[]
color1="#788890"
color2="#28388f"
color3="#accdec"
color4="#6d6e72"
ruts=[]
fecha_actual=dt.datetime.now()
fecha_citada=dt.datetime(2021,6,9,14,30)
cita_auxiliar=clases.Cita(fecha_citada,lista_medicos[0], lista_pacientes[0], "Online")
lista_pacientes[0].agregarCita(cita_auxiliar)
lista_medicos[0].agregarCita(cita_auxiliar)
def isRut(_rut):
        if len(_rut)==0:
            return False
        rut=_rut.replace("-","")
        
        verificador=rut[-1]
        print(verificador)
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
        print(verificar)
        if verificar==int(verificador):
            return True
        else:
            return False

#esto lo use para crear los archivos
"""
medicos_csv = open('./datos/Medicos.csv','w')
medicos_writer = csv.writer(medicos_csv)

medico_atributos= ['nombre completo', 'rut', 'edad', 'email','numero de telefono','especialidad']
medicos_writer.writerow(medico_atributos)

for medico in clases_objeto.getMedicos():
    medico_info= [medico.getNombreCompleto(), medico.getRut(), medico.getEdad(), medico.getEmail(),medico.getNumeroTelefonico(),medico.getEspecialidad()]
    medicos_writer.writerow(medico_info)

pacientes_csv = open('./datos/Pacientes.csv', 'w')
pacientes_writer = csv.writer(pacientes_csv)
pacientes_reader= csv.DictReader(pacientes_csv)
pacientes_atributos= ['nombre completo', 'rut', 'edad', 'email','numero de telefono','prevision']
pacientes_writer.writerow(pacientes_atributos)

for paciente in clases_objeto.getPacientes():
    paciente_info= [paciente.getNombreCompleto(), paciente.getRut(), paciente.getEdad(), paciente.getEmail(),paciente.getNumeroTelefonico(),paciente.getPrevision()]
    pacientes_writer.writerow(paciente_info)

citas_csv = open('./datos/Citas.csv', 'w')
citas_writer = csv.writer(citas_csv)
citas_reader= csv.DictReader(citas_csv)
citas_atributos= ['codigo', 'rut paciente', 'rut medico', 'fecha citada','fecha de creacion', 'modalidad','prestacion','confirmada','tiempo restante']
citas_writer.writerow(citas_atributos)

for paciente in clases_objeto.getPacientes():
    cod_citas=[]
    for cita in paciente.getCitas():
        cod_citas.append(cita.getCodigo())
    for codigo in cod_citas:
        cita = paciente.buscarCita(codigo)
        cita_info= [cita.getCodigo(),cita.getPaciente().getRut(),cita.getMedico().getRut(), cita.getFechaCitada(), cita.getFechaActual(),cita.getModalidad(),cita.getPrestacion(),cita.getConfirmada(),cita.getTiempoRestante()]
        citas_writer.writerow(cita_info)
medicos_csv = open('./datos/Medicos.csv','r')
medicos_reader = csv.DictReader(medicos_csv)
for linea in medicos_reader:
    print(linea)
"""
import pandas as pd
import matplotlib.pyplot as plt


datos_medicos = pd.read_csv('./datos/Medicos.csv')
esp=datos_medicos["especialidad"]
cantidad_especialidad= esp.value_counts()
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]

plt.pie(cantidad_especialidad.array, labels=cantidad_especialidad.index, colors=colors, autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*cantidad_especialidad.array.sum()))
plt.title("cantidad de especialistas")
plt.show()
