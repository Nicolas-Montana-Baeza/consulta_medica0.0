from tkinter import YES,BOTH,NS, Listbox,S,Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame,W,StringVar,FLAT,NE,END,N,Text,ACTIVE,DISABLED,NORMAL,E,Scrollbar,RIGHT,Y,LEFT
from tkcalendar import Calendar
from PIL import Image, ImageTk

from datosDeRelleno import *
from estilo import*

#Creacion de algunas listas para darle datos a nuestro objeto Clinica
cita_aux=clinica.Cita()
lista_entry_datos_paciente=[]


def disableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ('Frame','Labelframe'):
            child.configure(state='disable')
        else:
            disableChildren(child)

def enableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        print (wtype)
        if wtype not in ('Frame','Labelframe'):
            child.configure(state='normal')
        else:
            enableChildren(child)

#def mostrar_listbox():
 #   print(ventana_principal.focus_get())
    #if ventana_principal.focus_get()=

def autocompletarPaciente():
    _busqueda=rut_entry.get()
    paciente=clinica_objeto.buscarPaciente(_busqueda)

    if len(paciente)==0:
        messagebox.showwarning(message="No se ha podido encontrar el rut ingresado...", title="Error")
    
        for i in range(len(lista_entry_datos_paciente)):
            lista_entry_datos_paciente[i].delete(0,END)
            prevision_btn.set("Sin Prevision")
    
        return
    paciente=paciente[0]
    datos_paciente=[paciente.getPrimerNombre(), paciente.getSegundoNombre(),paciente.getPrimerApellido(), paciente.getSegundoApellido(), paciente.getNumeroTelefonico(),paciente.getEmail()]

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
    medico_seleccionado_entry.config(state=NORMAL) 
    medico_seleccionado_entry.delete(0,END)
    medico_seleccionado_entry.insert(0,lista_medicos_listbox.get(ACTIVE))
    medico_seleccionado_entry.config(state=DISABLED)  

    return

def buscar(evento):
    escrito=buscar_doctor_entry.get()
    
    if escrito == "":
        datos=clinica_objeto.getMedicos()
    else:
        datos=clinica_objeto.buscarMedico(escrito)
    
    actualizarListbox(datos)

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

ventana_principal=Tk()
ventana_principal.title(str(clinica_objeto.getNombre())) 
ventana_principal.configure(bg=color2)
ventana_principal.geometry("1260x656")

