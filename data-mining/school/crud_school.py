
from school_db import conn, cur
import os
import bcrypt

status_menu = True
global status_op

def create_country(op):
        os.system('clear') 
        print("::: CREAR NUEVO PAÍS :::")
        name = input("Nombre del país: ")
        abrev = input("Abreviatura: ")
        descrip = input("Descripción: ")
        # Insertar nuevo país en la tabla
        cur.execute("INSERT INTO countries (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, datetime('now'), datetime('now'))", (name, abrev, descrip))
        conn.commit()
        print("::: País creado exitosamente :::")
        input("Presiona Enter para continuar...")

def create_department(op):
    os.system('clear')

    name = input("Ingrese el nombre del departamento: ")
    abrev = input("Ingrese la abreviatura del departamento: ")
    descrip = input("Ingrese la descripción del departamento: ")
    cur.execute("SELECT * from countries")
    print(cur.fetchall)
    id_country = input("Ingrese el ID del país al que pertenece el departamento: ")
    cur.execute("INSERT INTO departments (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_country))
    conn.commit()
    print("Registro de departamento creado con éxito.")

    os.system('pause')
    menu()

def create_city(op):
    os.system('clear')

    name = input("Ingrese el nombre de la ciudad: ")
    abrev = input("Ingrese la abreviatura de la ciudad: ")
    descrip = input("Ingrese la descripción de la ciudad: ")
    cur.execute("SELECT * from departments")
    print(cur.fetchall)
    id_dept = input("Ingrese el ID del departamento al que pertenece la ciudad: ")
    cur.execute("INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)", 
                (name, abrev, descrip, id_dept))
    conn.commit()
    print("Registro de ciudad creado con éxito.")

    os.system('pause')
    menu()

def create_identification_type(op):
    os.system('clear')

    name = input("Ingrese el nombre del tipo de identificación: ")
    abrev = input("Ingrese la abreviatura del tipo de identificación: ")
    descrip = input("Ingrese la descripción del tipo de identificación: ")
    cur.execute("INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (name, abrev, descrip))
    conn.commit()
    print("Registro de tipo de identificación creado con éxito.")

    os.system('pause')
    menu()

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())
def create_persons(op):

        #create a new person
        os.system('clear')

        print("::: REGISTRAR :::")
        fname = input("Ingrese el nombre de la nueva persona: ")
        lname = input("Ingrese el apellido de la nueva persona: ")
        typid = input("Ingrese el tipo de identificación: ")
        idennum = input("Ingrese el número de identificación: ")
        idexpcity = input("Ingrese el ID de la ciudad de expedición:")
        address = input("Ingrese la dirección de la nueva persona: ")
        mobile = input("Ingrese el número de teléfono móvil: ")
        id_users = input("Ingrese el ID del usuario relacionado: ")

        new_persons = '''
                INSERT INTO persons 
                (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_users, created_at, updated_at) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
            '''
        cur.execute(new_persons, (fname, lname, typid, idennum, idexpcity, address, mobile, id_users))   
        conn.commit()

        print("::: Persona creada exitosamente. :::")
        os.system('pause')
        menu()

def create_student(op):
    os.system('clear')

    code = input("Ingrese el código del estudiante: ")
    id_persons = input("Ingrese el ID del estudiante: ")
    cur.execute("INSERT INTO students (code, id_persons, status, created_at, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (code, id_persons, 0))  # Estado predeterminado
    conn.commit()
    print("Registro de estudiante creado con éxito.")

    os.system('pause')
    menu()

def create_users(op):
        os.system('clear')

        print("::: REGISTRAR TU CORREO Y CONTRASEÑA :::")
        email = input("Ingrese el correo electrónico: ")
        passwd = input("Ingrese la contraseña: ")
        passwd_hashed = hash_password(passwd)

        new_user = '''
            INSERT INTO users 
            (email, password, status, created_at, updated_at, deleted_at) 
            VALUES (?, ?, ?, datetime('now'), datetime('now'), NULL)
        '''

        cur.execute(new_user, (email, passwd_hashed, True))
        conn.commit()

        print("::: Usuario creado exitosamente. :::")
        os.system('pause')
        menu()
  

#menu general
def menu():
        
        global opt
        status_opt = True
        while status_menu: 
            os.system('clear')
            print("::::::::::::::::::::::::::::::")
            print("::::::    MENU GENERAL  ::::::")
            print("::::::::::::::::::::::::::::::")
            print("[1]. create_country")
            print("[2]. create_department")
            print("[3]. create_city")
            print("[4]. create_identification_type")
            print("[5]. create_persons")
            print("[6]. create_student")
            print("[7]. create_users")
            print("[8]. Salir")
            
            while status_opt:
                opt = input("Presione una opción: ")
                if opt < '1' or opt > '8':
                    print("**** Opción no válida, inténtelo de nuevo. ****")
                else :
                    status_opt = False

            if opt == '1':
                create_country(opt)
            elif opt == '2':
                create_department(opt)
            elif opt == '3':
                create_city(opt)
            elif opt == '4':
                create_identification_type(opt)
            elif opt == '5':
                create_persons(opt)
            elif opt == '6':
                create_student(opt)
            elif opt == '7':
                create_users(opt)
            elif opt == '8':
                print("::: Vuelve pronto :::")
                exit()
        
menu()  
#Close connection
conn.close()