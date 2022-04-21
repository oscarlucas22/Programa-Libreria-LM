from flask import Flask, render_template, abort
app = Flask(__name__)
import json

with open("books.json") as fichero:
    datos = json.load(fichero)
    
@app.route('/')
def inicio():
    return render_template("inicio.html", datos = datos)
    
@app.route('/libro/<isbn>')
def libro(isbn):
    for libro in datos:
        if libro.get("isbn") == isbn:
            return render_template("libro.html", libro = libro)
    abort(404)

@app.route('/categorias/<categoria>')
def categorias(categoria):
    return render_template("categorias.html", datos = datos, categoria = categoria)

app.run("0.0.0.0",5000,debug=True)
