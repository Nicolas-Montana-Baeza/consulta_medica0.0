import clinica
from tkinter import  Listbox,S,Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame, W,StringVar,FLAT,NE,END,N,Text
from tkcalendar import Calendar
from random import randint
#Creacion de algunas listas para darle datos a nuestro objeto Clinica
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
#hay que agregar datos a la clinica
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
    
    if type(paciente)==list:
        return
    
    datos_paciente=[paciente.getPrimerNombre(), paciente.getSegundoNombre(),paciente.getPrimerApellido(), paciente.getSegundoApellido(), paciente.getNumeroTelefonico(),paciente.getEmail()]
    
    if paciente.getPrevision=="ISAPRE":
        isapre_btn.select()
    
    elif paciente.getPrevision=="FONASA":
        fonasa_btn.select()
    
    else:
        sin_prevision_btn.select()

    prevision_btn=paciente.getPrevision()
    
    for i in range(len(datos_paciente)):
        lista_entry_datos_paciente[i].delete(0)
        lista_entry_datos_paciente[i].insert(0,datos_paciente[i])
       
def agregarCita():
    return

#def buscar(busqueda):
    
def buscarMedico():
    _busqueda=buscar_doctor_entry.get()
    

ventana_principal=Tk()
ventana_principal.title(str(clinica_objeto.getNombre())) 
ventana_principal.configure(bg=color2)
ventana_principal.geometry("1260x656")

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
buscar_doctor_entry.grid(row=1,column=0)

buscar_btn=Button(buscar_medico_frame,text="Buscar", command=lambda:buscarMedico())
buscar_btn.grid(row=1,column=2)
lista_medicos_listbox=Listbox(buscar_medico_frame,width=30)
#lista_medicos_listbox.grid(rowspan=2, row=2, column=0, sticky=S)

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
fonasa_btn=Radiobutton(ingresar_paciente,highlightthickness=0, text="FONASA", variable=prevision_btn,value="FONASA", bg=color3)
fonasa_btn.grid(row=2,column=0)
isapre_btn=Radiobutton(ingresar_paciente,highlightthickness=0, text="ISAPRE", variable=prevision_btn,value="ISAPRE", bg=color3)
isapre_btn.grid(row=2,column=1)
sin_prevision_btn=Radiobutton(ingresar_paciente,highlightthickness=0, text="Sin Prevision", variable=prevision_btn,value="Sin Prevision", bg=color3)
sin_prevision_btn.grid(row=2,column=2)

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

codigo_frame=LabelFrame(citas_agendadas_frame,text="Buscar cita por codigo", bg=color3)
codigo_frame.pack(anchor=W)

ingresar_codigo_label=Label(codigo_frame, text="Ingrese su codigo: ", bg=color3).grid(row=0,column=0,sticky=W)
ingresar_codigo_entry=Entry(codigo_frame, width=30)
ingresar_codigo_entry.grid(row=1,column=0)

buscar_btn=Button(codigo_frame,text="Buscar").grid(row=1,column=2)

#una vez encontrada la cita se muestra en este Frame
gestionar_cita_frame=LabelFrame(citas_agendadas_frame,text="Información de la Cita", bg=color3)
gestionar_cita_frame.pack()

info_cita_txtbox=Text(gestionar_cita_frame,width=50,height=20)
info_cita_txtbox.insert(END,"Su cita no fue encontrada...\n Revise su codigo o comuniquese con nuestro equipo")
info_cita_txtbox.grid(row=1,column=0)

agendar_hora_btn=Button(gestionar_cita_frame,text="Confirmar")
agendar_hora_btn.grid(row=2,column=0)

cancelar_hora_btn=Button(gestionar_cita_frame,text="Cancelar")
cancelar_hora_btn.grid(row=2,column=1)

reagendar_hora_btn=Button(gestionar_cita_frame,text="Reagendar")
cancelar_hora_btn.grid(row=2,column=2)

#ACA VA LA ELECCION DE FECHA Y HORA PARA LA CITA, DEBERIA CAMBIAR DE ACUERDO A LA DISPONIBILIDAD PERO DPS VEMOS ESO

disponibilidad_citas_frame=LabelFrame(agendar_cita_frame, text="Seleccione la fecha para agendar su cita: ", bg=color3)

calendario = Calendar(disponibilidad_citas_frame)

calendario.pack(pady=30)

disponibilidad_citas_frame.pack(anchor=W)

#
# seleccion_hora = Spinbox(
# disponibilidad_citas_frame, 


ventana_principal.mainloop()