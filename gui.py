from tkinter import X,SW,S,SE,ttk,font,YES,BOTH,NS, Listbox,S,Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame,W,StringVar,FLAT,NE,END,N,Text,ACTIVE,DISABLED,NORMAL,E,Scrollbar,RIGHT,Y,LEFT,Spinbox
from tkinter.constants import BOTTOM, TOP
#from tkcalendar import Calendar
from PIL import Image,ImageTk
import ttkbootstrap
from datosDeRelleno import *
from PIL import Image,ImageTk
from estilo import*


#Creacion de algunas listas para darle datos a nuestro objeto Clinica

lista_entry_datos_paciente=[]

def autocompletarPaciente():
    _busqueda=buscar_rut_entry.get()
    paciente=clinica_objeto.buscarPaciente(_busqueda)

    if len(paciente)==0:
        messagebox.showwarning(message="No se ha podido encontrar el rut ingresado...", title="Error")
    
        for i in range(len(lista_entry_datos_paciente)):
            lista_entry_datos_paciente[i].delete(0,END)
            prevision_btn.set("Sin Prevision")
    
        return
    paciente=paciente[0]
    datos_paciente=[paciente.getRut(), paciente.getPrimerNombre(), paciente.getSegundoNombre(),paciente.getPrimerApellido(), paciente.getSegundoApellido(), paciente.getNumeroTelefonico(),paciente.getEmail()]

    prevision_btn.set(paciente.getPrevision())
    
    for i in range(len(datos_paciente)):
        lista_entry_datos_paciente[i].delete(0,END)
        lista_entry_datos_paciente[i].insert(0,datos_paciente[i])
       
def agregarCita():
    return
    
def buscarMedico():
    _busqueda=buscar_doctor_entry.get()
    return clinica_objeto.buscarMedico(_busqueda)

def actualizarListbox(datos):
    lista_medicos_listbox.delete(0,END)
    for medico in datos:
        lista_medicos_listbox.insert(END, medico)
    
    return

def seleccionarMedico(evento):
    medico_seleccionado_label["text"]=lista_medicos_listbox.get(ACTIVE)

    return

def buscar(evento):
    escrito=buscar_doctor_entry.get()
    
    if escrito == "":
        datos=clinica_objeto.getMedicos()
    else:
        datos=clinica_objeto.buscarMedico(escrito)
    
    actualizarListbox(datos)

def agregarDatosPaciente():
    paciente_temporal=clinica.Paciente(nombre1_entry.get(), nombre2_entry.get(), apellido1_entry.get(), apellido2_entry.get(), rut_entry.get(), edad_entry.get(),
    email_entry.get(), tel_contacto_entry.get())
    clinica_objeto.agregarPaciente(paciente_temporal)
    return

def cancelarDatosPaciente():
    
    for i in range(len(lista_entry_datos_paciente)):
        lista_entry_datos_paciente[i].delete(0,END)
        prevision_btn.set("Sin Prevision")

def agendarCita():

    return
    
ventana_principal=Tk()
ventana_principal.title(str(clinica_objeto.getNombre())) 
ventana_principal.resizable(0,0)
s=ttkbootstrap.Style()
s.theme_use("darkly")


"""
image = Image.open('imagenes/fondoPrincipal.png')

photo = ImageTk.PhotoImage(image)
fondo = Label(ventana_principal, image = photo)
fondo.place(x=0,y=0,relheight=1,relwidth=1)
"""
#FUENTES
titulo_font = font.Font(family="Arial",weight="bold",size=35)
subtitulo_font = font.Font(family="Arial Nova", weight="bold",size= 20)
subtitulo2_font = font.Font(family="Arial Narrow", weight="bold",size=15)
subtitulo3_font = font.Font (family= "Arial Narrow", size= 15)
subtitulo4_font = font.Font (family= "Arial Narrow", size= 15)
subtitulo5_font = font.Font (family= "Arial Narrow", size= 12)


#en este frame irán todas las entradas necesarias para una cita
agendar_cita_frame=LabelFrame(ventana_principal,relief=FLAT, bg=Charade,bd=0)
agendar_cita_frame.pack(side=LEFT,fill=Y, expand=True, padx=40, pady=40)
agendar_cita_label=Label(agendar_cita_frame, text="Agendar Cita",font=titulo_font,bg=CuriousBlue, highlightthickness=0)
agendar_cita_label.pack(fill=X)

