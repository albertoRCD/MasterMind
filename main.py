'''

Juego: Muertos y heridos (MasterMind)

'''

import random
import os

digitos = "0123456789"
numero = ""
muertos = 0
heridos = 0
intento = None
intentos = []
salir = False

#Presentación del programa

os.system("cls")

print("***********************************************")
print("*                                             *")
print("*         Juego Muertos y Heridos             *")
print("*           Tienes 15 intentos                *")
print("*                                             *")
print("*         Pulsa Enter para empezar            *")
print("*                                             *")
print("***********************************************")

input()

#Generamos el número aleatorio a adivinar

while len(numero) < 4:
    digito = random.choice(digitos)
    if digito not in numero:
        numero += digito

#Bucle principal mientras no se acierte numero

while True:

    os.system("cls")

    print("***********************************************")
    print("*            MUERTOS Y HERIDOS                *")
    print("***********************************************")
    print("*     NUMERO         -         M   -   H      *")
    print("*  -----------       -       --------------   *")

    #Mostramos todos los intentos que el usuario ha hecho hasta el momento

    for i in range(len(intentos)):
        print(f"    {intentos[i][0]}             -          {intentos[i][1]}  -  {intentos[i][2]}")
        print("*                                        *")


    #Comprobación de si se ha ganado, y salida del programa en ese caso.

    if numero == intento:
        print("*         Has acertado el número. Has ganado.     *")
        print(f"*       Has necesitado {len(intentos)} intentos     *")

    #Comprobación de los intentos, y salida del programa si agotados

    if len(intentos) >= 15:
        print("*    Has agotado los intentos. Has perdido.     *")
        print(f"*             El número era: {numero}          *")
        break

    #Bucle para que el usuario elija un número correcto

    while True:
        intento = input("=> Introduce intento ('q' para salir): ")
        if intento == 'q':
            salir = True
            break
        elif len(intento)< 4 or len(intento)>4:
            print("Introduce un número de 4 dígitos")
        elif intento[0] not in digitos or intento[1] not in digitos or intento[2] not in digitos or \
                intento[3] not in digitos:
            print("Introduce solo números del 0 al 9")
        elif intento[0] == intento[1] or intento[0] == intento[2] or intento[0] == intento[3] or \
            intento[1] == intento[2] or intento[1] == intento [3] or intento[2] == intento[3]:
            print("No se puede repetir número, inténtalo de nuevo")
        else:
            break

    # Si la bandera salir es True salimos del programa

    if salir:
        print(f"La solución era: {numero}")

    #Bucle para comprobar el número de muertos y heridos

    for i in range(4):
        if intento[i] in numero:
            if intento[i] == numero[i]:
                muertos += 1
            else:
                heridos +=1

    #Añadimos el intento y su resultado a la lista de intentos

    intentos.append([intento, muertos, heridos])

    #Reiniciamos las variables a cero para nuevo intento

    muertos = 0
    heridos = 0