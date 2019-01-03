
pokemon_elegido = input("¿Contra qué Pokemos quieres combatir? (Squirtle / Charmander / Bullbasaur): ")

vida_pikachu = 100

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_pokemon = 7
    nombre_pokemon = "Charmander"

elif pokemon_elegido == "Bullbasaur":
    vida_enemigo = 100
    nombre_pokemon = "Bullbasaur"
    ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo >0:
    ataque_elegido = input("¿Qué ataque vamo a usar? (Chispazo / Bola Voltio)")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola Voltio":
        vida_pikachu -= 12

    print("La vida del {} ahora es de {}".format(nombre_pokemon, vida_enemigo) )

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has Ganado!")

elif vida_pikachu <= 0:
    print("¡Has Perdido!")

print("el combate a terminado")