"""
#contiene los radio buttons
escoger_especialidades=LabelFrame(agendar_cita_frame, text="Escoja la Especialidad", padx=5, pady=5")
escoger_especialidades.pack(anchor=W)

especialidades=["Medicina General","Kinesiologia","Pediatria", "Odontologia"]
opcion=StringVar()
opcion.set(especialidades[0])

kine_btn=Radiobutton(escoger_especialidades,highlightthickness=0, text=especialidades[1], variable=opcion, value=especialidades[1]")
med_gnrl_btn=Radiobutton(escoger_especialidades,highlightthickness=0, text=especialidades[0], variable=opcion, value=especialidades[0]",)
pedia_btn=Radiobutton(escoger_especialidades,highlightthickness=0, text=especialidades[2], variable=opcion, value=especialidades[2]")
odont_btn=Radiobutton(escoger_especialidades,highlightthickness=0, text=especialidades[3], variable=opcion, value=especialidades[3]")
kine_btn.pack(anchor=W)
med_gnrl_btn.pack(anchor=W)
pedia_btn.pack(anchor=W)
odont_btn.pack(anchor=W)"""

buscar_medico_frame=LabelFrame(agendar_cita_frame,text="Buscar Medico",width=30, bg=Charade, font=subtitulo_font, labelanchor=N)
buscar_medico_frame.pack(fill=BOTH, expand=True, padx=30, pady=10)
buscar_doctor_label=Label(buscar_medico_frame, text="Ingrese su Busqueda:", bg=Charade, font=subtitulo2_font)
buscar_doctor_label.grid(row=0,column=0,sticky=W)
buscar_doctor_entry=Entry(buscar_medico_frame, width=30, highlightthickness=0,relief=FLAT)
buscar_doctor_entry.grid(row=1,column=0, sticky=W)


framelistbox=LabelFrame(buscar_medico_frame, relief=FLAT)
framelistbox.grid(row=2,column=0)
lista_medicos_listbox=Listbox(framelistbox,width=45,height=4)
lista_medicos_listbox.pack(side=LEFT)
medico_seleccionado_label=Label(buscar_medico_frame, bg=Charade, font=subtitulo5_font)
buscar_doctor_label=Label(buscar_medico_frame, text="Medico escogido:", bg=Charade, font=subtitulo2_font)
buscar_doctor_label.grid(row=3,column=0,sticky=W)
medico_seleccionado_label.grid(row=4,column=0,sticky=W)
scrollbar = Scrollbar(framelistbox)
scrollbar.pack(side=RIGHT,fill=Y)
lista_medicos_listbox.config(yscrollcommand=scrollbar.set)
 
scrollbar.config(command=lista_medicos_listbox.yview)

#Ingreso de datos del paciente

ingresar_paciente=LabelFrame(agendar_cita_frame,text="Datos del Paciente", bg=Charade, font=subtitulo_font, labelanchor=N)
ingresar_paciente.pack(fill=BOTH, expand=True, padx=30, pady=10)

#autocompletar con rut

buscar_rut_ic = Image.open('./imagenes/buscapaciente.png')
buscar_rut_ic = buscar_rut_ic.resize((30, 30), Image.ANTIALIAS)
buscar_rut_ic = ImageTk.PhotoImage(buscar_rut_ic)
buscar_rut_label=Label(ingresar_paciente, text="Rut(sin puntos): ")
buscar_rut_label.grid(row=0,column=0)
buscar_rut_entry=Entry(ingresar_paciente, width=10)
buscar_rut_entry.grid(row=0,column=1,sticky=W)
buscar_rut_btn=Button(ingresar_paciente, text="Buscar" ,command=lambda:autocompletarPaciente(),  image=buscar_rut_ic)
buscar_rut_btn.grid(row=0,column=2)
rut_autocompletar_label=Label(ingresar_paciente, text="Buscar paciente por Rut: ", bg=Charade, font=subtitulo4_font)
rut_autocompletar_label.grid(row=0,column=0)


    #prevision

