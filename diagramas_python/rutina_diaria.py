hora = int(input("Que hora es? "))
alarma = True
if hora < 4:
    print ("podemos seguir durmiendo")
else: 
     respuesta_alarma = input("la alarma suena a las 4am, ya sonó la alarma? ")
     
if respuesta_alarma.lower() == "si":
    respuesta_alarma = True
else:
    respuesta_alarma = False
    print ("no es hora de levantarnos ")
if respuesta_alarma:
    print("es hora de levantarnos ") 
 
 