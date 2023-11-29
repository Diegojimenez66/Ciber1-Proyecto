from flask import request, session
import json
import decimal
from __main__ import app
import controlador_maquinas

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/maquinas",methods=["GET"])
def maquinas():
    maquinas,code= controlador_maquinas.obtener_maquinas()
    return json.dumps(maquinas, cls = Encoder),code

@app.route("/maquina/<id>",methods=["GET"])
def maquina_por_id(id):
    maquina,code = controlador_maquinas.obtener_maquina_por_id(id)
    return json.dumps(maquina, cls = Encoder),code

@app.route("/maquinas",methods=["POST"])
def guardar_maquina():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        maquina_json = request.json
        ret,code=controlador_maquinas.insertar_maquina(maquina_json["nombre"], maquina_json["descripcion"], float(maquina_json["precio"]), maquina_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/maquinas/<id>", methods=["DELETE"])
def eliminar_maquina(id):
    ret,code=controlador_maquinas.eliminar_maquina(id)
    return json.dumps(ret), code

@app.route("/maquinas", methods=["PUT"])
def actualizar_maquina():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        maquina_json = request.json
        ret,code=controlador_maquinas.actualizar_maquina(maquina_json["id"],maquina_json["nombre"], maquina_json["descripcion"], float(maquina_json["precio"]),maquina_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code