prevision_label=Label(ingresar_paciente, text="Prevision del Paciente:", bg=Charade, font=subtitulo4_font)
prevision_label.grid(row=1,column=0)
prevision_btn=StringVar()
prevision_btn.set("Sin Prevision")
opciones_prevision_frame=LabelFrame(ingresar_paciente, bg=Charade, relief=FLAT, bd=0)
opciones_prevision_frame.grid(columnspan=3)
sin_prevision_btn=Radiobutton(opciones_prevision_frame,highlightthickness=0, text="Sin Prevision", variable=prevision_btn,value="Sin Prevision", bg=Charade, font=subtitulo5_font)
sin_prevision_btn.pack(side=LEFT)
isapre_btn=Radiobutton(opciones_prevision_frame,highlightthickness=0,bg=Charade, text="Isapre", variable=prevision_btn,value="ISAPRE",  font=subtitulo5_font)
isapre_btn.pack(side=LEFT)
fonasa_btn=Radiobutton(opciones_prevision_frame,highlightthickness=0, text="Fonasa", variable=prevision_btn,value="FONASA", bg=Charade, font=subtitulo5_font)
fonasa_btn.pack(side=LEFT)

    #primer nombre
rut_label=Label(ingresar_paciente, text="Rut (sin puntos):",bg=Charade, font=subtitulo4_font)
rut_label.grid(row=3,column=0)
rut_entry=Entry(ingresar_paciente, width=10)
rut_entry.grid(row=3,column=1)
lista_entry_datos_paciente.append(rut_entry)

nombre1_label=Label(ingresar_paciente, text="Primer Nombre:",bg=Charade, font=subtitulo4_font)
nombre1_label.grid(row=4,column=0)
nombre1_entry=Entry(ingresar_paciente, width=10)
nombre1_entry.grid(row=4,column=1)
lista_entry_datos_paciente.append(nombre1_entry)
    #segundo nombre

nombre2_label=Label(ingresar_paciente, text="Segundo Nombre:", bg=Charade, font=subtitulo4_font)
nombre2_label.grid(row=5,column=0)
nombre2_entry=Entry(ingresar_paciente, width=10)
nombre2_entry.grid(row=5,column=1)
lista_entry_datos_paciente.append(nombre2_entry)
    #Primer Apellido

apellido1_label=Label(ingresar_paciente, text="Primer Apellido:", bg=Charade, font=subtitulo4_font)
apellido1_label.grid(row=6,column=0)
apellido1_entry=Entry(ingresar_paciente, width=10)
apellido1_entry.grid(row=6,column=1)
lista_entry_datos_paciente.append(apellido1_entry)
    #Segundo Apellido

apellido2_label=Label(ingresar_paciente, text="Segundo Apellido:", bg=Charade, font=subtitulo4_font)
apellido2_label.grid(row=7,column=0)
apellido2_entry=Entry(ingresar_paciente, width=10)
apellido2_entry.grid(row=7,column=1)
lista_entry_datos_paciente.append(apellido2_entry)
    
    #numero contacto
tel_contacto_label=Label(ingresar_paciente, text="Número Telefono/Celular:", bg=Charade, font=subtitulo4_font)
tel_contacto_label.grid(row=8,column=0)
tel_contacto_entry=Entry(ingresar_paciente, width=10)
tel_contacto_entry.grid(row=8,column=1)
lista_entry_datos_paciente.append(tel_contacto_entry)

    #email
email_label=Label(ingresar_paciente, text="Correo Electronico:", bg=Charade, font=subtitulo4_font)
email_label.grid(row=9,column=0)
email_entry=Entry(ingresar_paciente, width=10)
email_entry.grid(row=9,column=1)
lista_entry_datos_paciente.append(email_entry)
    #edad
edad_label=Label(ingresar_paciente,text="Edad:",bg=Charade, font=subtitulo4_font)
edad_label.grid(row=10,column=0)
edad_entry=Entry

#Frame de botones

