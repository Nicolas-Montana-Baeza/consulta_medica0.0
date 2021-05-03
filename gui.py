from clinica import Clinica
from tkinter import  Tk,Radiobutton,Label,Button,messagebox,Entry,LabelFrame, W,StringVar,FLAT

class GuiDominio(Tk):

    def __init__(self):
        super(GuiDominio, self).__init__()
        self.ventana_principal=Tk()
        self.clinica= Clinica()
        self.clinica.setNombre("Clinica de la Salud")
        self.color1="#788890"
        self.color2="#28388f"
        self.color3="#accdec"
        self.color4="#6d6e72"
        self.ventana_principal.title(str(self.clinica.getNombre())) 
        self.ventana_principal.configure(bg=self.color2)

        #en este frame irán todas las entradas necesarias para una cita
        self.agendar_cita=LabelFrame(self.ventana_principal, text="Agendar Cita", padx=5, pady=5, bg=self.color3, relief=FLAT)
        self.agendar_cita.pack(padx=10,pady=10)

        #contiene los radio buttons
        self.escojer_especialidades=LabelFrame(self.agendar_cita, text="Escoja la Especialidad", padx=5, pady=5, bg=self.color3)
        self.escojer_especialidades.pack(anchor=W)
        self.especialidades=[
        ("Medicina General", "Medicina General"),
        ("Kinesiologia", "Kinesiologia"),
        ("Pediatria", "Pediatria"),
        ("Odontologia", "Odontologia")
        ]
        self.opcion = StringVar()
        self.opcion.set("Medicina General")

        for texto, especialidad in self.especialidades:
            Radiobutton(self.escojer_especialidades,highlightthickness=0, text=texto, variable=self.opcion, value=especialidad, bg=self.color3).pack(anchor=W)

        #Además se necesitará propiciar una modalidad
        self.modalidad=StringVar()
        self.modalidad.set("Online")
        self.escojer_modalidad=LabelFrame(self.agendar_cita,text="Modalidad",padx=5, pady=5, bg=self.color3)
        self.escojer_modalidad.pack(anchor=W)
        Radiobutton(self.escojer_modalidad,highlightthickness=0, text="Online", variable=self.modalidad,value="Online", bg=self.color3).grid(row=0,column=0)
        Radiobutton(self.escojer_modalidad,highlightthickness=0, text="Presencial", variable=self.modalidad,value="Presencial", bg=self.color3).grid(row=0,column=1)

        #Ingreso de datos del paciente
        self.ingresar_paciente=LabelFrame(self.agendar_cita,text="Datos del Paciente", padx=5, pady=5,bg=self.color3)
        self.ingresar_paciente.pack(anchor=W)

            #rut se podria agregar que al ingresar el rut si el paciente ya existe los datos se autocompleten
        self.rut_label=Label(self.ingresar_paciente, text="Rut(sin puntos): ", bg=self.color3).grid(row=0,column=0)
        self.rut=Entry(self.ingresar_paciente, width=10).grid(row=0,column=1)

            #prevision
        self.prevision_label=Label(self.ingresar_paciente, text="Prevision del Paciente:", bg=self.color3).grid(row=1,column=0)
        self.prevision=StringVar()
        self.prevision.set("FONASA")
        Radiobutton(self.ingresar_paciente,highlightthickness=0, text="FONASA", variable=self.prevision,value="FONASA", bg=self.color3).grid(row=2,column=0)
        Radiobutton(self.ingresar_paciente,highlightthickness=0, text="ISAPRE", variable=self.prevision,value="ISAPRE", bg=self.color3).grid(row=2,column=1)
        Radiobutton(self.ingresar_paciente,highlightthickness=0, text="Sin Prevision", variable=self.prevision,value="Sin Prevision", bg=self.color3).grid(row=2,column=2)
            #primer nombre
        self.nombre1_label=Label(self.ingresar_paciente, text="Primer Nombre: ", bg=self.color3).grid(row=3,column=0)
        self.nombre1=Entry(self.ingresar_paciente, width=10).grid(row=3,column=1)

            #segundo nombre
        self.nombre2_label=Label(self.ingresar_paciente, text="Segundo Nombre: ", bg=self.color3).grid(row=4,column=0)
        self.nombre2=Entry(self.ingresar_paciente, width=10).grid(row=4,column=1)

            #Primer Apellido
        self.apellido1_label=Label(self.ingresar_paciente, text="Primer Apellido: ", bg=self.color3).grid(row=5,column=0)
        apellido1=Entry(self.ingresar_paciente, width=10).grid(row=5,column=1)

            #Segundo Apellido
        self.apellido2_label=Label(self.ingresar_paciente, text="Segundo Apellido: ", bg=self.color3).grid(row=6,column=0)
        self.apellido2=Entry(self.ingresar_paciente, width=10).grid(row=6,column=1)

            #numero contacto
        self.tel_contacto_label=Label(self.ingresar_paciente, text="Número Telefono/Celular: ", bg=self.color3).grid(row=7,column=0)
        self.tel_contacto=Entry(self.ingresar_paciente, width=10).grid(row=7,column=1)

            #email
        self.email_label=Label(self.ingresar_paciente, text="Correo Electronico: ", bg=self.color3).grid(row=8,column=0)
        self.email=Entry(self.ingresar_paciente, width=10).grid(row=8,column=1)

        #en este se mostraran las citas por paciente
        #citas_agendadas=LabelFrame(ventana_principal, text="Mis Citas", padx=5, pady=5, bg=self.color3)

ventana_principal= GuiDominio()
ventana_principal.mainloop()