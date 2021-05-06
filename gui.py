import tkinter
from typing import Text
from clinica import Clinica
from tkinter import  Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame, W,StringVar,FLAT,NE,END,N
from tkcalendar import *

clinica= Clinica()
clinica.setNombre("Clinica de la Salud")
#hay que agregar datos a la clinica
color1="#788890"
color2="#28388f"
color3="#accdec"
color4="#6d6e72"
     
ventana_principal=Tk()
ventana_principal.title(str(clinica.getNombre())) 
ventana_principal.configure(bg=color2)
ventana_principal.geometry("1260x656")

#en este frame irán todas las entradas necesarias para una cita

agendar_cita=LabelFrame(ventana_principal, text="Agendar Cita", padx=5, pady=5, bg=color3, relief=FLAT)
agendar_cita.grid(row=0,column=1)

#contiene los radio buttons

escojer_especialidades=LabelFrame(agendar_cita, text="Escoja la Especialidad", padx=5, pady=5, bg=color3)
escojer_especialidades.pack(anchor=W)

especialidades=[
("Medicina General", "Medicina General"),
("Kinesiologia", "Kinesiologia"),
("Pediatria", "Pediatria"),
("Odontologia", "Odontologia")
]

opcion = StringVar()

opcion.set("Medicina General")

for texto, especialidad in especialidades:
    Radiobutton(escojer_especialidades,highlightthickness=0, text=texto, variable=opcion, value=especialidad, bg=color3).pack(anchor=W)

#Además se necesitará propiciar una modalidad

modalidad=StringVar()

modalidad.set("Online")

escojer_modalidad=LabelFrame(agendar_cita,text="Modalidad",padx=5, pady=5, bg=color3)

escojer_modalidad.pack(anchor=W)
Radiobutton(escojer_modalidad,highlightthickness=0, text="Online", variable=modalidad,value="Online", bg=color3).grid(row=0,column=0)
Radiobutton(escojer_modalidad,highlightthickness=0, text="Presencial", variable=modalidad,value="Presencial", bg=color3).grid(row=0,column=1)

#Ingreso de datos del paciente
ingresar_paciente=LabelFrame(agendar_cita,text="Datos del Paciente", padx=5, pady=5,bg=color3)
ingresar_paciente.pack(anchor=W)

    #rut se podria agregar que al ingresar el rut si el paciente ya existe los datos se autocompleten

rut_label=Label(ingresar_paciente, text="Rut(sin puntos): ", bg=color3).grid(row=0,column=0)

rut_entry=Entry(ingresar_paciente, width=10).grid(row=0,column=1)


    #prevision

prevision_label=Label(ingresar_paciente, text="Prevision del Paciente:", bg=color3).grid(row=1,column=0)

prevision_btn=StringVar()

prevision_btn.set("FONASA")
Radiobutton(ingresar_paciente,highlightthickness=0, text="FONASA", variable=prevision_btn,value="FONASA", bg=color3).grid(row=2,column=0)
Radiobutton(ingresar_paciente,highlightthickness=0, text="ISAPRE", variable=prevision_btn,value="ISAPRE", bg=color3).grid(row=2,column=1)
Radiobutton(ingresar_paciente,highlightthickness=0, text="Sin Prevision", variable=prevision_btn,value="Sin Prevision", bg=color3).grid(row=2,column=2)
    #primer nombre

nombre1_label=Label(ingresar_paciente, text="Primer Nombre: ", bg=color3).grid(row=3,column=0)

nombre1=Entry(ingresar_paciente, width=10).grid(row=3,column=1)

    #segundo nombre

nombre2_label=Label(ingresar_paciente, text="Segundo Nombre: ", bg=color3).grid(row=4,column=0)

nombre2=Entry(ingresar_paciente, width=10).grid(row=4,column=1)

    #Primer Apellido

apellido1_label=Label(ingresar_paciente, text="Primer Apellido: ", bg=color3).grid(row=5,column=0)

apellido1=Entry(ingresar_paciente, width=10).grid(row=5,column=1)

    #Segundo Apellido

apellido2_label=Label(ingresar_paciente, text="Segundo Apellido: ", bg=color3).grid(row=6,column=0)

apellido2=Entry(ingresar_paciente, width=10).grid(row=6,column=1)

    #numero contacto

tel_contacto_label=Label(ingresar_paciente, text="Número Telefono/Celular: ", bg=color3).grid(row=7,column=0)

tel_contacto_entry=Entry(ingresar_paciente, width=10).grid(row=7,column=1)

    #email

email_label=Label(ingresar_paciente, text="Correo Electronico: ", bg=color3).grid(row=8,column=0)

email_entry=Entry(ingresar_paciente, width=10).grid(row=8,column=1)

#en este se mostraran las citas por paciente, o por codigo de cita y debe confirmar, cancelar o reagendar la cita necesaria
#def guardar_cita():
citas_agendadas_frame=LabelFrame(ventana_principal, text="Mis Citas", padx=5, pady=5, bg=color3)
citas_agendadas_frame.grid(row=0,column=2,sticky=N)

codigo_frame=LabelFrame(citas_agendadas_frame,text="Buscar cita por codigo", bg=color3)
codigo_frame.pack(anchor=W)

ingresar_codigo_label=Label(codigo_frame, text="Ingrese su codigo: ", bg=color3).grid(row=0,column=0,sticky=W)
ingresar_codigo_entry=Entry(codigo_frame, width=30).grid(row=1,column=0)

buscar_btn=Button(codigo_frame,text="Buscar").grid(row=1,column=2)

#una vez encontrada la cita se muestra en este Frame
gestionar_cita_frame=LabelFrame(citas_agendadas_frame,text="Información de la Cita", bg=color3)
gestionar_cita_frame.pack()

info_cita_txtbox=tkinter.Text(gestionar_cita_frame,width=50,height=20)
info_cita_txtbox.insert(END,"Su cita no fue encontrada...\n Revise su codigo o comuniquese con nuestro equipo")
info_cita_txtbox.grid(row=1,column=0)

agendar_hora_btn=Button(gestionar_cita_frame,text="Confirmar").grid(row=2,column=0)

cancelar_hora_btn=Button(gestionar_cita_frame,text="Cancelar").grid(row=2,column=1)

reagendar_hora_btn=Button(gestionar_cita_frame,text="Reagendar").grid(row=2,column=2)

#ACA VA LA ELECCION DE FECHA Y HORA PARA LA CITA, DEBERIA CAMBIAR DE ACUERDO A LA DISPONIBILIDAD PERO DPS VEMOS ESO

disponibilidad_citas_frame=LabelFrame(agendar_cita, text="Seleccione la fecha para agendar su cita: ", bg=color3)

calendario = Calendar(disponibilidad_citas_frame)

calendario.pack(pady=30)

disponibilidad_citas_frame.pack(anchor=W)

#
# seleccion_hora = Spinbox(
# disponibilidad_citas_frame, 


ventana_principal.mainloop()