from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_maquina(nombre, descripcion, precio,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO maquinas(nombre, descripcion, precio,foto) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion, precio,foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un maquina", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_maquina_a_json(maquina):
    d = {}
    d['id'] = maquina[0]
    d['nombre'] = maquina[1]
    d['descripcion'] = maquina[2]
    d['precio'] = maquina[3]
    d['foto'] = maquina[4]
    return d

def obtener_maquinas():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM maquinas")
            maquinas = cursor.fetchall()
            maquinasjson=[]
            if maquinas:
                for maquina in maquinas:
                    maquinasjson.append(convertir_maquina_a_json(maquina))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los maquinas", file=sys.stdout)
        maquinasjson=[]
        code=500
    return maquinasjson,code

def obtener_maquina_por_id(id):
    maquinajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM maquinas WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM maquinas WHERE id =" + id)
            maquina = cursor.fetchone()
            if maquina is not None:
                maquinajson = convertir_maquina_a_json(maquina)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un maquina", file=sys.stdout)
        code=500
    return maquinajson,code


def eliminar_maquina(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM maquinas WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un maquina", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_maquina(id, nombre, descripcion, precio, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE maquinas SET nombre = %s, descripcion = %s, precio = %s, foto=%s WHERE id = %s",
                       (nombre, descripcion, precio, foto,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un maquina", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
