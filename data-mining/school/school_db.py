#Import engine database package
import sqlite3

#Create a database connnection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor object by conection => Let us execute sql commands or operations (Query)
cur = con.cursor()

#Create users table
users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id_users INTEGER PRIMARY KEY, 
        email TEXT(100) UNIQUE NOT NULL,
        password TEXT(250) NOT NULL,
        status BOOLEAN NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATATIME NULL
    );
'''
#Create persons table
persons_table = '''
    CREATE TABLE IF NOT EXISTS persons (
        id_persons INTEGER PRIMARY KEY,
        first_name TEXT(50) NOT NULL,
        last_name TEXT(50) NOT NULL, 
        id_ident_type INTEGER NOT NULL,
        ident_number TEXT(15) NOT NULL,
        id_exp_city INTEGER NOT NULL,
        address TEXT(150) NOT NULL,
        mobile TEXT(50) NOT NULL,
        id_users INTEGER NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME NULL,
        FOREIGN KEY (id_users) REFERENCES users(id_users)
        FOREIGN KEY (id_ident_type) REFERENCES identification_types(id_ident_type)
        FOREIGN KEY (id_exp_city) REFERENCES cities(id_exp_city)
    );
'''
#Create students table
students_table = '''
    CREATE TABLE IF NOT EXISTS students (
        id_students INTEGER PRIMARY KEY, 
        code TEXT(50) NOT NULL,
        id_persons INTEGER NOT NULL,
        status BOOLEAN NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATATIME NULL,
        FOREIGN KEY (id_persons) REFERENCES persons(id_persons)
    );
'''
#Create identification_types table
identification_types_table = '''
    CREATE TABLE IF NOT EXISTS identification_types (
        id_ident_type INTEGER PRIMARY KEY, 
        name TEXT(50) NOT NULL,
        abrev TEXT(10) NOT NULL,
        descrip TEXT(100) NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATATIME NULL
    );
'''
#Create cities table
cities_table = '''
    CREATE TABLE IF NOT EXISTS cities (
        id_exp_city INTEGER PRIMARY KEY, 
        name TEXT(100) NOT NULL,
        abrev TEXT(10) NOT NULL,
        descrip TEXT(10) NOT NULL,
        id_dept INTEGER NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATATIME NULL,
        FOREIGN KEY (id_dept) REFERENCES departments(id_dept)
    );
'''
#Create departments table
departments_table = '''
    CREATE TABLE IF NOT EXISTS departments (
        id_dept INTEGER PRIMARY KEY, 
        name TEXT(100) NOT NULL,
        abrev TEXT(10) NOT NULL,
        descrip TEXT(10) NOT NULL,
        id_country INTEGER NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATATIME NULL,
        FOREIGN KEY (id_country) REFERENCES countries(id_country)
    );
'''
#Create countries table
countries_table = '''
    CREATE TABLE IF NOT EXISTS countries (
        id_country INTEGER PRIMARY KEY, 
        name TEXT(100) NOT NULL,
        abrev TEXT(10) NOT NULL,
        descrip TEXT(10) NOT NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATATIME NULL
    );
'''

#Execute SQL (Query)
cur.execute(users_table)
cur.execute(persons_table)
cur.execute(students_table)
cur.execute(identification_types_table)
cur.execute(cities_table)
cur.execute(departments_table)
cur.execute(countries_table)

#Save changes in database => Push to database
con.commit()

print("::: Database market has been created :::")

#Close connection
#con.close()