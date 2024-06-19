from numbers import Number
from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException
from models.atencion import Atencion
from controls.ordenacion.quicksort import QuickSort
from controls.ordenacion.mergesort import MergeSort
from controls.ordenacion.shellsort import ShellSort
from controls.tda.linked.burbuja import Burbuja


class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
    

    @property
    def _atype(self):
        return self.__atype

    @_atype.setter
    def _atype(self, value):
        self.__atype = value


    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value
 
        
    @property    
    def isEmpty(self):
        return self.__head == None or self._length == 0
    
    def _getFirst_(self, poss):
        if not self.isEmpty:
            return self.__head
        else:
            return "List is Empty"
    
    def _getLast_(self, poss):
        if not self.isEmpty:
            return self.__last
        else:
            return "List is Empty"
        
    def getData(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head._data
        elif poss == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node._data
        

    def getNode(self, poss):
        if self.isEmpty:
           raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            return self.__head
        elif poss == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < poss:
                cont += 1
                node = node._next
            return node
            
        
    
    def addFirst(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            headOld = self.__head #guarada toda la lista hara ahora
            node = Node(data, headOld)  
            self.__head = node
            self.__length += 1

    def addLast(self, data):
        if self.isEmpty:
            self.addFirst(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    
    def addNode(self, data, poss):
       
        if poss == 0:
            self.addFirst(data)
        elif poss == self.__length:
            self.addLast(data)
        else:
            node_preview = self.getNode(poss - 1)
            node_actuality = node_preview._next
            node = Node(data, node_actuality)
            node_preview._next = node
            self.__length += 1


    def edit (self, data, poss = 0):
        if poss == 0:
            print("entro en 0 en edit")
            print(data)
            self.__head._data = data
        elif poss == (self.__length - 1):
            self.__last._data = data
        else:
            node = self.getNode(poss)
            node._data = data

    def add(self, data, pos = 0):
        if pos == 0:
            self.addFirst(data)
        elif pos == self.__length:
            self.addLast(data)
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    @property
    def toArray (self):
        array = []
        node = self.__head
        while node != None:
            array.append(node._data)
            node = node._next
        return array
    
    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.addLast(array[i])


    def dicToListLast(self, array_dict):
        for i in range(0, len(array_dict)):
            data = Atencion().deserializar(array_dict[i])                
            self.addLast(data)

    def dicToListFirst(self, array_dict):
        for i in range(0, len(array_dict)):
            a = Atencion().deserializar(array_dict[i])
            print(a)            
            self.addFirst(a)
            
    
    def delete(self, poss = 0 ):
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        elif poss < 0 or poss >= self.__length:
            raise ArrayPositionException("Index out of range")
        elif poss == 0:
            node = self.__head._next
            del self.__head
            self.__head = node
            self.__length -= 1
        elif poss == (self.__length - 1):
            print("entro en el ultimo")
            node = self.getNode(self.__length - 2)
            node._next = None
            del self.__last
            self.__last = node
            self.__length -= 1
            print(self.__length)
        else:
            node_previous = self.getNode(poss-1)
            node_next = node_previous._next._next
            node_previous._next = node_next
            self.__length -= 1
#Metodo burbuja
    def sort(self, type):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            #datos primitivos
            if isinstance(array[0], Number) or isinstance(array[0], str):
                #order = Burbuja()
                order = Burbuja()
                if type == 1:
                    array = order.sort_burbuja_number_ascendent(array)
                    #array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_burbuja_number_descendent(array)
                    #array = order.sort_primitive_descendent(array)
            self.toList(array)

    def sort_models(self, attribute, type = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                #order = Burbuja()
                order = Burbuja()
                if type == 1:
                    #array = order.sort_burbuja_attribute_ascendent(array, attribute)
                    array = order.sort_burbuja_attribute_ascendent(array, attribute)
                else:
                    #array = order.sort_burbuja_attribute_descendent(array, attribute)
                    array = order.sort_burbuja_attribute_descendent(array, attribute)
                #cls = getattr(array[0], "_apellidos")
                #print(cls)
            self.toList(array)   
        return self
    
    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            for i in range(0, len(array)):
                if(array[i].lower().__contains__(data.lower())):    
                    list.add(array[i], list._length)
        return list    
#Metodo QuickSort
    def QuickSort(self, type):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            # datos primitivos
            if isinstance(array[0], (int, float, str)):
                order = QuickSort()
                if type == 1:
                    array = order.sort_primitive_quicksort(array)
                else:
                    array = order.sort_primitive_quicksort(array)[::-1]
            self.toList(array)

    def sort_models_quickSort(self, attribute, type=1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                order = QuickSort()
                if type == 1:
                    array = order.sort_models_quicksort(array, attribute)
                else:
                    array = order.sort_models_quicksort(array, attribute)[::-1]
            self.toList(array)
        return self
    
#Metodo MergeSort
    def sortMerge(self, type):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            # datos primitivos
            if isinstance(array[0], (int, float, str)):
                order = MergeSort()
                if type == 1:
                    array = order.sort_primitive_mergesort(array)
                else:
                    array = order.sort_primitive_mergesort(array)[::-1]
            self.toList(array)

    def sort_models_mergeSort(self, attribute, type=1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                order = MergeSort()
                if type == 1:
                    array = order.sort_models_mergesort(array, attribute)
                else:
                    array = order.sort_models_mergesort(array, attribute)[::-1]
            self.toList(array)
        return self
    
#Metodo ShellSort
    def sortShell(self, type):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            # datos primitivos
            if isinstance(array[0], (int, float, str)):
                order = ShellSort()
                if type == 1:
                    array = order.sort_primitive_shellsort(array)
                else:
                    array = order.sort_primitive_shellsort(array)[::-1]
            self.toList(array)
    
    def sort_models_shellSort(self, attribute, type=1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                order = ShellSort()
                if type == 1:
                    array = order.sort_models_shellsort(array, attribute)
                else:
                    array = order.sort_models_shellsort(array, attribute)[::-1]
            self.toList(array)
        return self
    

    #Metodo de busqueda binaria
    def busqueda_binario(self, lista, objetivo):
        if isinstance(lista, Linked_List):
            lista.sort(1)  # Ordena la lista en orden ascendente
            arreglo = lista.toArray
        else:
            arreglo = lista

        inicio = 0
        fin = len(arreglo) - 1

        while inicio <= fin:
            centro = (inicio + fin) // 2
            if arreglo[centro] == objetivo:
                return arreglo[centro]
            elif arreglo[centro] < objetivo:
                inicio = centro + 1
            else:
                fin = centro - 1

        return -1


    def busqueda_binario_models(self, lista, atributo, objetivo):
        if isinstance(lista, Linked_List):

            lista.sort_models(atributo, 1)  # ordena la lista en orden ascendente según el atributo
            arreglo = lista.toArray
        else:
            arreglo = lista

        inicio = 0
        fin = len(arreglo) - 1

        while inicio <= fin:
            centro = (inicio + fin) // 2
            valor_centro = getattr(arreglo[centro], atributo)

            if valor_centro == objetivo:
                return arreglo[centro]
            elif valor_centro < objetivo:
                inicio = centro + 1
            else:
                fin = centro - 1
        return -1  # Aqui se retorna -1 si no se encuentra el objetivo en la lista

    #Metodo lineal binario
    def busqueda_lineal_binario(self, lista, objetivo):
        if isinstance(lista, Linked_List):
            lista.sort(1)  # Ordena ascendente
            arreglo = lista.toArray
        else:
            arreglo = lista

        for i in range(len(arreglo)):
            if arreglo[i] == objetivo:
                return i
        return -1

    def busqueda_lineal_binario_models(self, lista, objetivo, attribute):
        listita = Linked_List()
        if isinstance(lista, Linked_List):
            lista.sort(1)  # Ordenaa lista  ascendente
            arreglo = lista.toArray
        else:
            arreglo = lista
        
        for i in range(len(arreglo)):
            valor_centro = getattr(arreglo[i], attribute)

            if valor_centro == objetivo:
                listita.add(arreglo[i], listita._length)
        return listita
    
    ########################################################################################
    #serializable
    @property
    def serializable(self):
        array = self.toArray 
        array_dict = []
        for i in range(0, len(array)): 
            array_dict.append(array[i].serializable) 
        return array_dict
    

    @classmethod
    def deserializar(self, array_dict):
        linked = Linked_List()
        linked.dicToListLast(array_dict)
        return linked
    
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def __str__(self) -> str: #metodo toString    #cometar ctrl+k+c   / ctrl+k+u
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " -> "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None :
            data += str(node._data) + "   "
            node = node._next
        print("Lista de datos")
        print(data)
    
    #Eliminar
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element
        

    #Segunda opcion de toArray
    @property   
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                array.append(node._data)	
                cont += 1
                node = node._next
        return array