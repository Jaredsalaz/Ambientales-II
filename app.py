""" Importamos flask y render_template """
from flask import Flask, render_template

""" instanciamos un objeto app """
app = Flask(__name__)

""" creamos ruta inicial """
@app.route('/')
def home():  
    return render_template("inicio.html")

""" creamos ruta para papel """
@app.route('/papel')
def papel():
    return render_template("papel.html")

""" creamos ruta residuos no organicos """
@app.route('/noOrganico')
def noOrganico():
    return render_template("noOrganico.html")

""" creamos ruta plasticos"""
@app.route('/plastico')
def plastico():
    return render_template("plastico.html")

""" creamos ruta para tetrabriks """
@app.route('/tetrabriks')
def tetrabriks():
    return render_template("tetrabriks.html")

""" creamos ruta para vidrio"""
@app.route('/vidrio')
def vidrio():
    return render_template("vidrio.html")

""" creamos ruta para organicos """
@app.route('/organicos')
def organicos():
    return render_template("organico.html")

""" creamos ruta para pilas """
@app.route('/pilas')
def pilas():
    return render_template("pilas.html")

""" creamos ruta para las colillas de cigarros """
@app.route('/cigarros')
def cigarros():
    return render_template("cigarros.html")

if __name__ == '__main__':
    app.run(debug=True)