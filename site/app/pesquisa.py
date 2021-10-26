
import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request
from app import app

def sem_ponto(preco):

    preco = list(preco)
    preco.remove(".")
    preco = "".join(preco)

    return preco

def tiravirgula(preco):

    preco = list(preco)
    i = preco.index(",")
    preco = preco[:i]

def reinverte(preco):

    preco = list(preco)
    preco = preco[::-1]

    i = preco.index(",")

    preco = preco[:i]

    for n in preco:
     if n != "0": 
        return True
    return False


    
def mercadolivre(produto_nome):
    url_base = 'https://lista.mercadolivre.com.br/'
    try:
        
        
        response = requests.get("https://lista.mercadolivre.com.br/"+produto_nome)

        site = BeautifulSoup(response.text, 'html.parser')

        produtos = site.find('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})


        precoreal = produtos.find('span', attrs={'class': 'price-tag-fraction'})
        precocentavos = produtos.find('span', attrs={'class': 'price-tag-cents'})
        prereais = produtos.find('span', attrs={'class': 'price-tag-symbol'})

        titulo = produtos.find('h2', attrs={'class': 'ui-search-item__title'})

        link = produtos.find('a', attrs={'class': 'ui-search-link'})

        print(precocentavos)
        print(precoreal)
        print(prereais)

        print ("o titulo do produto é: ", titulo.text)
        print ("o preço do produto é: ", prereais.text, precoreal.text+ "."+ precocentavos.text)
        print ("o link do produto é: ", link['href'])

        tituloescrito = titulo.text
        linkescrito = link['href']

        preco_mercadolivre = precoreal.text
        if "." in preco_mercadolivre:
            preco_mercadolivre = sem_ponto(precoreal.text)


        preco_mercadolivre += "."+ precocentavos.text
        preco_mercadolivre = float(preco_mercadolivre)
        
        return [preco_mercadolivre, tituloescrito, linkescrito, "Mercado Livre"]

    except AttributeError:
        return [preco_mercadolivre,"Algo deu errado", linkescrito, "Mercado Livre"]
        
    

def trocafone(produto_nome):
    
    try:
       
        
        url_base = 'https://www.trocafone.com/comprar/list?q='    
            
        response = requests.get("https://www.trocafone.com/comprar/list?q="+produto_nome)

        site = BeautifulSoup(response.text, 'html.parser')

        produtos = site.find('div', attrs={'class': 'js-results-container search-result-container'})


        precorealt = produtos.find('span', attrs={'class': 'price-value'})
        '''
        precocentavos = produtos.find('div', attrs={'class': 'mGXnE _37W_B'})
        '''
        prereaist = produtos.find('span', attrs={'class': 'currency_sign'})
    
        titulot = produtos.find('div', attrs={'class': 'product_title'})


        links = produtos.find ('div', attrs={'product_title'})
        linkt = links.a

        print(f"aaaaaaaaaaaaaa {linkt}")
        print(type(linkt))
        print(linkt["href"])

        textot= titulot.text.strip()

        
        print ("o titulo do produto é: ", textot)
        print ("o preço do produto é: ", prereaist.text, precorealt.text)
        print ("o link do produto é: ", linkt)
        
        print(precorealt.text)
        preco = precorealt.text
        if "." in precorealt.text:
            preco = sem_ponto(precorealt.text)
        preco= preco.replace(",", ".")
        preco = float(preco)
        
        return [preco, textot, linkt['href'], "Troca Fone" ]
        
    except AttributeError:
        return [preco, "Algo deu errado", linkt['href'], "Troca Fone" ]
 




    