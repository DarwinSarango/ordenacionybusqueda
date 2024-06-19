from flask import Blueprint, jsonify, abort, request, render_template, redirect
from controls.atencionControl import AtencionControl
from controls.servidorControl import ServidorControl
from controls.tda.linked.linkedList import Linked_List

router = Blueprint('router', __name__)

# GET is for presenting data
# POST is for saving data, modifying data, and logging in

@router.route('/')
def home():
    return render_template('index.html')

# LISTA SERVIDORES PUBLICOS
@router.route('/servidor')
def lista_servidores():
    sc = ServidorControl()
    servidores = sc._list()
    return render_template('ventanilla/ventanilla.html', lista=sc.to_dic_list(servidores))

@router.route('/servidor/<tipo>/<attr>/<algoritmo>')
def ordenar_servidores(tipo, attr, algoritmo):
    sc = ServidorControl()
    servidores = sc._list()

    if algoritmo == 'quicksort':
        servidores.sort_models_quickSort(attr, int(tipo))
    elif algoritmo == 'mergesort':
        servidores.sort_models_mergeSort(attr, int(tipo))
    elif algoritmo == 'shellsort':
        servidores.sort_models_shellSort(attr, int(tipo))
    else:
        servidores.sort_models_quickSort(attr, int(tipo))
    
    return render_template('ventanilla/ventanilla.html', lista=sc.to_dic_list(servidores))

#BUSCAR SERVIDOR PUBLICO
@router.route('/servidor/buscar/<searchType>/<searchTerm>/<searchAlgorithm>')
def buscar_servidores(searchType, searchTerm, searchAlgorithm):
    sc = ServidorControl()
    servidores = sc._list()

    if searchAlgorithm == 'binarysearch':
            dato = servidores.busqueda_binario_models(servidores, searchType, searchTerm)
            servidores.clear
            servidores.addNode(dato, 0)

    elif searchAlgorithm == 'linearsearch':
        servidores = servidores.busqueda_lineal_binario_models(servidores, searchTerm, searchType)
    else:
        servidores = []

    return jsonify(sc.to_dic_list(servidores)) 






# EDITAR SERVIDOR PUBLICO
@router.route('/servidor/editar/<pos>')
def ver_editar_servidor(pos):
    sc = ServidorControl()
    servidor = sc._get(int(pos))
    return render_template("ventanilla/editar.html", data=servidor)

# VER ATENCIONES DEL SERVIDOR PUBLICO
@router.route('/servidor/atenciones/<pos>', methods=['GET', 'POST'])
def ver_atenciones_servidor(pos):
    sc = ServidorControl()
    atenciones = sc._list().getData(int(pos)-1)._atenciones
    return render_template("ventanilla/listaAtenciones.html", lista=atenciones.serializable, idServidor=pos)

# MODIFICAR SERVIDOR PUBLICO
@router.route('/servidor/modificar', methods=["POST"])
def modificar_servidor():
    sc = ServidorControl()
    data = request.form
    pos = data["id"]
    servidor = sc._list().getData(int(pos)-1)   

    # TODO ...Validar
    sc._servidor = servidor
    sc._servidor._nombreServidor = data["nombreServidor"]
    sc._servidor._apellidoServidor = data["apellidoServidor"]
    sc._servidor._especialidad = data["especialidad"]
    sc.merge(int(pos)-1)
    return redirect("/servidor", code=302)

# ELIMINAR SERVIDOR PUBLICO
@router.route('/servidor/eliminar/<pos>')
def eliminar_servidor(pos):
    sc = ServidorControl()
    sc._delete(int(pos)-1)
    return redirect("/servidor", code=302)

# ELIMINAR ATENCION
@router.route('/servidor/atenciones/eliminar/<idServidor>')
def eliminar_atencion(idServidor):
    sc = ServidorControl()
    atenciones = sc._list().getData(int(idServidor)-1)._atenciones
    atenciones.dequeque()
    servidor = sc._list().getData(int(idServidor)-1)
    servidor._atenciones = atenciones
    sc.merge(int(idServidor)-1)
    return redirect("/servidor/atenciones/" + idServidor, code=302)

# INGRESAR NUEVA ATENCION
@router.route('/servidor/atenciones/ver/<idServidor>')
def registrar_atencion(idServidor):
    return render_template('ventanilla/registrar.html', idServidor=idServidor)

@router.route('/servidor/atenciones/registrar/<idServidor>', methods=["POST"])
def guardar_atencion(idServidor):
    sc = ServidorControl()
    ac = AtencionControl()
    data = request.form
    ac._atencion._calificacion = data["calificacion"]
    ac._atencion._tiempo = data["tiempo"]
    ac._atencion._motivo = data["motivo"]
    ac._atencion._fecha = data["fecha"]
    ac.save()
    atenciones = sc._list().getData(int(idServidor)-1)._atenciones
    atenciones._top = 15
    if atenciones.verifyTop == False: 
        return redirect("/servidor/atenciones/" + idServidor, code=302)
    else:
        atenciones.queque(ac._atencion)
        servidor = sc._list().getData(int(idServidor)-1)
        servidor._atenciones = atenciones
        sc._servidor = servidor
        sc.merge(int(idServidor)-1)
        return redirect("/servidor/atenciones/" + idServidor, code=302)
