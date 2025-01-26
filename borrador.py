import random

def elegir_palabra():
    palabras = ['python', 'programacion', 'juego', 'desafio', 'computadora']
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    oculta = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            oculta += letra
        else:
            oculta += '_'
    return oculta

def jugar_adivina_la_palabra():
    palabra = elegir_palabra()
    letras_adivinadas = []
    letras_incorrectas = []
    vidas = 6

    print("¡Bienvenido al juego Adivina la palabra!")
    print(f"Tienes {vidas} vidas.")

    while vidas > 0:
        print("\nPalabra:", mostrar_palabra_oculta(palabra, letras_adivinadas))
        print("Letras incorrectas:", ', '.join(letras_incorrectas))
        letra = input("Ingresa una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, ingresa una sola letra.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya ingresaste esa letra.")
            continue

        if letra in palabra:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas) == set(palabra):
                print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
                break
        else:
            letras_incorrectas.append(letra)
            vidas -= 1
            print(f"Letra incorrecta. Te quedan {vidas} vidas.")

        if vidas == 0:
            print(f"Perdiste. La palabra era: {palabra}")

if __name__ == "__main__":
    while True:
        jugar_adivina_la_palabra()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