image = Image.open('imagenes/fondoPrincipal.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = Label(ventana_principal, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

#en este frame irán todas las entradas necesarias para una cita

agendar_cita_frame=LabelFrame(ventana_principal, text="Agendar Cita", padx=5, pady=5, bg=color3, relief=FLAT)
agendar_cita_frame.grid(row=0,column=1)


"""
#contiene los radio buttons
escojer_especialidades=LabelFrame(agendar_cita_frame, text="Escoja la Especialidad", padx=5, pady=5, bg=color3)
escojer_especialidades.pack(anchor=W)

especialidades=["Medicina General","Kinesiologia","Pediatria", "Odontologia"]
opcion=StringVar()
opcion.set(especialidades[0])

kine_btn=Radiobutton(escojer_especialidades,highlightthickness=0, text=especialidades[1], variable=opcion, value=especialidades[1], bg=color3)
med_gnrl_btn=Radiobutton(escojer_especialidades,highlightthickness=0, text=especialidades[0], variable=opcion, value=especialidades[0], bg=color3,)
pedia_btn=Radiobutton(escojer_especialidades,highlightthickness=0, text=especialidades[2], variable=opcion, value=especialidades[2], bg=color3)
odont_btn=Radiobutton(escojer_especialidades,highlightthickness=0, text=especialidades[3], variable=opcion, value=especialidades[3], bg=color3)
kine_btn.pack(anchor=W)
med_gnrl_btn.pack(anchor=W)
pedia_btn.pack(anchor=W)
odont_btn.pack(anchor=W)"""

buscar_medico_frame=LabelFrame(agendar_cita_frame,text="Buscar Medico", bg=color3)
buscar_medico_frame.pack(anchor=W)
buscar_doctor_label=Label(buscar_medico_frame, text="Ingrese su Busqueda:", bg=color3).grid(row=0,column=0,sticky=W)
buscar_doctor_entry=Entry(buscar_medico_frame, width=30)
buscar_doctor_entry.grid(row=1,column=0, sticky=W)

buscar_medico_btn=Button(buscar_medico_frame,text="Buscar", command=lambda:buscarMedico())
buscar_medico_btn.grid(row=1,column=0,sticky=E)
framelistbox=LabelFrame(buscar_medico_frame, relief=FLAT, bg=color3)
framelistbox.grid(row=2,column=0)
lista_medicos_listbox=Listbox(framelistbox,width=45,height=4)
lista_medicos_listbox.pack(side=LEFT)
medico_seleccionado_entry=Entry(buscar_medico_frame,width=45, state=DISABLED,disabledbackground="white",disabledforeground="black")
buscar_doctor_label=Label(buscar_medico_frame, text="Medico escogido: ", bg=color3).grid(row=3,column=0,sticky=W)
medico_seleccionado_entry.grid(row=4,column=0,sticky=W)
scrollbar = Scrollbar(framelistbox)
scrollbar.pack(side=RIGHT,fill=Y)
lista_medicos_listbox.config(yscrollcommand=scrollbar.set)
 
scrollbar.config(command=lista_medicos_listbox.yview)

#Además se necesitará propiciar una modalidad

modalidad=StringVar()



escojer_modalidad=LabelFrame(agendar_cita_frame,text="Modalidad",padx=5, pady=5, bg=color3)

escojer_modalidad.pack(anchor=W)
online_btn=Radiobutton(escojer_modalidad,highlightthickness=0, text="Online", variable=modalidad,value="Online", bg=color3)
online_btn.grid(row=0,column=0)
presencial_btn=Radiobutton(escojer_modalidad,highlightthickness=0, text="Presencial", variable=modalidad,value="Presencial", bg=color3)
presencial_btn.grid(row=0,column=1)

#Ingreso de datos del paciente

ingresar_paciente=LabelFrame(agendar_cita_frame,text="Datos del Paciente", padx=5, pady=5,bg=color3)
ingresar_paciente.pack(anchor=W)

    #rut se podria agregar que al ingresar el rut si el paciente ya existe los datos se autocompleten

rut_label=Label(ingresar_paciente, text="Rut(sin puntos): ", bg=color3).grid(row=0,column=0)
rut_entry=Entry(ingresar_paciente, width=10)
rut_entry.grid(row=0,column=1)
buscar_rut_btn=Button(ingresar_paciente, text="Autocompletar" ,command=lambda:autocompletarPaciente())
buscar_rut_btn.grid(row=0,column=2)
rut_autocompletar_label=Label(ingresar_paciente, text="Rut(sin puntos): ", bg=color3)
rut_autocompletar_label.grid(row=0,column=0)


    #prevision

prevision_label=Label(ingresar_paciente, text="Prevision del Paciente:", bg=color3).grid(row=1,column=0)
prevision_btn=StringVar()
prevision_btn.set("Sin Prevision")
sin_prevision_btn=Radiobutton(ingresar_paciente,highlightthickness=0, text="Sin Prevision", variable=prevision_btn,value="Sin Prevision", bg=color3)
sin_prevision_btn.grid(row=2,column=0)
isapre_btn=Radiobutton(ingresar_paciente,highlightthickness=0, text="ISAPRE", variable=prevision_btn,value="ISAPRE", bg=color3)
isapre_btn.grid(row=2,column=1)
fonasa_btn=Radiobutton(ingresar_paciente,highlightthickness=0, text="FONASA", variable=prevision_btn,value="FONASA", bg=color3)
fonasa_btn.grid(row=2,column=2)



    #primer nombre

nombre1_label=Label(ingresar_paciente, text="Primer Nombre: ", bg=color3).grid(row=3,column=0)
nombre1_entry=Entry(ingresar_paciente, width=10)
nombre1_entry.grid(row=3,column=1)
lista_entry_datos_paciente.append(nombre1_entry)
    #segundo nombre

nombre2_label=Label(ingresar_paciente, text="Segundo Nombre: ", bg=color3).grid(row=4,column=0)
nombre2_entry=Entry(ingresar_paciente, width=10)
nombre2_entry.grid(row=4,column=1)
lista_entry_datos_paciente.append(nombre2_entry)
    #Primer Apellido

apellido1_label=Label(ingresar_paciente, text="Primer Apellido: ", bg=color3).grid(row=5,column=0)
apellido1_entry=Entry(ingresar_paciente, width=10)
apellido1_entry.grid(row=5,column=1)
lista_entry_datos_paciente.append(apellido1_entry)
    #Segundo Apellido

apellido2_label=Label(ingresar_paciente, text="Segundo Apellido: ", bg=color3).grid(row=6,column=0)
apellido2_entry=Entry(ingresar_paciente, width=10)
apellido2_entry.grid(row=6,column=1)
lista_entry_datos_paciente.append(apellido2_entry)
    #numero contacto

tel_contacto_label=Label(ingresar_paciente, text="Número Telefono/Celular: ", bg=color3).grid(row=7,column=0)
tel_contacto_entry=Entry(ingresar_paciente, width=10)
tel_contacto_entry.grid(row=7,column=1)
lista_entry_datos_paciente.append(tel_contacto_entry)
    #email

email_label=Label(ingresar_paciente, text="Correo Electronico: ", bg=color3).grid(row=8,column=0)
email_entry=Entry(ingresar_paciente, width=10)
email_entry.grid(row=8,column=1)
lista_entry_datos_paciente.append(email_entry)


#en este se mostraran las citas por paciente, o por codigo de cita y debe confirmar, cancelar o reagendar la cita necesaria

citas_agendadas_frame=LabelFrame(ventana_principal, text="Mis Citas", padx=5, pady=5, bg=color3)
citas_agendadas_frame.grid(row=0,column=2,sticky=N)

ingresar_codigo_label=Label(citas_agendadas_frame, text="Ingrese su codigo: ", bg=color3).grid(row=0,column=0,sticky=W)
ingresar_codigo_entry=Entry(citas_agendadas_frame, width=30)
ingresar_codigo_entry.grid(row=1,column=0,sticky=W)

buscar_btn=Button(citas_agendadas_frame,text="Buscar").grid(row=1,column=0,sticky=E)

#una vez encontrada la cita se muestra en este Frame

gestionar_cita_frame=LabelFrame(citas_agendadas_frame,text="Información de la Cita", bg=color3)
gestionar_cita_frame.grid(row=2,column=0)
info_cita_txtbox=Text(gestionar_cita_frame,width=50,height=20)
info_cita_txtbox.insert(END,"Su cita no fue encontrada...\n Revise su codigo o comuniquese con nuestro equipo")
info_cita_txtbox.grid(row=1,column=0)

agendar_hora_btn=Button(gestionar_cita_frame,text="Confirmar")
agendar_hora_btn.grid(row=2,column=0)

cancelar_hora_btn=Button(gestionar_cita_frame,text="Cancelar")
cancelar_hora_btn.grid(row=2,column=0,sticky=E)

reagendar_hora_btn=Button(gestionar_cita_frame,text="Reagendar")
reagendar_hora_btn.grid(row=2,column=0,sticky=W)

#ACA VA LA ELECCION DE FECHA Y HORA PARA LA CITA, DEBERIA CAMBIAR DE ACUERDO A LA DISPONIBILIDAD PERO DPS VEMOS ESO

disponibilidad_citas_frame=LabelFrame(agendar_cita_frame, text="Seleccione la fecha para agendar su cita: ", bg=color3)

calendario = Calendar(disponibilidad_citas_frame)

calendario.pack(pady=30)

disponibilidad_citas_frame.pack(anchor=W)

#
# seleccion_hora = Spinbox(
# disponibilidad_citas_frame, 

actualizarListbox(clinica_objeto.getMedicos())
lista_medicos_listbox.bind("<<ListboxSelect>>", seleccionarMedico)
buscar_doctor_entry.bind("<KeyRelease>", buscar)
ventana_principal.mainloop()