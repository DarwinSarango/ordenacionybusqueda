import random
import sys
import time
sys.path.append('../')
from controls.servidorControl import ServidorControl
from controls.tda.queque.queque import QueQue
from controls.atencionControl import AtencionControl
from controls.tda.linked.linkedList import Linked_List
from controls.ordenacion.quicksort import QuickSort

sdp = ServidorControl()
atc = AtencionControl()
queque = QueQue(15)
try:
    

    # sdp._servidor._nombreServidor = "Juan"
    # sdp._servidor._apellidoServidor = "Perez"
    # sdp._servidor._especialidad = "Medico General"
    # sdp.save


    # atc._atencion._calificacion = "Excelente"
    # atc._atencion._fecha = "2021-10-10"
    # atc._atencion._motivo = "Consulta"
    # atc._atencion._tiempo = "10:00"
    # queque.queque(atc._atencion)

    # atc._atencion._calificacion = "Mala"
    # atc._atencion._fecha = "2021-10-10"
    # atc._atencion._motivo = "Consulta"
    # atc._atencion._tiempo = "10:00"
    # queque.queque(atc._atencion)


    # sdp._servidor._nombreServidor = "Dr. Juan Perez"
    # sdp._servidor._atenciones = queque
    # inicio = time.time()
    # sdp.save
    # fin = time.time()

    # sdp._servidor._nombreServidor = "Dr. Maria Lopez"
    # sdp._servidor._atenciones = queque
    # inicio = time.time()
    # sdp.save
    # fin = time.time()

    # sdp._servidor._nombreServidor = "Dr. Carlos Ramirez"
    # sdp._servidor._atenciones = queque
    # inicio = time.time()
    # sdp.save
    # fin = time.time()

    # print("Tiempo de ejecucion: ", fin - inicio)


    # # #Numeros
    # lista = Linked_List()
    # for i in range(25000):
    #     lista.add(round(random.random()*1000, 2))
    # #lista.print
    # inicio = time.time()
    # #lista.QuickSort(1)
    # #lista.sortMerge(1)
    # #lista.sortShell(1)
    # fin = time.time()
    # print("Tiempo de ejecución: Método ShellSort ", fin - inicio)
    # #lista.print

    #sdp._list().print
    #listaAux = sdp._list().sort_models_quickSort("_especialidad", 1)
    #listaAux = sdp._list().sort_models_mergeSort("_nombreServidor", 2)
    #listaAux.print


    # Buscar con busqueda binaria
    # listaS = Linked_List()
    # sdp._list().print
    # print("HOLA BUSCADO")
    # listita = listaS.busqueda_lineal_binario_models(sdp._list(),"Mario", "_nombreServidor")
    # listita.print


    # #Numeros Busqueda Binario
    lista = Linked_List()
    for i in range(25000):
        lista.add(round(random.random()*1000, 2))
    inicio = time.time()
    listita = lista.busqueda_lineal_binario(lista, 5000 )
    fin = time.time()
    print("Tiempo de ejecución: Busqueda Binaria ", fin - inicio)

    
except Exception as error:
    print("Errores:")
    print(error)