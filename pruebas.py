import clases
from random import randint
import datetime as dt
from math import floor
import csv
import matplotlib.pyplot as plt
import numpy as np
from heapq import merge
from collections import OrderedDict
import pandas as pd

from tkinter import Toplevel,BOTTOM,X,font,BOTH, Listbox,S,Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame,W,StringVar,FLAT,END,N,Text,ACTIVE,Scrollbar,RIGHT,Y,LEFT,Spinbox
from PIL import Image,ImageTk
from ttkbootstrap import Style
from datosDeRelleno import *
from PIL import ImageTk
import PIL
from estilo import *
import datetime as dt
from datosDeRelleno import *
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

def crearMedicos(_nombres,_ruts, _emails,_datoses,_especialidades):
    personas=[]
    
    if len(_nombres)==len(_ruts) and len(_ruts) == len(_emails) and len(_emails)==len(_datoses):
        
        for i in range (len(_nombres)):
            rut=_ruts[i]
            email=_emails[i]
    
            if len(_nombres[i])>=3 and clases.Persona.isRut(rut) and clases.Persona.isMail(email):
                nombre2=_nombres[i][1::-2]
                nombre2=nombre2[0]
                persona_aux=clases.Medico(_nombres[i][0],nombre2,_nombres[i][-2],_nombres[i][-1],_ruts[i],_datoses[i],_emails[i], "",_especialidades[i])
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

