from flask import Flask,render_template
from pymongo import MongoClient

def conexion():
    # return MongoClient("localhost",27017)
    return MongoClient("mongodb+srv://admin:lpajaro@cluster0.xttb3.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Lista las universidades
def listaUniversidades():
    mongo = conexion()
    dbeducacion = mongo["Educacion"]
    coleccionUniversidades =  dbeducacion["universidades"]
    listauniversidades = coleccionUniversidades.find({},{"_id":0})
    lg = [lg for lg in listauniversidades]
    mongo.close()
    return lg 


app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def index():
    lg=listaUniversidades()
    return render_template('inicio.html',universidades = lg)


@app.route('/mapa')
def mapa():
    lg=listaUniversidades()
    return render_template('mapa.html',universidades = lg)


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

