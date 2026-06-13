# FUNCIONES BATALLA
import random
import time
from funcionesrpg import *

def loboferoz():
	enemigo1: ["Lobo Feroz", 150, "Arañazo", "Mordida"]
	return enemigo1
	
def guardian():
	enemigo2: ["Guardian de Piedra", 200, "Martillazo", "Pisoton"]
	
def bandido():
	enemigo3: ["Bandido", 120, "Facazo", "Navajazo"]
	
def jugador():
	prota: ["Jugador", 150, "Punzante", "Puntazo"]
	
def batalla(opcion2):
	
	if opcion2 == 1:
		escribir("""
	Un gruñido sordo hace eco entre los árboles.
	Dos ojos amarillos y brillantes te clavan la mirada.
	Un imponente Lobo Salvaje muestra sus colmillos ensangrentados.
	El depredador ha encontrado a su presa!
	""")