botones_paciente_frame=LabelFrame(ingresar_paciente, bd=0, relief=FLAT,bg=Charade)
botones_paciente_frame.grid(columnspan=3,row=10,column=0)
confirmar_paciente_ic = Image.open('./imagenes/confirmar_paciente.png')
confirmar_paciente_ic = confirmar_paciente_ic.resize((50, 50), Image.ANTIALIAS)
confirmar_paciente_ic = ImageTk.PhotoImage(confirmar_paciente_ic)
confirmar_paciente_btn=Button(botones_paciente_frame,text="Confirmar", image = confirmar_paciente_ic, command=lambda:agregarDatosPaciente())
confirmar_paciente_btn.pack(side=LEFT,padx=30)

cancelar_paciente_ic = Image.open('./imagenes/cancelar_paciente.png')
cancelar_paciente_ic = cancelar_paciente_ic.resize((50, 50), Image.ANTIALIAS)
cancelar_paciente_ic = ImageTk.PhotoImage(cancelar_paciente_ic)
cancelar_paciente_btn=Button(botones_paciente_frame,text="Cancelar", image = cancelar_paciente_ic, command=lambda:cancelarDatosPaciente())
cancelar_paciente_btn.pack(side=RIGHT,padx=30)

#en este se mostraran las citas por paciente, o por codigo de cita y debe confirmar, cancelar o reagendar la cita necesaria

citas_agendadas_frame=LabelFrame(ventana_principal,relief=FLAT, bg=Charade,bd=0)
citas_agendadas_frame.pack(side=LEFT,fill=X, expand=True, padx=40, pady=40, anchor=N)
citas_agendadas_label=Label(citas_agendadas_frame,bg=CuriousBlue, text="Mis Citas",font=titulo_font, highlightthickness=0)
citas_agendadas_label.pack(fill=X)



#ingresa el codigo
gestionar_cita_frame=LabelFrame(citas_agendadas_frame,text="Información de la Cita",bg=Charade,font=subtitulo_font, labelanchor=N)
gestionar_cita_frame.pack(fill=Y, expand=True, padx=30, pady=10)
ingresar_codigo_label=Label(gestionar_cita_frame, text="Ingrese el código de su cita",bg=Charade,font=subtitulo2_font)
ingresar_codigo_label.pack()
ingresar_codigo_entry=Entry(gestionar_cita_frame, width=30)
ingresar_codigo_entry.pack()

#Boton buscar
buscar_cita_ic = Image.open('./imagenes/buscacita.png')
buscar_cita_ic = buscar_cita_ic.resize((50, 50), Image.ANTIALIAS)
buscar_cita_ic = ImageTk.PhotoImage(buscar_cita_ic)
buscar_btn=Button(gestionar_cita_frame,text="Buscar", image=buscar_cita_ic)
buscar_btn.pack(  pady=10)

#muestra la informacion encontrada de la cita
info_cita_txtbox=Text(gestionar_cita_frame,width=50,height=20)
info_cita_txtbox.insert(END,"Su cita no fue encontrada...\n Revise su codigo o comuniquese con nuestro equipo")
info_cita_txtbox.pack(padx=10)

agendar_hora_ic = Image.open('./imagenes/confirmar.png')
agendar_hora_ic = agendar_hora_ic.resize((50, 50), Image.ANTIALIAS)
agendar_hora_ic = ImageTk.PhotoImage(agendar_hora_ic)
agendar_hora_btn=Button(gestionar_cita_frame,text="Confirmar", image = agendar_hora_ic)
agendar_hora_btn.pack(side=LEFT,padx=15,pady=10)

cancelar_hora_ic = Image.open('./imagenes/cancelar.png')
cancelar_hora_ic = cancelar_hora_ic.resize((50, 50), Image.ANTIALIAS)
cancelar_hora_ic = ImageTk.PhotoImage(cancelar_hora_ic)
cancelar_hora_btn=Button(gestionar_cita_frame,text="Cancelar", image = cancelar_hora_ic)
cancelar_hora_btn.pack(side=RIGHT,padx=15,pady=10)

