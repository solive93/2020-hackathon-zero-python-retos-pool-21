from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    
    if player == ai:
        return 'Empate!'
    if (player == "piedra") and (ai == "papel"):
        return 'Perdiste!'
    if player == "tijeras" and ai == "piedra":
        return 'Perdiste!'
    if player == "papel" and ai == "tijeras":
        return 'Perdiste!'
    return 'Ganaste!'
    
  

# Entry Point
def Game():
    player = print("Escoge: piedra, papel o tijera? ").lower()
    ai = options.randint(0, 2).lower()
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

