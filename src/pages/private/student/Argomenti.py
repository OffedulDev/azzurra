# IMPORTS
from nicegui import ui
from datetime import datetime

import pages.private.student.Root as Root
import pages.public.Login as Login
import shared.Database as Database

# FUNCTIONS
def render_page():
    with Root.render_page() as main_row: 
        with ui.column() as column:
            column.classes("p-4")
            with ui.row() as row_a:
                row_a.classes("flex flex-row items-center h-fit")

                ui.icon("newspaper", size="md")
                ui.markdown("### Argomenti di lezione")
        
            # Filters Vars
            argomenti_column = None
            teacher_filter = None
            date_filter = None

            def render_argomenti_di_lezione():
                student_data = Login.get_student_data()
                argomenti_column.clear()

                conditions = {
                    "SCHOOL": student_data[1],
                    "CLASS": student_data[2],
                    "DATE": date_filter.value
                }

                if not teacher_filter.value == "":
                    conditions["TEACHER_FULL_NAME"] = teacher_filter.value

                entries_with_school = Database.get_entries("lesson_subjects", conditions, approximate=True)

                for entry in entries_with_school:
                    with argomenti_column:
                        with ui.row() as argomento_row:
                            argomento_row.classes("w-full gap-3 flex flex-row items-center flex-start outline outline-1 outline-gray-500 border-box px-6 py-5")
                            argomento_row.style("border-radius: 1.5rem")

                            ui.icon("toc", size="1.5rem").classes("bg-black text-white border-box p-1 rounded-full")
                            ui.label(entry[3]).classes("pr-4")

                            ui.icon("schedule", size="1.5rem").classes("bg-orange-500 text-white border-box p-1 rounded-full")
                            ui.label(entry[7]).classes("pr-4")
                            ui.element("br")

                            ui.icon("draw", size="1.5rem").classes("bg-blue-500 text-white border-box p-1 rounded-full")
                            ui.label(entry[1]).classes("font-semibold")

                            ui.button("Visualizza", icon="link").props("flat")


            # Filters
            with ui.row() as row_b:
                with ui.input("Data", value=datetime.now().strftime("%Y-%m-%d")) as date:
                    date.props("outlined")
                    
                    with date.add_slot("append"):
                        ui.icon('edit_calendar').on("click", lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        date_filter = ui.date(on_change=render_argomenti_di_lezione).bind_value(date).bind_value_from(date).props("minimal")

                with ui.input("Docente", on_change=render_argomenti_di_lezione) as teacher:
                    teacher.props("outlined")
                    teacher_filter = teacher

                    with teacher.add_slot("append"):
                        ui.icon("square_foot")
                
            # Refreshable Zone

            with ui.column() as argomenti_column_a:
                argomenti_column_a.classes("w-full")
                argomenti_column = argomenti_column_a

            render_argomenti_di_lezione()
                



            
            

