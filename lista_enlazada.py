class listaEncadenada:
    def __init__(self):
        self.cabeza = None
#________________________________________________
# Método para agregar elementos en el frente de la lsta encadena
    def adicionarFrente(self, data):
        self.cabeza = Nodo(data=data, proximo=self.cabeza)
#________________________________________________
# Método para verificar si la estructura de datos esta vacia
    def esVacio(self):
        return self.cabeza == None
#_________________________________________________
# Método para agregar elementos al final de la lista encadenada
    def adicionarFinal(self, data):
        if not self.cabeza:
            self.cabeza = Nodo(data=data)
            return
        curr = self.cabeza
        while curr.proximo:
            curr = curr.proximo
            curr.proximo = Nodo(data=data)
# Método para eliminar Nodos
#__________________________________________________
    def eliminarNodo(self, key):
        curr = self.cabeza
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.proximo
        if prev is None:
            self.cabeza = curr.proximo
        elif curr:
            prev.proximo = curr.proximo
        curr.proximo = None
# __________________________________________
    def estaEnLista(self,keyBuscar):
        esta = False
        curr=self.cabeza
        while curr and not esta :
            if curr.clave==keyBuscar :
                esta=True
            break
        curr = curr.proximo
        return esta
#___________________________________________________
# Método para obtener el ultimo Nodo
    def ultimoNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        return temp.data
#___________________________________________________
# Método para imprimir la lista de Nodos
    def imprimirLista( self ):  
        Nodo = self.cabeza
        while Nodo != None:
            print(Nodo.data, end =" ---& ")
            Nodo = Nodo.proximo
# ________________________________________________
# Creamos clase nodo
class Nodo:
    def __init__(self, data = None, proximo = None):
        self.data = data
        self.proximo = proximo
        self.clave=None
    def __str__(self):
        return str(self.data)