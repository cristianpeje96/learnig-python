#funcion para simular los intentos de ingreso de clave en cajero automatico
#intentos permitidos 3

def cajero():
    #clave regitrada en el banco
    my_clave_banco = '2024'

    cont_attempts = 0 
    status = True
    while status:
        clave = input("Digite tu clave: ")
        if my_clave_banco == clave:
            print("Has ingresado a tu cuenta")
            print(f"intento satisfactorio: {cont_attempts}")
            cont_attempts += 1
            status = False
        else :
            if cont_attempts > 3:
                print(f"Intento {cont_attempts}: Clave incorrecta, intenta nuevamente.")
                cont_attempts += 1
            else:
                print(f"intento {cont_attempts}: clave incorrecta")
                cont_attempts += 1

            if cont_attempts >= 3:
                print("Se han agotado todos los intentos, tu cuenta se ha bloqueado")
                break
            
        
        


#clave que digito en el ATM
cajero()
