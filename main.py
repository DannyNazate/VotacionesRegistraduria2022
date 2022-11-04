from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido

#from Controladores.ControladorEstudiante import ControladorEstudiante
#from Controladores.ControladorDepartamento import ControladorDepartamento
#from Controladores.ControladorMateria import ControladorMateria
#from Controladores.ControladorInscripcion import ControladorInscripcion
miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()

#miControladorDepartamento=ControladorDepartamento()
#miControladorMateria=ControladorMateria()
#miControladorInscripcion=ControladorInscripcion()
###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###################################################################################
@app.route("/mesa",methods=['GET'])
def getMesa():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
###################################################################################
@app.route("/partido",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
