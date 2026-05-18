#RETO EDABIT
#Crea una función que devuelva la lista de números de un rango dado. Pero para los múltiplos de tres, devuelve 'Eda' en lugar del número y para los múltiplos de cinco, devuelve 'Bit'
#Para los números que son multiplos de tres como de cinco, devuelve 'EdaBit'

def eda_bit(num1, num2):
    lista_numeros=list(range(num1,num2+1))
    #if lista_numeros[0]==0:
        #lista_numeros[0]='Eda'
    for i in range(len(lista_numeros)):
        if lista_numeros[i]%15==0:
            lista_numeros[i]='Edabit'
        elif lista_numeros[i]%3==0:
                lista_numeros[i]='Eda'
        elif lista_numeros[i]%5==0:
                lista_numeros[i]='Bit'
    return lista_numeros
    
print(eda_bit(0,10))