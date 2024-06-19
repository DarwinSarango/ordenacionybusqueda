from controls.tda.queque.queque import QueQue
from models.atencion import Atencion

class ServidorPublico:
    def __init__(self):
        self.__id = 0
        self.__nombreServidor = ""
        self.__apellidoServidor = ""
        self.__especialidad = ""


    @property
    def _apellidoServidor(self):
        return self.__apellidoServidor

    @_apellidoServidor.setter
    def _apellidoServidor(self, value):
        self.__apellidoServidor = value

    @property
    def _especialidad(self):
        return self.__especialidad

    @_especialidad.setter
    def _especialidad(self, value):
        self.__especialidad = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombreServidor(self):
        return self.__nombreServidor

    @_nombreServidor.setter
    def _nombreServidor(self, value):
        self.__nombreServidor = value

    @property
    def _atenciones(self):
        return self.__atenciones

    @_atenciones.setter
    def _atenciones(self, value):
        self.__atenciones = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "nombreServidor": self.__nombreServidor,
            "apellidoServidor": self.__apellidoServidor,
            "especialidad": self.__especialidad,
        }
    @classmethod
    def deserializar(self,data):
        servidor = ServidorPublico()
        servidor._id = data["id"]
        servidor._nombreServidor = data["nombreServidor"]
        servidor._apellidoServidor = data["apellidoServidor"]
        servidor._especialidad = data["especialidad"]

        return servidor
    
    def __str__(self):
        return f"ServidorPublico: {self.__id} {self.__nombreServidor} {self.__apellidoServidor} {self.__especialidad}"