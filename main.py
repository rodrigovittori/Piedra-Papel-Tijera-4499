"""
Primera Actividad Módulo 3: Proyecto - Piedra-Papel-Tijeras
Versión: 1.0.1

Link al repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/blob/main/main.py
Hitorial del repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/commits/main/main.py
Link al proyecto final (en HUB): https://hub.kodland.org/project/337200
-------------------------------------

REGLAS:

Las reglas son sencillas: Los jugadores eligen simultáneamente uno de los tres signos: piedra, papel o tijera. El ganador se determina según las siguientes reglas: 

1.    El papel le gana a la piedra (“El papel envuelve a la piedra”).

2.    La piedra le gana a la tijera (“La piedra destruye a la tijera”).

3.    La tijera le gana al papel (“La tijera corta el papel)


Paso Nº 1: Creamos variables: 
    > contadoras: ronda_actual; puntaje_jugador, puntaje_compu y empates;

Paso Nº 2: Creamos el bucle principal:
    > agregamos una nueva variable de control, de tipo bool (verdadero o falso) llamada seguir_jugando
    > agregamos un bucle while(seguir_jugando)
      y dentro de éste un check para validar si el usuario desea continuar o no

Paso Nº 3: Pedir al Jugador su elección (piedra, papel o tijera)
    > Creamos una nueva variable (dentro del bucle) -> opcion_jugador
    > Pedimos su valor con input() y lo convertimos a int()
        > 1) Piedra
        > 2) Tijeras
        > 3) Papel

    > Creamos un bucle para verificar que la opción ingresada sea válida (opcion_jugador >= 0) and (opcion_jugador <= 3)
        > Si el valor NO es válido, lo solicitamos nuevamente
        > En cambio, si es válido, convertimos ese valor a su equivalente en texto:
            > 1: "Piedra" / 2: "Tijeras" / 3: "Papel"

Paso Nº 4: Generamos con random.randint(1-3) la respuesta de la computadora y la almacenamos en una nueva variable
           llamada opcion_compu; luego, la reemplazamos por el texto equivalente

Paso Nº 5: Evaluamos el resultado de la ronda. La consigna indica que debemos seguir el órden:
            > empate -> victoria (jugador) -> else: derrota (jugador)

Pasos Nº 6-9: Paso 6: Sumar puntajes en cada ronda según el resultado
                      > agregamos contador += 1 en cada caso de nuestro if-elif-else
                        p/ los casos de empate, victoria y derrota

              Paso 7: Mostrar mensajes de victoria/derrota/empate
                      > ya hecho

              Paso 8: Mostramos puntuación actual al comienzo y fin de cada ronda
                      > agregamos dos prints:
                          > El primero ANTES de decidir
                          > El segundo DESPUES de decidir

                      > modificamos el código para que en lugar de mostrar el mensaje con un print
                        lo almacene y lo muestre después

                      > agregamos un mensaje extra al finalizar el juego
                      
              Paso 9: Agregar suspenso antes de mostrar la elección de la computadora
                      > importamos la librería time
                      > agreramos una pausa con time.sleep(3) antes de mostrar la elección del bot

############################################################################

 Tareas: Paso 10: Piensa en cómo podrías enseñarle a la computadora para que le gane al jugador más seguido. ¿Te animas?
         HW: Modificar el programa para que sea una lucha entre bots y nos pregunte cada x cant. de rondas si deseamos
             detener la simulación
"""

import random
import time

""" ··· [ Variables ] ··· """
puntaje_jugador = 0
puntaje_compu = 0
empates = 0

ronda_actual = 0
seguir_jugando = True
""" ····················· """

"""   ###################
     # BUCLE PRINCIPAL #
    ###################    """

while (seguir_jugando):

    """ > Paso Nº 1: Pedir al jugador su elección """
    opcion_jugador = 0

    while ((opcion_jugador <= 0) or (opcion_jugador > 3)):
        opcion_jugador = int(input("\n Que eliges? \n (1) Piedra (2) Tijeras (3) Papel \n >"))

    # *************************** #

    """ > Paso Nº 2: Calcular la elección de nuestro bot / IA """
    opcion_compu = random.randint(1, 3)
    ronda_actual += 1

    # *************************** #

    """ > Paso Nº 3: Configuramos el texto """

    # Convertimos el valor ingresado por el Usuario a texto:

    if (opcion_jugador == 1):
        opcion_jugador = "Piedra"
            
    elif (opcion_jugador == 2):
        opcion_jugador = "Tijeras"
            
    elif (opcion_jugador == 3):
        opcion_jugador = "Papel"
        
    else:
        opcion_jugador = "VALOR NO VALIDO"

    # Convertimos el valor seleccionado por el Bot a texto:

    if (opcion_compu == 1):
        opcion_compu = "Piedra"
            
    elif (opcion_compu == 2):
        opcion_compu = "Tijeras"
            
    elif (opcion_compu == 3):
        opcion_compu = "Papel"
        
    else:
        opcion_compu = "VALOR NO VALIDO"

    #########################################################
    
    time.sleep(3)

    print("________________________________________________________________________")
    print(" RONDA #", ronda_actual, " | ELECCION JUGADOR: ", opcion_jugador, " | ELECCION PC: ", opcion_compu)

    #########################################################

    """ Paso Nº 4: DETERMINAR RESULTADO DE RONDA: """
    resultado_ronda = ""

    ## CASO 1: EMPATE
    if(opcion_jugador == opcion_compu ):
        resultado_ronda = "\n" + "Es un empate :/"
        empates += 1

    ## CASO 2: VICTORIA!
    elif( ((opcion_jugador == "Piedra")  and (opcion_compu == "Tijeras")) or
          ((opcion_jugador == "Papel")   and (opcion_compu == "Piedra"))  or
          ((opcion_jugador == "Tijeras") and (opcion_compu == "Papel")) ):
        resultado_ronda = "\n" + "¡HAS GANADO! :D"
        puntaje_jugador += 1

    ## CASO 3: DERROTA :(
    else:
        resultado_ronda = "\n" + "Has sido derrotado :("
        puntaje_compu += 1

    """ * Espacio para insertar texto * """
    
    print("JUGADOR: ", opcion_jugador)
    print("COMPU: ", opcion_compu)

    #########################################################

    """ Paso Nº 5: MOSTRAR RESULTADO DE RONDA: """
    
    print("\n________________________________________________________________________")
    print(resultado_ronda)
    print("\n________________________________________________________________________")
    print(" RONDAS: ", ronda_actual, " | Puntuacion Jugador: ", puntaje_jugador, " | Puntuacion PC: ", puntaje_compu, " | Empates: ", empates)
        
    #########################################################
    
    # Paso Final: PREGUNTAMOS SI QUIERE SEGUIR JUGANDO

    seguir_jugando = input("\n ¿Desea seguir jugando? (S/N): ")

    if ('S' in seguir_jugando) or ('s' in seguir_jugando) or (seguir_jugando == ""):
        seguir_jugando = True
    
    else:
        seguir_jugando = False

###### JUEGO FINALIZADO ######
print("________________________________________________________________________")
print("\n                            RESULTADO FINAL:                            ")
print("________________________________________________________________________")
print(" RONDAS: ", ronda_actual, " | Puntuacion Jugador: ", puntaje_jugador, " | Puntuacion PC: ", puntaje_compu, " | Empates: ", empates)
print("\n\n ¡Gracias por jugar!")