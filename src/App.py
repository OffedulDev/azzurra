# IMPORTS
from fastapi.responses import RedirectResponse
from nicegui import ui, app
from uuid import uuid4

# PAGES
import pages.public.Login as login
import pages.private.student.Dashboard as student_dashboard
import pages.private.student.Argomenti as argomenti_di_lezione

# APP
@ui.page("/")
def main():
    if login.is_user_logged_in() == True:
        if login.get_user_data()["TYPE"] == 0:
            return RedirectResponse(url="/area-studente")
        
        ui.label("Area Docente")
        return

    return RedirectResponse(url="/login")


@ui.page("/login", title="Accedi")
def login_page():
    if login.is_user_logged_in() == True: 
        return RedirectResponse(url="/")
    
    login.render_page()

# Area Studente
@ui.page("/area-studente")
def area_studente_main():
    if login.is_user_logged_in() == False:
        return RedirectResponse(url="/")
    
    return RedirectResponse(url="/area-studente/dashboard")

@ui.page("/area-studente/dashboard")
def area_studente_dashboard():
    if login.is_user_logged_in() == False:
        return RedirectResponse(url="/")
    
    return student_dashboard.render_page()

@ui.page("/area-studente/argomenti-di-lezione")
def area_studente_argomenti_di_lezione():
    if login.is_user_logged_in() == False:
        return RedirectResponse(url="/")
    
    return argomenti_di_lezione.render_page()

@ui.page("/debug")
def debug():
    return argomenti_di_lezione.render_page()

ui.run(title="QuickClass", language="it", storage_secret=uuid4())