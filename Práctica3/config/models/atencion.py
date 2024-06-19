class Atencion:
    def __init__(self):
        self.__id = 0
        self.__calificacion = ""
        self.__tiempo = "" 
        self.__motivo = ""
        self.__fecha = ""

    
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _calificacion(self):
        return self.__calificacion

    @_calificacion.setter
    def _calificacion(self, value):
        self.__calificacion = value

    @property
    def _tiempo(self):
        return self.__tiempo

    @_tiempo.setter
    def _tiempo(self, value):
        self.__tiempo = value

    @property
    def _motivo(self):
        return self.__motivo

    @_motivo.setter
    def _motivo(self, value):
        self.__motivo = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value
        

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "calificacion": self.__calificacion,
            "tiempo": self.__tiempo,
            "motivo": self.__motivo,
            "fecha": self.__fecha,
        }

    @classmethod
    def deserializar(self, data):
        atencion = Atencion()
        atencion._id = data["id"]
        atencion._calificacion = data["calificacion"]
        atencion._tiempo = data["tiempo"]
        atencion._motivo = data["motivo"]
        atencion._fecha = data["fecha"]
        return atencion
    
    def __str__(self):
        return f"{self.__id} {self.__calificacion} {self.__tiempo} {self.__motivo} {self.__fecha}"