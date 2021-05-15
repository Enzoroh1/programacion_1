from consumo_api import get_all_sw_characters_names, get_charter_by_id
from consumo_api import altura
from consumo_api import peso
from random import randint

id1 = randint(1,83),
personaje1 = get_charter_by_id(1)


id2 = randint(1,83),
personaje2 = get_charter_by_id(5)



#EJERCICIO A
if (altura(personaje1) > altura(personaje2)) :
   print ("El personaje mas alto es ",personaje1["name"],"la altura es ", altura(personaje1))

else:
    print ("El personaje mas alto es",personaje2["name"],"la altura es ", altura(personaje2))

#EJERCICIO B
if (peso(personaje1)) > (peso(personaje2)):

   print ("El personaje mas pesado es",personaje1["name"],"el peso es ", altura(personaje1))

else:
    print ("El personaje mas pesado es",personaje2["name"],"el peso es ", altura(personaje2))


#EJERCICIO C
films1 = len(personaje1["films"])
films2 = len(personaje2["films"])

if(films1 == films2 ):
    print("los personajes ",personaje1["name"]," y ",personaje2["name"], "participaron en la misma cantidad de peliculas")

if(films1 > films2):
    print("el personaje que participo en mas peliculas es: ",personaje1["name"], "con un total de", films1)
elif(films1 < films2):
    print("el personaje que participo en mas peliculas es: ",personaje2["name"], "con un total de", films2)



#EJERCICIO D
if (personaje1 == "Yoda" or personaje2 == "Grievous" or  personaje1 == "Grievous" or personaje2 == "Yoda") :
    print(personaje1)
    print(personaje2)