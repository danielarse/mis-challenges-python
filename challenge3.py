#INVERTIR COLORES
#Crea una función que invierta los 'rgb' valores de una tupla dada.
def color_invert(rgb):
    return (255-rgb[0],255-rgb[1],255-rgb[2])
print('Orden invertido de rgb es: ', color_invert((26,30,10)))
print(color_invert((0, 0, 0)))      
print(color_invert((165, 170, 221)))
print(color_invert((110, 140, 241)))
print()