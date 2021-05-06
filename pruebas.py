from clinica import *
from random import randint
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

def crearPersonas(_nombres,_ruts, _emails,_edades):
    personas=[]
    _nombres=formatoNombres(_nombres)
    
    if len(_nombres)==len(_ruts) and len(_ruts) == len(_emails) and len(_emails)==len(_edades):
        
        for i in range (len(_nombres)):
            
            if len(_nombres[i])>=3 and Persona.isRut(_ruts[i]) and Persona.isMail(_emails[i]) and type(_edades[i])==int and 1 <= int(_edades[i]):
                persona_aux=Persona(_nombres[i][0],_nombres[i][1::-2],_nombres[i][-2],_nombres[i][-1],_ruts[i],_edades[i],_emails[i], "")
                personas.append(persona_aux)
    
        return personas
    else:
        return False

lista_doctores=["ADRIANA CAROLINA HERNANDEZ MONTERROZA", "MARCELA ADRIANA  REY SANCHEZ","ANDREA CATALINA ACERO CARO","BRIGITE . POLANCO RUIZ","CRISTINA ELIZABETH BARTHEL GUARDIOLA","GLORIA PATRICIA MENDOZA ALVEAR","LAURA . DIAZ MEJIA","MARIANA DEL PILAR SANTOS MILACHAY","PAOLA ANDREA CORREA LARIOS","YURI CATALINA SALAZAR ARISTIZABAL"]
lista_ruts=["14541798-8","20784145-5","14077811-7","14860117-8","7590500-9","17851414-8","7889811-9","11599665-7","19566898-1","9014730-7"]
lista_emails=crearEmails(lista_doctores)
lista_edades=crearEdad(lista_doctores)

lista_personas=crearPersonas(lista_doctores,lista_ruts,lista_emails,lista_edades)

"""
if len(lista_doctores)==len(lista_ruts):
    for i in range (len(lista_doctores)):
        print("entre"+str(i))
        if len(lista_doctores[i])>=3:
                print("cree")
                persona_aux=Persona(lista_doctores[i][0],lista_doctores[i][1::-2],lista_doctores[i][-2],lista_doctores[i][-1],lista_ruts[i],lista_edades[i],lista_emails,"")
                lista_personas.append(persona_aux)
print("sali")"""

for persona in lista_personas:
    print(persona.getPrimerNombre())