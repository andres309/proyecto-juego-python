import random

vidas = 3
vidas_pc =3

print("------------------------------------------")
print("--  Bienvenido a Piedra, Papel o tijera --")
print("-- ---------------------------------------")
print()
print(":) REGLAS :)")
print("1.AL pc y a ti se le asignaran 3 vidas ")
print("si ganas una partida, ademas ganaras ")
print("una vida, y al pc se le resta una, y")
print("viceversa.")
print("2. si eliges un numero que no asigne un")
print("ataque automaticamente perderas esa partida.")
print("3.para ganar debes vencer al PC hasta que")
print("se le acaben las vidas")
print("-_- vivir o morir has tu eleccion -_-")
print()

print()
print("######### MENSAJE DE 'PC' PARA TI #########")
print()
print("(◣∀◢)ψ acabare contigo inutil (◣∀◢)ψ")
print()
print("###########################################")
print()
print()


while vidas > 0 and vidas_pc >0:
    print("Realiza tu elección a partir de los números")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("0. Salir")
    

    elec_juga = int(input("Digite su ataque: "))
    print()

    # tipos de ataques
    piedra = "piedra"
    papel = "papel"
    tijera = "Tijera"
    nulo = "Nulo"

    # estableciendo el tipo de ataque para el jugador según el número de elección
    if elec_juga == 1:
        tipo_ataque_jugador = piedra
    elif elec_juga == 2:
        tipo_ataque_jugador = papel
    elif elec_juga == 3:
        tipo_ataque_jugador = tijera
    else:
        tipo_ataque_jugador = nulo
        

    # estableciendo el ataque de PC
    elec_pc = random.randint(1, 3)

    if elec_pc == 1:
        tipo_ataque_pc = piedra
    elif elec_pc == 2:
        tipo_ataque_pc = papel
    elif elec_pc == 3:
        tipo_ataque_pc = tijera
    else:
        tipo_ataque_pc = nulo

    # Jugando
    if elec_pc == elec_juga:
        print(f"PC elige {tipo_ataque_pc} tu eliges {tipo_ataque_jugador} EMPATE ")
        print()
    elif (elec_juga == 2 and elec_pc == 1) or (elec_pc == 2 and elec_juga == 3) or (elec_pc == 3 and elec_juga == 1):
        print(f"PC elige {tipo_ataque_pc} tu eliges {tipo_ataque_jugador} GANASTE ")
        print()
        vidas += 1 # aumentando una vida si gana el jugador
        vidas_pc-=1
    else:
        print(f"PC elige {tipo_ataque_pc} tu eliges {tipo_ataque_jugador} PERDISTE ")
        print()
        vidas -= 1 # disminuyendo una vida si pierde el jugador
        vidas_pc +=1
    print(f"Tienes {vidas} vidas")
    print()
    print(f"pc tine {vidas_pc} vidas")
    print()
    
if vidas ==0:
    print("Se acabaron tus vidas. El juego ha terminado.")
    print()
    print("(◣∀◢)ψ Te dije que  acabaria contigo dulces pesadillas (◣∀◢)ψ ")
else:
    print("felicidades ganaste el juego")
    print()
    print("(◣∀◢)ψ ganaste esta, pero en la proxima te destruire (◣∀◢)ψ ")
    print()
    print()
