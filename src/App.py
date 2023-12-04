# IMPORTS
from fastapi.responses import RedirectResponse
from nicegui import ui, app
from uuid import uuid4

# PAGES
import pages.public.Login as login
import pages.private.student.Dashboard as student_dashboard

# APP
@ui.page("/")
def main():
    if login.is_user_logged_in() == True:
        if login.get_user_data()["TYPE"] == 0:
            student_dashboard.render_page(login.get_student_data())
            return
        
        ui.label("Area Docente")
        return

    return RedirectResponse(url="/login")


@ui.page("/login", title="Accedi")
def login_page():
    if login.is_user_logged_in() == True: 
        return RedirectResponse(url="/")
    
    login.render_page()

@ui.page("/debug")
def debug():
    return student_dashboard.render_page({
        "full_name": "Mario Rossi",
        "school_name": "Istituto Comprensivo di Lanterna",
        "class": "1C"
    })

ui.run(title="QuickClass", language="it", storage_secret=uuid4())