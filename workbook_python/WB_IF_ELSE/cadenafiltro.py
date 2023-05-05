"""este programa filtra palabras segun la letra determinada"""
palabras = input("ingrese una lista de palabras separadas por una coma (,): ")
letra = input("ingrese la letra incial para filtrar en la lista ")
lista_palabras = palabras.split(",")
for palabra in lista_palabras:
    if palabra.strip().lower().startswith(letra):
        print(palabra)
#el comando strip elimina los espacios en blanco, el comando lower convierte las letras en minuscula y el comando startswith verifica la inicial