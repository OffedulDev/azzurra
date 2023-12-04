# IMPORTS
import sqlite3

# FUNCTIONS

def get_connection():
    return sqlite3.connect("Database.db")

def execute_command(command):
    connection = get_connection()
    cursor = connection.cursor()
    
    r = cursor.execute(command)
    connection.close()

    return r

def new_entry(table_name, first_name, last_name, username):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f'''
        INSERT INTO {table_name} (first_name, last_name, username)
        VALUES (?, ?, ?)
    ''', (first_name, last_name, username))
    connection.commit()
    connection.close()

def get_entry(table_name, column, value):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f'''
        SELECT * FROM {table_name} WHERE {column} = ?
    ''', (value,))
    return cursor.fetchone()