from clinica import Clinica
from tkinter import *

clinica= Clinica()
clinica.setNombre(" Clinica de la Salud")
ventana_principal = Tk()
ventana_principal.title(str(clinica.getNombre())) 
ventana_principal.geometry("1300x568")
fondo_imagen= PhotoImage(file="/home/nicolas/Documents/consulta_medica0.0/imagenes/plantilla_gris.png")
fondo= Canvas(ventana_principal, width=1300, height=568)
fondo.pack(fill="both",expand=True)
fondo.create_image(0,0,image=fondo_imagen,anchor="nw")
ventana_principal.mainloop()
