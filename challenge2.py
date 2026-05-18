#FUNCION DE TARTAMUDEO
#Escribe una función que tartamudee una palabra como si alguien estuviera luchando por leerla. Las dos primeras letras se repiten dos veces con puntos suspensivos... y un espacio después de cada una, y luego la palabra se pronuncia con un signo de interrogación ?.
def stutter (word):
    #return f"{word[:2]}... {word[:2]}... {word}?"
    return word[:2]+"... "+word[:2]+"... "+ word+"?"
print(stutter('amigo'))