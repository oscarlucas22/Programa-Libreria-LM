from flask import Flask, render_template, abort
app = Flask(__name__)
import json

with open("books.json") as fichero:
    datos = json.load(fichero)

app.run("0.0.0.0",5000,debug=True)
