from clinica import Clinica
from tkinter import *

clinica= Clinica()
clinica.setNombre(" Clinica de la Salud")
ventana_principal = Tk()
ventana_principal.title(str(clinica.getNombre())) 
ventana_principal.geometry("1300x568")
fondo_imagen= PhotoImage(file="/home/nicolas/Documents/consulta_medica0.0/imagenes/plantilla_gris.png")
fondo= Label(ventana_principal, image=fondo_imagen)
fondo.place(x=0,y=0,relwidth=1, relheight=1)
ventana_principal.mainloop()
