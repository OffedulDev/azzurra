# IMPORTS
from nicegui import ui
from datetime import datetime, timedelta

import pages.private.student.Root as Root
import pages.public.Login as Login
import shared.Database as Database
import pages.private.student.Argomenti as Argomenti

# FUNCTIONS
def render_dialog(entry):
    with ui.dialog() as dialog, ui.card() as card:
        with ui.row() as title_row:
            title_row.classes("flex flex-row items-center")
            ui.label(entry[8]).classes("font-bold")
            ui.label(entry[2]).classes("text-white outline outline-1 outline-black border-box px-2 py-1 rounded-full bg-black")
        
        ui.label(entry[6]).classes("max-w-md h-fit")

        with ui.element("span") as info_column:
            info_column.classes("border-box p-3 gap-1 outline outline-1 outline-black rounded-lg w-full h-fit")
            
            ui.label("Data di consegna").classes("pb-1")
            with ui.row() as row_b:
                row_b.classes("flex flex-row items-center gap-2")
                ui.icon("handshake", size="1.5rem").classes("text-white bg-green-500 rounded-full border-box p-1")
                ui.label(entry[7]).classes("text-[1rem]")

        ui.button("OK", icon="cancel", on_click=dialog.close).classes("text-red").props("rounded outline")

    return dialog

def get_compito(compito_id):
    student_data = Login.get_student_data()
    conditions = {
                    "SCHOOL_NAME": student_data[1],
                    "CLASS": student_data[2],
                    "ASSIGNMENT_ID": compito_id
                }

    entries = Database.get_entries("assignments", conditions)
    return entries[0]

def get_last_compito():
    tomorrow_date = datetime.now() + timedelta(1)
    student_data = Login.get_student_data()

    conditions = {
                    "SCHOOL_NAME": student_data[1],
                    "CLASS": student_data[2],
                    "DATE": tomorrow_date.strftime("%Y-%m-%d")
                }

    entries = Database.get_entries("assignments", conditions)
    return entries[0]

def render_page():
    with Root.render_page() as main_row: 
        with ui.column() as column:
            column.classes("p-4 sm:ml-[15rem]")

            with ui.row() as row_a:
                row_a.classes("flex flex-row items-center h-fit")

                ui.icon("checklist", size="md")
                ui.markdown("### Compiti")
        
            # Filters Vars
            date_filter = None
            teacher_filter = None
            compiti_column = None

            def render_compiti():
                if compiti_column == None: return

                student_data = Login.get_student_data()
                compiti_column.clear()

                conditions = {
                    "SCHOOL_NAME": student_data[1],
                    "CLASS": student_data[2],
                    "DATE": date_filter.value
                }

                if not teacher_filter.value == "":
                    conditions["TEACHER_FULL_NAME"] = teacher_filter.value

                entries = Database.get_entries("assignments", conditions, approximate=True)
                for entry in entries:
                    linked_subject = Database.get_entry("lesson_subjects", "ARGOMENTO_ID", entry[4])

                    with compiti_column:
                        with ui.card() as compiti_card:
                            with ui.row() as title_row:
                                title_row.classes("flex flex-row items-center")
                                ui.label(entry[8]).classes("font-bold")
                                ui.label(entry[2]).classes("text-white outline outline-1 outline-black border-box px-2 py-1 rounded-full bg-black")
                                
                            ui.label(entry[6]).classes("max-w-md h-fit")
                            
                            with ui.element("span") as info_column:
                                info_column.classes("border-box p-3 gap-1 outline outline-1 outline-black rounded-lg w-full h-fit")
                                
                                ui.label("Data di consegna").classes("pb-1")
                                with ui.row() as row_b:
                                    row_b.classes("flex flex-row items-center gap-2")
                                    ui.icon("handshake", size="1.5rem").classes("text-white bg-green-500 rounded-full border-box p-1")
                                    ui.label(entry[7]).classes("text-[1rem]")

                                ui.label("Argomento collegato").classes("pt-3 pb-1")
                                with ui.row() as row_b:
                                    row_b.classes("flex flex-row items-center gap-2")
                                    ui.icon("dashboard", size="1.5rem").classes("text-white bg-blue-200 rounded-full border-box p-1")
                                    
                                    dialog = Argomenti.render_dialog(linked_subject, show_compiti_button=False)
                                    ui.button(linked_subject[3], on_click=dialog.open).classes("text-[1rem] text-black text-left").props("flat")


            # Filters
            with ui.row() as row_b:
                tomorrow_date = datetime.now() + timedelta(1)
                with ui.input("Data", on_change=render_compiti, value=tomorrow_date.strftime("%Y-%m-%d")) as date:
                    date.props("outlined")
                    
                    with date.add_slot("append"):
                        ui.icon('edit_calendar').on("click", lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        date_filter = ui.date().bind_value(date).bind_value_from(date).props("minimal")

                with ui.input("Docente", on_change=render_compiti) as teacher:
                    teacher.props("outlined")
                    teacher_filter = teacher

                    with teacher.add_slot("append"):
                        ui.icon("square_foot")       

            # Refreshable Zone
            with ui.column() as compiti_column_a:
                compiti_column_a.classes("w-full h-full")
                compiti_column = compiti_column_a

            render_compiti()




            
            

