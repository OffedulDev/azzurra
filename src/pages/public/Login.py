# IMPORTS
import sqlite3
import shared.Database as Database
import shared.Storage as Storage
import time

from uuid import uuid4
from nicegui import ui

# VARS
users = []

# FUNCTIONS
def login_user(username):
    if Storage.get_from_storage("token"): ui.notify("Impossibile impostare token d'accesso; token già esistente", close_button="OK", type="warning"); return
    
    user_data = Database.get_entry("accounts", "username", username)
    user_type = user_data[2]

    t = uuid4()
    users.append({
        "TOKEN": t,
        "USERNAME": username,
        "TYPE": user_type
    })

    Storage.write_to_storage("token", t)

def get_user_data():
    if is_user_logged_in() == False: return
    token = Storage.get_from_storage("token")

    for user in users:
        if user["TOKEN"] == token:
            return user
    
    return None

def is_user_logged_in():
    token = Storage.get_from_storage("token")
    if token == None: return False

    for user in users:
        if user["TOKEN"] == token:
            return True
    
    Storage.write_to_storage("token", None)
    return False

def logout():
    if is_user_logged_in() == False: ui.notify("Utente già sloggato vuole sloggare?", close_button="OK", type="warning"); return
    ui.notify("Uscendo dall'account...", type="ongoing")
    
    user_data = get_user_data()
    users.pop(users.index(user_data))
    Storage.write_to_storage("token", None)

    ui.notify("Sei uscito correttamente!", type="positive")
    ui.open("/login")
    
    

def validate_login(Username, Password):
    Entry = Database.get_entry("accounts", "username", Username)

    if Entry == None: ui.notify(message="Credenziali invalide.", close_button="OK", type="negative"); return False
    if not Entry[0] == Username or not Entry[1] == Password: return ui.notify(message="Credenziali invalide.", close_button="OK", type="negative"); return False
    
    return True

def get_student_data():
    user_data = get_user_data()
    account_name = user_data["USERNAME"]

    student_data = Database.get_entry("students_accounts", "account_name", account_name)
    return student_data
    

def render_page():

    # SET BACKGROUND IMAGE
    ui.query("body").style(f'background-image: url("https://edu.google.com/images/social_image.jpg")')
    ui.query("body").style(f'background-repeat: norepeat')
    ui.query("body").style(f'background-size: cover')
    ui.query("body").style(f'backdrop-filter: blur(8px)')
    ui.query("body").style(f'--webkit-backdrop-filter: blur(8px)')
    ui.query("body").style(f'overflow: hidden')
    ui.query("body").style(f'display: flex')
    ui.query("body").style(f'align-items: center')
    ui.query("body").style(f'justify-content: center')

    # LOGIN FUNCTION
    username_field = None
    password_field = None
    def handle_login():
        if validate_login(username_field.value, password_field.value) == False: return
        login_user(username_field.value)
        
        ui.open("/")

    # LOGIN FORM
    with ui.card().style("margin-top: 20vh; display: flex; justify-content: center; align-items: center; width: 145%; transform: translateX(-15%)"):
        ui.image("https://cdn-icons-png.flaticon.com/512/8312/8312504.png").style("width: 35%; height: 25%; object-fit: cover")
        ui.label("Accesso").style("font-weight: bold; font-size: 1.5em")
        ui.separator()
        username_field = ui.input(label="Username",
                                 placeholder="...")
        password_field = ui.input(label="Password", 
                                 placeholder="...", 
                                 password=True, 
                                 password_toggle_button=True)
        
        ui.link("Password dimenticata?")
        ui.button("Accedi", on_click=handle_login).tooltip("Accedi al sistema")
