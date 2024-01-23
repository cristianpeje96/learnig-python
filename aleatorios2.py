'''script que gener el lanzamiento de dos dados (1-6), y que muestre por pantalla el mensaje 
ganador cuando genere dados iguales de lo contrario el mensaje dira sigue intentando'''

#importo biblioteca para generar numeros aleatorios enteros.
from random import randint

# funcion: generar o lanzar los dos dados 
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

d = dices()
d1 = d[0]
d2 = d[1]

print("dices:", d)
print("dice 1:", d1)
print("dice 2:", d2)

if d1 == d2:   
    print("Felicitaciones eres el ganador")
else : 
    print("sigue intentando")



#print("dice1:", dice1)
#print("dice2:", dice2)
