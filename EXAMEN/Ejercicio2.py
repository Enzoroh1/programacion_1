import json
import requests

def consultar_personajes(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        diccionario = json.loads(respuesta.text)
        return diccionario
    else:
        print('nope')


urlbase = consultar_personajes('https://swapi.dev/api/people/')

#EJERCICIO A
sw_data = []

while(urlbase['next'] is not None):
    for doc in urlbase['results']:
        sw_data.append(doc)
    urlbase = consultar_personajes(urlbase['next'])


def nombre (item):
    return (item['name'])

sw_data.sort(key=nombre)

for index, character in enumerate(sw_data):
    
    print(character['name'], character['species'], character['homeworld'])

#EJERCICIO B
for personaje in sw_data:
    if(len(personaje["films"]) == 6):
        print(personaje["name"])