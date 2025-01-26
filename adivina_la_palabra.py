"""
El objetivo consiste en desarrollar el juego interactivo “adivina la palabra”. 
   
El funcionamiento esperado es el siguiente:
Al ejecutar el programa se mostrará por pantalla una palabra oculta usando tantos guiones como letras 
contiene la palabra a adivinar(la palabra a adivinar será elegida por el programa usando el módulo de 
Python random), la cantidad de vidas con las que cuenta el jugador y las cantidad de letras incorrectas 
que va ingresando.
   
Cuando el jugador ingresa una letra es necesario que se valide el dato( que sea una letra). 
Luego de validar la letra ingresada se corrobora si la letra ingresada pertenece a alguna de las letras 
de la palabra a adivinar. 

Cada vez que el jugador ingrese una letra que NO pertenece a la palabra a adivinar se restará una vida.
El juego finaliza cuando el jugador queda sin vidas, cuando adivina todas las letras de la palabra o
cuando selecciona no jugar más. Para todos los casos se debe mostrar un mensaje indicando si ganó la partida 
o si perdió. 
"""
#Usando random para que las palabras aparezcan de forma aleatoria
import random

#Definiendo función para elegir la palabra que adivinará el usuario
def adivina_la_palabra():
    #Se crea una lista de las palabras del juego
    palabras = ["cocodrilo", "hipopotamo", "elefante", "mariposa", "dinosaurio", "ornitorrinco", "camaleon"]
    palabra_oculta = random.choice(palabras) 
    progreso = ["_"],len(palabra_oculta) 
    intentos = 6

    print("Adivina la palabra! Recuerda que tienes 6 intentos")
    print(" ".join(progreso))

    while intentos >0 and "_" in progreso:
        letra = input ("\n Adivina una letra").lower

        if len(letra) !=1 or not letra.isalpha():
            print("Ingresa una sola letra por portunidad")
            continue
        elif letra in palabra_oculta:
            print(f"La letra {letra} está entre la palabra oculta!")


