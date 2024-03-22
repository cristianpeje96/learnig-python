'''
Bucle: loop, repetir una acción N veces, iteraciones (cantidad de ejecución)
Contadores (cuenta o incrementa)
acumuladores (acumulación de valores. Peje. sumar valores)
Contar valores es diferente de sumar valores
'''
# Funcion bucle para imprimir los numeros del 1 al 10 en pantalla
def list_numbers():
    #Bucle que imprime lista de numeros por pantalla
    i = 1 
    while i <= 100:
        print(i)
        i = i + 1
    print("i: ", i)

def list_numbers2():
    #Bucle que imprime lista de numeros por pantalla
    i = 1
    status = True 
    while status: #while status == true
        if i == 11:
            break
        print(i)
        i = i + 1
    print("i: ", i)

def list_numbers3():
    #Bucle que imprime lista de numeros por pantalla
    i = 1
    status = True 
    while status: #while status == true
        print(i)
        i = i + 1
        if i == 11:
            status = False
    print("i: ", i)

list_numbers3()
#list_numbers2()
#list_numbers()
