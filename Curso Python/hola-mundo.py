meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "FR": "Significa que tienes razon, o que algo es verdad",
            "XD": "Una forma de expresar risa, similar a 'LOL'",
            "CF":"Tiene muchisimos significados,el mas comun es Cambia formas otro es XD"
            }

for i in range (5): #bucle
    word = input("Ingrese una palabra para buscar su significado(¡¡¡¡EN MAYUSCULAS!)!):")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("La palabra no se encuentra en el diccionario.")

#["CRINGE", "LOL", "FR", "XD", "CF"]