"""este codigo es un juego para encontrar el tesoro peridido en una isla"""
import sys
print ("\nBIENVENIDO A LA ISLA. \n\nTu mision: \nEcontrar el tesoro, mucha suerte! \n\nTendras que tomar desiciones a lo largo de la historia para \nalcanzar tus objetivos. Pero ten cuidado, podrias morir en el proceso!. \n\n\n ")
hacia_donde = input("Ya caminaste durante una (1) hora y adelante el camino se divide en dos. Ahora tendras que decidir entre girar a la derecha O girar a la izquierda \n¿Cual eliges? " )
if hacia_donde.lower() == "derecha":
    print("Felicidades, pasaste. ")
else:
    print("lo siento, caiste en un agujero \nSe acabó el juego ")
    sys.exit()

nadar_ono = input("Ahora dime, ¿Quieres nadar al otro lado o espera? " )
if nadar_ono.lower() == "esperar":
    print("Felicidades, pasaste. ")   
else:
    print("lo siento, fuiste atacado por una tribu mientras nadabas \nSe acabo el juego ")
    sys.exit() 
    
luz_ono = input("Se está poniendo el sol, ¿quieres prender una fogata? ")
if luz_ono.lower() == "no":
    print("felicidades, pasaste. ")
else: 
    print("La tribu te vio y ahora vendran a asesinarte. \nSe acabó el juego ")
    sys.exit()
cruzar = input("hay un puente justo al frente, ¿lo vas a cruzar?")
if cruzar.lower() == "si": 
    print("felicidades, pasaste. ")
else:
    print("lo siento, el guardia te descubrió. Se acabó el juego. ")
    sys.exit() 
puerta = input("Esta es tu decision final, tienes que pensarlo muy bien. \n\nHay dos puertas grandes. Una amarilla y otra azul pero tambien estan las del fondo \n¿cual vas a elegir?")
if puerta.lower() == "amarilla":
    print("felicidades, acabas de encontrar el tesoro perdido. \nDisfrutalo! ")
elif puerta.lower() == "azul": 
    print("lo siento, fuiste deborado por bestias. Se acabó el juego.")
    sys.exit()
else: 
    print("lo siento, fuiste tragado por el vacio del espacio y ahora estas atrapado en un bucle del espacio tiempo se acabó el juego") 