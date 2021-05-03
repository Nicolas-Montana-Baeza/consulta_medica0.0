from clinica import Clinica
from tkinter import *
##creacion de ventana y fondo
clinica= Clinica()
clinica.setNombre(" Clinica de la Salud")
ventana_principal = Tk()
ventana_principal.title(str(clinica.getNombre())) 
ventana_principal.geometry("1300x568")
ventana_principal.configure(bg="#788890")
def crearSeleccionDeEspecialidad():
    especialidades=[
    ("Medicina General", "Medicina General"),
    ("Kinesiologia", "Kinesiologia"),
    ("Pediatria", "Pediatria"),
    ("Odontologia", "Odontologia")
    ]
    opcion = StringVar()
    opcion.set("Medicina General")

    for texto, especialidad in especialidades:
        Radiobutton(ventana_principal, text=texto, variable=opcion, value=especialidad, bg="#788890").pack(anchor=W)
crearSeleccionDeEspecialidad()
ventana_principal.mainloop()
