
#1. importar la clase 

from personaje import *

#2. instanciar un objeto 

heroe = personaje()

#3. acceder a sus atributo 

print("atributos personaje")
print("el personaje pertenece a la raza: " + heroe.especie)
print("se llama: " + heroe.nombre)
print("mide: " + str(heroe.altura) + " metros")
print("")

print("metodos personaje")

heroe.correr(True)
heroe.lanzargranada
heroe.recargararma(68)