#boton reagendar
reagendar_hora_ic = Image.open('./imagenes/reagendar.png')
reagendar_hora_ic = reagendar_hora_ic.resize((50, 50), Image.ANTIALIAS)
reagendar_hora_ic = ImageTk.PhotoImage(reagendar_hora_ic)
reagendar_hora_btn=Button(gestionar_cita_frame,text="Reagendar", image = reagendar_hora_ic)
reagendar_hora_btn.pack(side=BOTTOM,padx=15,pady=10)

#ELECCION DE FECHA Y HORA PARA LA CITA, DEBERIA CAMBIAR DE ACUERDO A LA DISPONIBILIDAD PERO DPS VEMOS ESO


modalidad=StringVar()

escojer_fecha_frame=LabelFrame(ventana_principal, text="Datos Cita",bg=Charade,font=subtitulo_font, labelanchor=N)
escojer_modalidad=LabelFrame(escojer_fecha_frame,text="Modalidad",padx=5, pady=5,bg=Charade,font=subtitulo2_font, labelanchor=N)
escojer_modalidad.pack(fill=BOTH, expand=True, padx=30, pady=10)
online_btn=Radiobutton(escojer_modalidad,highlightthickness=0, text="Online", variable=modalidad,value="Online", bg=Charade,font=subtitulo5_font)
online_btn.grid(row=0,column=0)
presencial_btn=Radiobutton(escojer_modalidad,highlightthickness=0, text="Presencial", variable=modalidad,value="Presencial", bg=Charade, font=subtitulo5_font)
presencial_btn.grid(row=0,column=1)

disponibilidad_citas_frame=LabelFrame(escojer_fecha_frame, text="Seleccionar fecha:", bg=Charade, font=subtitulo2_font, labelanchor=N)
disponibilidad_citas_frame.pack(fill=BOTH, expand=True, padx=30, pady=10)
seleccion_Dia=Spinbox(disponibilidad_citas_frame,width=10 ,values=("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
seleccion_Dia.grid(row=1, column=1)
dia_label=Label(disponibilidad_citas_frame,text="Día",bg=Charade, font=subtitulo4_font)
dia_label.grid(row=1,column=0)
seleccion_Mes=Spinbox(disponibilidad_citas_frame,width=10 ,values=("01","01","03","04","05","06","07","08","09","10","11","12"))
seleccion_Mes.grid(row=2,column=1)
dia_label=Label(disponibilidad_citas_frame,text="Mes",bg=Charade, font=subtitulo4_font)
dia_label.grid(row=2,column=0)
seleccion_Año=Spinbox(disponibilidad_citas_frame,width=10 ,values=("2021","2022","2023","2024","2025","2026","2027","2028","2029","2030","2031"))
seleccion_Año.grid(row=3,column=1)
dia_label=Label(disponibilidad_citas_frame,text="Año",bg=Charade, font=subtitulo4_font)
dia_label.grid(row=3,column=0)

hora = StringVar()
seleccion_hora=Spinbox(disponibilidad_citas_frame,width=10 ,values=("8","9","10","11","12","13","14","15","16","17","18","19","20","21","22"))
seleccion_minutos=Spinbox(disponibilidad_citas_frame,width=10 ,values=("00","30"))
seleccion_hora.grid(row=4,column=1)
seleccion_minutos.grid(row=5,column=1)
dia_label=Label(disponibilidad_citas_frame,text="Hora",bg=Charade, font=subtitulo4_font)
dia_label.grid(row=4,column=0)
dia_label=Label(disponibilidad_citas_frame,text="Minutos",bg=Charade, font=subtitulo4_font)
dia_label.grid(row=5,column=0)

reservar_hora_ic = Image.open('./imagenes/reservarhora.png')
reservar_hora_ic = reservar_hora_ic.resize((50, 50), Image.ANTIALIAS)
reservar_hora_ic = ImageTk.PhotoImage(reservar_hora_ic)

boton_hora=Button(disponibilidad_citas_frame,text="Reservar Hora",command=lambda:agendarCita, image = reservar_hora_ic)
boton_hora.grid(row=6,column=0, columnspan=2)
escojer_fecha_frame.pack()

actualizarListbox(clinica_objeto.getMedicos())
lista_medicos_listbox.bind("<<ListboxSelect>>", seleccionarMedico)
buscar_doctor_entry.bind("<KeyRelease>", buscar)
ventana_principal.mainloop()