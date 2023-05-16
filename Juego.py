import random

def jugabilidad(jugador1,jugador2,opciones,marcador):
    ganador={'spock':{'tijera':'Spock rompe la tijera','piedra':'Spock vaporiza la piedra'},
             'tijera':{'papel':'tijera corta papel','lagarto':'tijera decapita al lagarto'},
             'papel':{'piedra':'papel envuelve a piedra','spock':'papel desautoriza a spock'},
             'piedra':{'lagarto':'piedra aplasta al lagarto','tijera':'piedra aplasta las tijeras'},
             'lagarto':{'spock':'lagarto envenena a spock','papel':'lagarto se come el papel'}}
    if jugador1 not in opciones or jugador2 not in opciones:
        print("Uno de los jugadores no eligio una opcion correcta")
    else:
        if jugador1==jugador2:
            print("empate")
        elif jugador1 in ganador[jugador2].keys():
            print(f"perdiste {ganador[jugador2][jugador1]}")
            marcador[1]+=1
        else: 
            print(f"ganaste {ganador[jugador1][jugador2]}")
            marcador[0]+=1
    return marcador
            
def contar_puntos(marcador):
    if marcador[0]==marcador[1]:print(f"el marcador es igual por {marcador[0]} puntos, es un empate")
    elif marcador[0]>marcador[1]:print(f"el jugador1 gana {marcador[0]} a {marcador[1]} al jugador2")
    else :print(f"el jugador2 gana {marcador[1]} a {marcador[0]} al jugador1")

opciones=['piedra','papel','tijera','spock','lagarto']
marcador=[0,0]
while True:
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║      Juego de Piedra, Papel, Tijeras lagarto o Spock      ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("Por favor, elige una opción:")
    print("Piedra")
    print("Papel")
    print("Tijera")
    print("Lagarto")
    print("Spock")
    print("Salir\n")
    jugador1= input("digite la opcion: ").lower()
    maquina=random.choice(opciones)
    if jugador1=='salir':
        contar_puntos(marcador)
        print("Fin del juego")
        break      
    else:
        jugabilidad(jugador1,maquina,opciones,marcador)
        contar_puntos(marcador)

        


