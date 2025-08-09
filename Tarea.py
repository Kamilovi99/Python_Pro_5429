import random

bot = random.randint(0, 100)
player = int(input("inserta un número del 0 al 100:"))

if player == bot: 
    print("¡Felicidades ganastes!")
    game = input("¿Quieres continuar?(si/no):")

else:
    print("Intentalo otra vez")
    print("¿Quieres intentarlo continuar?")
    game = input("¿Quieres continuar?(si/no):")

if game == "si":
    bot = random.randint(0, 100)
    player = int(input("inserta un número del 0 al 100:"))

    if player == bot: 
        print("¡Felicidades ganastes!")
        game = input("¿Quieres continuar?(si/no):")

    else:
        print("Intentalo otra vez")
        print("¿Quieres intentarlo continuar?")
        game = input("¿Quieres continuar?(si/no):")

elif game == "no":
    exit