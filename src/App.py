# IMPORTS
from fastapi.responses import RedirectResponse
from nicegui import ui, app

import asyncio
from uuid import uuid4

# SHARED
import shared.Storage as Storage

# PAGES
import pages.public.Login as login

# PAGES - STUDENTE
import pages.private.student.Dashboard as student_dashboard
import pages.private.student.Argomenti as argomenti_di_lezione
import pages.private.student.Compiti as compiti

# PAGES - DOCENTE
import pages.private.teacher.SelezionaDati as seleziona_dati
import pages.private.teacher.Dashboard as teacher_dashboard

# APP
@ui.page("/")
def main():
    if login.is_user_logged_in() == True:
        if login.get_user_data()["TYPE"] == 0:
            return RedirectResponse(url="/area-studente")
        
        return RedirectResponse(url="/area-docente")

    return RedirectResponse(url="/login")


@ui.page("/login", title="Accedi")
def login_page():
    if login.is_user_logged_in() == True: 
        return RedirectResponse(url="/")
    
    return login.render_page()

# Area Studente
@ui.page("/area-studente")
def area_studente_main():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 1:
        return RedirectResponse(url="/")
    
    return RedirectResponse(url="/area-studente/dashboard")

@ui.page("/area-studente/dashboard")
def area_studente_dashboard():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 1:
        return RedirectResponse(url="/")
    
    return student_dashboard.render_page()

@ui.page("/area-studente/argomenti-di-lezione")
def area_studente_argomenti_di_lezione():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 1:
        return RedirectResponse(url="/")
    
    return argomenti_di_lezione.render_page()

@ui.page("/area-studente/compiti")
async def area_studente_compiti():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 1:
        return RedirectResponse(url="/")
    
    return compiti.render_page()

@ui.page("/area-docente")
def area_docente():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 0:
        return RedirectResponse(url="/")

    if Storage.get_from_storage("teacher_data") == None:
        return RedirectResponse(url="/area-docente/seleziona-dati")
    
    return RedirectResponse(url="/area-docente/dashboard")

@ui.page("/area-docente/dashboard")
def area_docente():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 0:
        return RedirectResponse(url="/")

    if Storage.get_from_storage("teacher_data") == None:
        return RedirectResponse(url="/area-docente/seleziona-dati")
    
    return teacher_dashboard.load_page()

@ui.page("/area-docente/seleziona-dati")
async def area_docente():
    if login.is_user_logged_in() == False or login.get_user_data()["TYPE"] == 0:
        return RedirectResponse(url="/")
    
    return await seleziona_dati.load_page()

@ui.page("/debug/1")
async def debug():
    login.login_user("David")
    return await seleziona_dati.load_page()

ui.run(title="QuickClass", language="it", storage_secret=uuid4())