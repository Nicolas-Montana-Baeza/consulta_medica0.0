from clinica import Clinica
from tkinter import  Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame, W,StringVar,FLAT
from tkcalendar import *

clinica= Clinica()
clinica.setNombre("Clinica de la Salud")
color1="#788890"
color2="#28388f"
color3="#accdec"
color4="#6d6e72"
     
ventana_principal=Tk()

ventana_principal.title(str(
    clinica.getNombre())) 

ventana_principal.configure(bg=
color2)


#en este frame irán todas las entradas necesarias para una cita

agendar_cita=LabelFrame(
    ventana_principal, text="Agendar Cita", padx=5, pady=5, bg=
color3, relief=FLAT)

agendar_cita.pack(padx=10,pady=10)

#contiene los radio buttons

escojer_especialidades=LabelFrame(
    agendar_cita, text="Escoja la Especialidad", padx=5, pady=5, bg=
color3)

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
    Radiobutton(
        escojer_especialidades,highlightthickness=0, text=texto, variable=
    opcion, value=especialidad, bg=
    color3).pack(anchor=W)

#Además se necesitará propiciar una modalidad

modalidad=StringVar()

modalidad.set("Online")

escojer_modalidad=LabelFrame(
    agendar_cita,text="Modalidad",padx=5, pady=5, bg=
color3)

escojer_modalidad.pack(anchor=W)
Radiobutton(
    escojer_modalidad,highlightthickness=0, text="Online", variable=
modalidad,value="Online", bg=
color3).grid(row=0,column=0)
Radiobutton(
    escojer_modalidad,highlightthickness=0, text="Presencial", variable=
modalidad,value="Presencial", bg=
color3).grid(row=0,column=1)

#Ingreso de datos del paciente

ingresar_paciente=LabelFrame(
    agendar_cita,text="Datos del Paciente", padx=5, pady=5,bg=
color3)

ingresar_paciente.pack(anchor=W)

    #rut se podria agregar que al ingresar el rut si el paciente ya existe los datos se autocompleten

rut_label=Label(
    ingresar_paciente, text="Rut(sin puntos): ", bg=
color3).grid(row=0,column=0)

rut=Entry(
    ingresar_paciente, width=10).grid(row=0,column=1)

    #prevision

prevision_label=Label(
    ingresar_paciente, text="Prevision del Paciente:", bg=
color3).grid(row=1,column=0)

prevision=StringVar()

prevision.set("FONASA")
Radiobutton(
    ingresar_paciente,highlightthickness=0, text="FONASA", variable=
prevision,value="FONASA", bg=
color3).grid(row=2,column=0)
Radiobutton(
    ingresar_paciente,highlightthickness=0, text="ISAPRE", variable=
prevision,value="ISAPRE", bg=
color3).grid(row=2,column=1)
Radiobutton(
    ingresar_paciente,highlightthickness=0, text="Sin Prevision", variable=
prevision,value="Sin Prevision", bg=
color3).grid(row=2,column=2)
    #primer nombre

nombre1_label=Label(
    ingresar_paciente, text="Primer Nombre: ", bg=
color3).grid(row=3,column=0)

nombre1=Entry(
    ingresar_paciente, width=10).grid(row=3,column=1)

    #segundo nombre

nombre2_label=Label(
    ingresar_paciente, text="Segundo Nombre: ", bg=
color3).grid(row=4,column=0)

nombre2=Entry(
    ingresar_paciente, width=10).grid(row=4,column=1)

    #Primer Apellido

apellido1_label=Label(
    ingresar_paciente, text="Primer Apellido: ", bg=
color3).grid(row=5,column=0)

apellido1=Entry(
    ingresar_paciente, width=10).grid(row=5,column=1)

    #Segundo Apellido

apellido2_label=Label(
    ingresar_paciente, text="Segundo Apellido: ", bg=
color3).grid(row=6,column=0)

apellido2=Entry(
    ingresar_paciente, width=10).grid(row=6,column=1)

    #numero contacto

tel_contacto_label=Label(
    ingresar_paciente, text="Número Telefono/Celular: ", bg=
color3).grid(row=7,column=0)

tel_contacto=Entry(
    ingresar_paciente, width=10).grid(row=7,column=1)

    #email

email_label=Label(
    ingresar_paciente, text="Correo Electronico: ", bg=
color3).grid(row=8,column=0)

email=Entry(
    ingresar_paciente, width=10).grid(row=8,column=1)

#en este se mostraran las citas por paciente, o por codigo de cita y debe confirmar, cancelar o reagendar la cita necesaria
#def guardar_cita():

citas_agendadas=LabelFrame(
    ventana_principal, text="Mis Citas", padx=5, pady=5, bg=
color3)

citas_agendadas.pack(anchor=W)

citas_agendadas2=Label(
    citas_agendadas, text="Ingrese su codigo: ", bg=
color3).grid(row=0,column=0)

citas_agendadas3=Entry(
    citas_agendadas, width=30).grid(row=0,column=1)

boton_aceptar=Button(
    citas_agendadas,text="Buscar").grid(row=0,column=2)

boton_agendar_hora=Button(
    citas_agendadas,text="Confirmar").grid(row=1,column=2)

boton_cancelar_hora=Button(
    citas_agendadas,text="Cancelar").grid(row=1,column=3)

boton_editar_hora=Button(
    citas_agendadas,text="Reagendar").grid(row=1,column=4)

#ACA VA LA ELECCION DE FECHA Y HORA PARA LA CITA, DEBERIA CAMBIAR DE ACUERDO A LA DISPONIBILIDAD PERO DPS VEMOS ESO

disponibilidad_citas=LabelFrame(
    agendar_cita, text="Seleccione la fecha para agendar su cita: ", bg=
color3)

calendario = Calendar(
    disponibilidad_citas)

calendario.pack(pady=30)

disponibilidad_citas.pack(anchor=W)
def grabar_fecha():
    
    seleccion.config(text="Su hora será agendada para el día " + 
    calendario.get_date())

boton_confirmar_fecha=Button(
    disponibilidad_citas, text="CONFIRMAR FECHA", command=grabar_fecha).pack()
#
# seleccion_hora = Spinbox(
# disponibilidad_citas, 



ventana= GuiDominio()
ventana.mainloop()