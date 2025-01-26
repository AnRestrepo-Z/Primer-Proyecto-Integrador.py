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
            for i, letra_nueva in enumerate(palabra_oculta):
                if letra_nueva == letra:
                    progreso[i] = letra
        else:
            intentos -=1
            print(f"la letra {letra} no está en la palabra. Te quedan {intentos} oportunidades")
        
        print("progreso: "+" ".join(progreso))

    if "_" not in progreso:
     print("\n¡Muy bien! Adivinaste la palabra 🥳")
    else:
        print("\nTus oportunidades terminaron 🙁 La palabra era {palabra_oculta}")