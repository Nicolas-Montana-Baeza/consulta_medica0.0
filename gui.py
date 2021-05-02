from clinica import Clinica
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
from tkinter import *

class Root(Tk):
  
    def __init__(self):
        super(Root, self).__init__()
        self.title("Consulta medica")
        self.minsize(720, 600)##ancho y alto
        self.configure(background='light blue')

        def imprima_mes():
            print(radioLeido)
            
        def obtenga_informacion():
                Monto_Informacion=e1.get()*informaciones[radioLeido.get()]
                print("informacion:",informaciones[radioLeido.get()])
            
        def imprima_mes():
            print(radioLeido)
            
        def obtenga_informacion():
            Monto_Informacion=e1.get()*informaciones[radioLeido.get()]
            print("informacion:",informaciones[radioLeido.get()])
            
        
        app = Tk() 
        app.geometry('600x400')
        app.title("Medico")
        radioLeido = IntVar() 

        
       
        Boton_1 =   Button(app,  text="Aceptar", fg="Blue",command=obtenga_informacion).place(x=250,y=150)

        rdioOne.grid(column=0, row=0)
        rdioTwo.grid(column=0, row=1)
        rdioThree.grid(column=0, row=2)


        self.tab2 = ttk.Frame(tabControl)

        tabControl.add(self.tab2, text="Paciente")
        def muestra_datos():
            print("Nombre: ", e1.get(),"Apellido:", e2.get() )
        app = Tk()
        Etiqueta_1=Label(app, text="Nombre ").grid(row=0)
        Etiqueta_2=Label(app, text="Apellido ").grid(row=1)
        Etiqueta_2=Label(app, text="Dirección").grid(row=2)
        Boton_1 =   Button(app,  text="Imprima los datos", fg="Blue",command=muestra_datos).place(x=250,y=150)
        app.geometry('600x400')
        app.title("Datos del Paciente")
        e1 = Entry(app)
        e2 = Entry(app)
        e3 = Entry(app)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        rdioOne = Radiobutton(app, text='Neurologo', variable=radioLeido, value=0) 
        rdioTwo = Radiobutton(app, text='Dentista', variable=radioLeido, value=1) 
        rdioThree = Radiobutton(app, text='Medico general', variable=radioLeido, value=2)




        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Cita")

        tabControl.pack(expand=0, fill="both")

    def startpressed(self):
        new = tk.Toplevel(self)
        new.minsize(720, 600)
        new.geometry('720x600')
        new.configure(background="blue")
        tabControl1 = ttk.Notebook(new)
        new.tab1 = ttk.Frame(tabControl1)
        tabControl1.add(new.tab1, text="tab 1")
        tabControl1.pack(expand=1)

    def createMenu(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Salir")

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="pregunta")

    def submit(self):
        newTop = Toplevel(self.master)
        display = Label(newTop, text="Review").pack()
        newTop.title("Review and Submit")
        newTop.focus_set()
        newTop.geometry("720x600")
        # WOULD LIKE: when this button is clicked it takes the user to tab 7 of the notebook window
        btnResult = Button(newTop, text="Tab 3").pack()
        btnBack = Button(newTop, text="Back").pack()

root = Root()
root.mainloop()
