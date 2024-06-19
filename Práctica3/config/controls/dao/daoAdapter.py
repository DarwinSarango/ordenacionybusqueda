from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import os.path

import json
import os

T = TypeVar('T')
class DaoAdapter(Generic[T]):
    atype: Type[T]

    def __init__(self, atype: Type[T]):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower()+".json"
        self.URL = os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) + "/data/"

    def _list(self):
        if os.path.isfile(self.URL+self.file):
            f = open(self.URL+self.file, "r")
            datos = json.load(f)
            self.lista.clear   
            for data in datos:
                a = self.atype.deserializar(data) 
                self.lista.addNode(a, self.lista._length)
        return self.lista
    
    def __transform__(self):
        aux = "["
        for i in range(0, self.lista._length):
            if i < self.lista._length - 1:
                aux += str(json.dumps(self.lista.getData(i).serializable)) + ","
            else:
                aux += str(json.dumps(self.lista.getData(i).serializable))
        aux += "]"

        return aux
    
    def to_dic_list(self, lista):
        aux = []
        arreglo = lista.toArray
        for i in range(0, lista._length):
            aux.append(arreglo[i].serializable)
        return aux
    
    def to_dic(self):
        aux = []
        lista = self._list()
        arreglo = lista.toArray
        for i in range(0, lista._length):
            aux.append(arreglo[i].serializable)
        return aux
    
    def _get(self, id):
        list = self._list()
        array = list.toArray
        for i in range(0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None
    
    def _save(self, data) -> T:
        self._list()
        self.lista.addNode(data, self.lista._length) 
        data._id = self.lista._length
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()

    def _delete(self, pos) -> T:
        self._list()
        self.lista.delete(pos)
        self.lista.print
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()


    def _merge(self, data: T, pos) -> T:
        data = self.lista.getData(pos)  #para obtener el id
        self._list()
        self.lista.edit(data, pos)
        a = open(self.URL+self.file, "w")
        a.write(self.__transform__())
        a.close()
     