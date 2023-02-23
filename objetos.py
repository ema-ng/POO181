
#1. importar la clase 

from personaje import *

#2.solicitar atributos para el objeto
 
print("")
print("###solicitud de datos del heroe ###")
esph=input("escribe la especie del heroe")
nomh=input("escribe el nombre del heroe")
alth=float(input("escribe la altura del heroe"))
balash=int(input("cuantas balas se recargaran al heroe"))

print("")
print("###solicitud de datos del villano ###")
espv=input("escribe la especie del villano")
nomv=input("escribe el nombre del villano")
altv=float(input("escribe la altura del villano"))
balasv=int(input("cuantas balas se recargaran al villano"))

#3.creamos 2 objetos

heroe = personaje(esph,nomh,alth)
villano = personaje(espv,nomv,altv)

#4. acceder a sus atributos y metodos decada obj

print("")
print("## atributos y metodos del heroe ## ")
print("el personaje pertenece a la raza: " + heroe.especie)
print("se llama: " + heroe.nombre)
print("mide: " + str(heroe.altura) + " metros")
print("")

heroe.correr(True)
heroe.lanzargranada
heroe.recargararma(balash)

print("")
print("## atributos y metodos del heroe ## ")
print("el personaje pertenece a la raza: " + villano.especie)
print("se llama: " + villano.nombre)
print("mide: " + str(villano.altura) + " metros")
print("")

villano.correr(False)
villano.lanzargranada
villano.recargararma(balasv)