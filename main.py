"""
Primera Actividad Módulo 3: Proyecto - Piedra-Papel-Tijeras
Versión: 0.4.0

Link al repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/blob/main/main.py
Hitorial del repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/commits/main/main.py
Link al proyecto final (en HUB): ** todavía NO publicado **
-------------------------------------

Paso Nº 4: Generamos con random.randint(1,3) la respuesta de la computadora y la almacenamos en una nueva variable
           llamada opcion_compu; luego, la reemplazamos por el texto equivalente

           > importar random
           > creamos variable opcion_compu y le asignamos un valor random(1-3)
           > converimos ese valor random (int) a texto (str)
"""
import random

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

    """ > Paso Nº 2: Calcular la elección de nuestro bot / IA """
    opcion_compu = random.randint(1, 3)
    ronda_actual += 1

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

    """ * Lugar para insertar suspenso* """

    print("ELECCION JUGADOR: ", opcion_jugador)
    print("ELECCION COMPU: ", opcion_compu)
    
    # Paso Final: PREGUNTAMOS SI QUIERE SEGUIR JUGANDO

    seguir_jugando = input("\n ¿Desea seguir jugando? (S/N): ")

    if ('S' in seguir_jugando) or ('s' in seguir_jugando) or (seguir_jugando == ""):
        seguir_jugando = True
    
    else:
        seguir_jugando = False
        print("JUEGO FINALIZADO")