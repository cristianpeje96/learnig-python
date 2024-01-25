'''

'''
import os
os.system("clear")

def calculator(x, y, z):
    if z == '1' :
        ans = x + y
        return x + y
    elif z == '2':
        return x - y
    elif z == '3' :
        return x * y
    elif z == '4' :
        if y == 0:
            return 'No es posible dividir entre cero'
        else :
            return x / y
    elif z == '5' :
        if y == 0:
            return x+y, x-y, x*y,'No es posible dividir entre cero'
        else :
            return x+y, x-y, x*y, x/y
    else :
        print(":::opcion invalida:::")
        return 'fail, invalid option'

n1 = float(input("Ingrese primer valor:"))
n2 = float(input("Ingrese segundo valor:"))

print(":::: MENU CALCULADORA ::::")
print("[1]. Sumar")
print("[2]. Restar")
print("[3]. Multiplicar")
print("[4]. Dividir")
print("[5]. Todas")
opc = input("Digite una opcion del menu:")

if opc == '1' or opc == '2' or opc == '3' or opc == '4' :
    ans = calculator(n1, n2, opc)
    print("Resultado:" , ans)
elif opc == 5:
    ans = calculator(n1, n2, opc)
    print("suma:", ans[0])
    print("resta:", ans[1])
    print("multiplicacion:", ans[2])
    print("division:", ans[3])

#print("resultado", calculator(n1, n2, opc))