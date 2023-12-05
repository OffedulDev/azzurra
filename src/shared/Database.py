# IMPORTS
import sqlite3
from datetime import datetime

# FUNCTIONS

def get_connection():
    return sqlite3.connect("Database.db")

def get_current_date_string():
    current_date = datetime.now()
    date_string = current_date.strftime("%d-%m-%Y")

    return date_string

def get_current_date_and_hour_string():
    current_date = datetime.now()
    date_string = current_date.strftime("%d-%m-%Y %H:%M:%S")

    return date_string

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

def get_entries(table_name, conditions, approximate=False):
    connection = get_connection()
    cursor = connection.cursor()

    operator = 'LIKE' if approximate else '='
    where_clause = ' AND '.join([f'{col} {operator} ?' for col in conditions.keys()])
    params = tuple(['%' + value + '%' if approximate else value for value in conditions.values()])

    cursor.execute(f'''
        SELECT * FROM {table_name} WHERE {where_clause}
    ''', params)
    return cursor.fetchall()
