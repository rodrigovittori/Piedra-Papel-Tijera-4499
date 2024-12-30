"""
Primera Actividad Módulo 3: Proyecto - Piedra-Papel-Tijeras
Versión: 0.2.0

Link al repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/blob/main/main.py
Hitorial del repo: https://github.com/rodrigovittori/Piedra-Papel-Tijera-4499/commits/main/main.py
Link al proyecto final (en HUB): ** todavía NO publicado **
-------------------------------------

Paso Nº 2: Creamos el bucle principal:
    > agregamos una nueva variable de control, de tipo bool (verdadero o falso) llamada seguir_jugando
    > agregamos un bucle while(seguir_jugando)
      y dentro de éste (bucle) un check para validar si el usuario desea continuar o no

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
    # Paso Final: PREGUNTAMOS SI QUIERE SEGUIR JUGANDO

    seguir_jugando = input("\n ¿Desea seguir jugando? (S/N): ")

    if ('S' in seguir_jugando) or ('s' in seguir_jugando) or (seguir_jugando == ""):
        seguir_jugando = True
    
    else:
        seguir_jugando = False
        print("JUEGO FINALIZADO")