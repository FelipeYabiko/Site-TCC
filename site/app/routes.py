from app import app
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup
from app.pesquisa import mercadolivre
from app.pesquisa import trocafone

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resultado', methods=['GET' , 'POST'])
def resul():
    
    if request.method == "POST":
        produto_nome = request.form.get('produto')
        if produto_nome == "":
            return render_template("index.html")
        preco_mercadolivre = mercadolivre(produto_nome)
        preco_trocafone = trocafone(produto_nome)
        
        lista = [preco_mercadolivre, preco_trocafone]
        print(lista)
        lista = sorted(lista)
        
        print(lista)
    return render_template('resultados.html',lista=lista)    


@app.route('/layout')
def layout():

    return render_template('layout.html')
    