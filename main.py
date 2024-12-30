"""
Primera Actividad Módulo 3: Proyecto - Piedra-Papel-Tijeras
Versión: 0.3.0

Link al repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/blob/main/main.py
Hitorial del repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/commits/main/main.py
Link al proyecto final (en HUB): ** todavía NO publicado **
-------------------------------------

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
"""

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

    # Convertimos el valor ingresado por el Usuario a texto:

    if (opcion_jugador == 1):
        opcion_jugador = "Piedra"
            
    elif (opcion_jugador == 2):
        opcion_jugador = "Tijeras"
            
    elif (opcion_jugador == 3):
        opcion_jugador = "Papel"
        
    else:
        opcion_jugador = "VALOR NO VALIDO"

    """ *** ELIMINAR DESPUES """
    print(" > Elegiste: ", opcion_jugador)
    """ *** ELIMINAR DESPUES """
    
    # Paso Final: PREGUNTAMOS SI QUIERE SEGUIR JUGANDO

    seguir_jugando = input("\n ¿Desea seguir jugando? (S/N): ")

    if ('S' in seguir_jugando) or ('s' in seguir_jugando) or (seguir_jugando == ""):
        seguir_jugando = True
    
    else:
        seguir_jugando = False
        print("JUEGO FINALIZADO")