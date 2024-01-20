#Titulo del script: calculadora basica v1
#Desarrollador: Cristian Pejendino
#date: 18/01/2024

''' Description :
this calculator let you get the result of 4 basic math 
operations from two numbers (variables).'''

#INPUTS(ENTRADAS)(dos variables estaticas)
num1 = 20
num2 = 5

#PROCESS (proceso)
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#OUTPUS
print("::VERSION 1::" )
print("number 1:", num1, type(num1))
print("number 2:", num2, type(num2))
print("the addition is:", add, type(add))
print("the subtraction is:", sub, type(sub))
print("the multiplication is:", mul, type(mul))
print("the division is:", div, type(div))

print("/n")
print("::VERSION 2::" )
print("number 1:", num1 )
print("number 2:", num2)
print("the addition is:", num1+num2)
print("the subtraction is:", num1-num2)
print("the multiplication is:", num1*num2)
print("the division is:", num1/num2)