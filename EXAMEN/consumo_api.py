import json
import requests
import random


def get_carter_by_id(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic

def ordenar_nombre(peronaje):
    return peronaje['name']

def altura(item):
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1

def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1

def color_pelo(item):
    return item['hair_color'] + item['name']

def consumo_api(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic



def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data


def search_characters_by_name(name):
    data = get_docs("https://swapi.dev/api/people?search="+str(name))
    return data['results']

def get_all_sw_characters():

    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            sw_data.append(personaje) 
        data = get_docs(data["next"])
    
    return sw_data

def get_all_sw_characters_names():
    
    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            sw_data.append(personaje['name'])
        data = get_docs(data["next"])
    
    return sw_data

def get_planeta(url):
    planeta = get_docs(url)
    return planeta['name']
