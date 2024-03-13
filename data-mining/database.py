'''
dev: joan c. script 
description: config data base 
'''

# impor engine database packgae
import sqlite3
import psycopg2

#crear la conexion con la base de datos
conn = sqlite3.connect('market.db')

#create cursor objecte by conecction = permite ejecutar comandos sql
cur = conn.cursor()

#create users table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        ident_number TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
'''
#ejecutar sql (query)
cur.execute(user_table)

#save changes in data base
#conn.commit()

print("::: DATABASE MARKET HAS BEEN CREATED :::")




