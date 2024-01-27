'''
bucle que genere n cantidad de numeros enteros aleatorios, el usuario debe digitar la cantidad de numeros a generar.
al finalizar debe presentar por pantalla el siguqien reporte:
-cauntos # son pares
- cuantos # son impares
- cuantos # son -
- cuantos # son +
- suma de numeros pares
- suma de numeros impares
'''
import os 
import random

os.system('clear')
def numbers_generator(cant):
    i = 1 
    pares = 0
    impares = 0
    positivo = 0 
    negativo = 0
    sum_pos = 0
    sum_neg = 0
    while i <= cant:
        num = random.randint(-10, 10)
        print(num)
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares += 1

        if num > 0 :
            positivo = positivo + 1
            sum_pos = sum_pos + num
        else:
            negativo += 1
            sum_neg += num
        i += 1
    
    print(f"Total de numeros generados: {cant}")
    print(f"Total pares generados: {pares}")
    print(f"Total inpares generados: {impares}")
    print(f"Total positivo generados: {positivo}")
    print(f"Total negativo generados: {negativo}")
    print(f"Total suma positivo generados: {sum_pos}")
    print(f"Total suma negativo generados: {sum_neg}")

    
cant_num = int(input("Qué cantidad de numeros deseas generar: "))
numbers_generator(cant_num)