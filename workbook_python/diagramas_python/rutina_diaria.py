print("¡Bienvenido a tu rutina diaria!")
hora = input("¿Qué hora es? (HH:MM) ")

if "04:00" <= hora < "05:00":
    print("Estás levantándote temprano, ¡bien hecho!")
    respuesta = input("¿Terminaste de levantarte? (Sí/No) ")
    if respuesta.lower() == "no":
        print("Tómate tu tiempo para levantarte, no te apures.")
    else:
        print("¡Excelente! Sigue adelante con tu día.")
        hora = input("¿Qué hora es ahora? (HH:MM) ")
        
if "05:00" <= hora < "07:30":
    print("¡Hora de ir al gym!")
    respuesta = input("¿Terminaste de hacer ejercicio? (Sí/No) ")
    if respuesta.lower() == "no":
        print("Asegúrate de completar tu entrenamiento, es importante para tu salud.")
    else:
        print("¡Muy bien! Continúa con tu rutina.")
        hora = input("¿Qué hora es ahora? (HH:MM) ")

if "07:30" <= hora < "09:00":
    print("Estás llegando al trabajo o a la escuela, ¡a trabajar!")
    respuesta = input("¿Llegaste a tu destino? (Sí/No) ")
    if respuesta.lower() == "no":
        print("Sigue adelante y llega a tiempo.")
    else:
        print("¡Genial! Sigue con tus actividades diarias.")
        hora = input("¿Qué hora es ahora? (HH:MM) ")

if "09:00" <= hora < "13:00":
    print("¡Hora del desayuno y de entrar a clase!")
    respuesta = input("¿Terminaste de desayunar y de entrar a clase? (Sí/No) ")
    if respuesta.lower() == "no":
        print("Asegúrate de completar tus tareas matutinas antes de seguir adelante.")
    else:
        print("¡Muy bien! Continúa con tus actividades.")
        hora = input("¿Qué hora es ahora? (HH:MM) ")

if "13:00" <= hora < "14:00":
    print("¡Hora de almorzar!")
    respuesta = input("¿Terminaste de almorzar? (Sí/No) ")
    if respuesta.lower() == "no":
        print("Tómate tu tiempo para almorzar y disfrutar de tu comida.")
    else:
        print("¡Excelente! Continúa con tu rutina diaria.")
        hora = input("¿Qué hora es ahora? (HH:MM) ")

if "14:00" <= hora < "18:00":
    print("Continúa con tus actividades diarias.")
    respuesta = input("¿Terminaste tus actividades? (Sí/No) ")
    if respuesta.lower() == "no":
        print("Sigue adelante y completa tus tareas.")
    else:
        print("¡Muy bien! Continúa con tu día.")
        hora = input("¿Qué hora es ahora? (HH:MM) ")

if "18:00" <= hora < "21:30":
    print("¡Hora de hacer la cena y comer!")
    respuesta = input("¿Terminaste de hacer la cena y comer? (Sí/No) ")
    if respuesta.lower() == "no":
        print("asegurate de comer antes de ir a dormir")
    else: 
        print("muy bien, es hora de dormir")