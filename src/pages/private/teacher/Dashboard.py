# IMPORTS
from nicegui import ui
import pages.public.Login as Login
import shared.Storage as Storage

# FUNCTIONS
def load_page():
    ui.label("Area Docente Test")

    teacher_data = Storage.get_from_storage("teacher_data")
    ui.label("Scuola: " + teacher_data["school"])
    ui.label("Classe: " + teacher_data["class"])
    ui.label("Materia: " + teacher_data["subject"])
    ui.button("TEMP RESET", on_click=lambda: Storage.write_to_storage("teacher_data", None))