"""
lista_nombres=["ADRIANA CAROLINA HERNANDEZ MONTERROZA", "MARCELA ADRIANA  REY SANCHEZ","ANDREA CATALINA ACERO CARO","BRIGITE . POLANCO RUIZ","CRISTINA ELIZABETH BARTHEL GUARDIOLA","GLORIA PATRICIA MENDOZA ALVEAR","LAURA . DIAZ MEJIA","MARIANA DEL PILAR SANTOS MILACHAY","PAOLA ANDREA CORREA LARIOS","YURI CATALINA SALAZAR ARISTIZABAL"]
lista_nombres=formatoNombres(lista_nombres)
#print(lista_nombres)
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_nombres)
#print(lista_emails)
lista_datoses=crearEdad(lista_nombres)
#print(lista_datoses)
lista_especialidades=crearEspecialidades(lista_nombres)
#print(lista_especialidades)
lista_medicos=crearMedicos(lista_nombres,lista_ruts,lista_emails , lista_datoses , lista_especialidades)
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




#Grafico porcentaje de previsiones (isapre,fonasa,sin prevision)
datos_prevision = pd.read_csv('./datos/Pacientes.csv')
pre=datos_prevision["prevision"]
cantidad_prevision= pre.value_counts()

plt.pie(cantidad_prevision.array, labels=cantidad_prevision.index, colors=colors, autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*cantidad_prevision.array.sum()))
plt.title("Previsión de los pacientes")
plt.show()


def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

#funcion para graficar f=pie o bar, datos , con titulo y 0=edad, 1=prevision, 2=especialidad, 3= fecha citada, 4= modalidad, 5= prestacion, 6= confirmada,7= fecha de creacion,8=
def graficarDatos(_datos,_titulo,_f,_titulo_x="x",_titulo_y="y"):
    aux = _datos.tolist()
    aux = merge_sort(aux)
    _datos=aux
    auxOrdenado = list(dict.fromkeys(_datos))
    count = 0
    cantidad = []
    for a in range (len(auxOrdenado)):
        cantidad.append(_datos.count(auxOrdenado[a]))
  

    porcentajes = []
    for a in range (len(cantidad)):
        porcentajes.append((cantidad[a]/(len(_datos)))*100)
        
   
    porAproximados =np.around(porcentajes).tolist()
    porAproximadosFinal = []

    for a in range (len(cantidad)):
        porAproximadosFinal.append(str(porAproximados[a])+"%")

   #datos
    datos=[]
    for a in range (len(cantidad)):
        datos.append(str(auxOrdenado[a]))

    if _f=="pie":
        plt.pie(porAproximados, explode=None, labels=porAproximadosFinal, shadow=True)
        print(datos)
        plt.legend(datos, title= "Codigo de Color", loc=0, bbox_to_anchor=(0.1 , 0.3), shadow=True)
        plt.title("Porcentaje de "+_titulo)
        plt.savefig(f"./graficos/"+_titulo+".png",dpi=300,bbox_inches="tight")

    elif _f=="bar":
        plt.bar(datos, cantidad, align="center")
        plt.title(_titulo)
        plt.ylabel(_titulo_y)
        plt.xlabel(_titulo_x)
        plt.grid(axis="y")
      #  plt.show()
        plt.savefig(f"./graficos/"+_titulo+".png",dpi=300,bbox_inches="tight")
    plt.show()

edad_pacientes = pd.read_csv('./datos/Pacientes.csv')
edad_pacientes=edad_pacientes["edad"].values
graficarDatos(edad_pacientes,"Edades de los Pacientes","bar","Edades", "Pacientes por Edad")

especialidad_medicos = pd.read_csv('./datos/Medicos.csv')
especialidad_medicos=especialidad_medicos["especialidad"].values
graficarDatos(especialidad_medicos,"Especialidades","pie")

datos_modalidad = pd.read_csv("./datos/Citas.csv")
datos_modalidad = datos_modalidad["modalidad"].values
#graficarDatos

datos_prestacion = pd.read_csv("./datos/Citas.csv")
datos_prestacion = datos_prestacion["prestacion"].values
#graficarDatos

datos_prevision = pd.read_csv('./datos/Pacientes.csv')
datos_prevision = datos_prevision["prevision"].values
#graficarDatos

confirmados = pd.read_csv('./datos/Citas.csv')
confirmados = confirmados["confirmada"].values
#graficarDatos

#lista que contiene todos los datos
Lista_datos = [edad_pacientes, especialidad_medicos, datos_modalidad, datos_prestacion, datos_prevision, confirmados]

datos_modalidad = pd.read_csv("./datos/Citas.csv")

ventana_principal=Tk()
ventana_principal.title("Dashboard") 
ventana_principal.resizable(0,0)
ventana_principal.geometry("400x200")
dashboard_btn= Button(ventana_principal, text="Dashboard")
grafico_list_btn=[]

edades_grafico_img = PIL.Image.open('./imagenes/Edades de los Pacientes.png')
edades_grafico_img =edades_grafico_img.resize((200, 100), PIL.Image.ANTIALIAS)
edades_grafico_img = ImageTk.PhotoImage(edades_grafico_img)
edades_grafico_btn=Button(ventana_principal, image =edades_grafico_img)
grafico_list_btn.append(edades_grafico_btn)

for btn in grafico_list_btn:
    btn.pack()
ventana_principal.mainloop()


root = Tk()
label = Label(root,text="Enter a digit that you guessed:").pack()
entry= Entry(root,bd=4)
entry.pack()
button1=Button(root,width=4,height=1,text='ok')
button1.pack()

root.mainloop()
"""
pacientes_csv = pd.read_csv('./datos/Pacientes.csv', index_col=0)
agregar={'nombre completo': [clinica_objeto.getPacientes()[-1].getNombreCompleto()],
         'rut': [clinica_objeto.getPacientes()[-1].getRut()],
         'edad': [clinica_objeto.getPacientes()[-1].getEdad()],
         'email': [clinica_objeto.getPacientes()[-1].getEmail()],
         'numero de telefono': [clinica_objeto.getPacientes()[-1].getNumeroTelefonico()],
         'prevision': [clinica_objeto.getPacientes()[-1].getPrevision()]
        }
agregar=pd.DataFrame(agregar)
agregar.to_csv("agregar.csv")
print(agregar)