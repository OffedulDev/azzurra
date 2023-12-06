# IMPORTS
from nicegui import ui
import pages.private.student.Root as Root
import pages.public.Login as Login
import pages.private.student.Compiti as Compiti

# FUNCTIONS
def truncate_string(input_string, max_length=60):
    if len(input_string) <= max_length:
        return input_string
    else:
        truncated_string = input_string[:max_length - 3] + "..."
        return truncated_string

def render_page():
    data = Login.get_student_data()
    
    with Root.render_page() as main_row: 
        with ui.column() as column:
            column.classes("pt-2 px-6 sm:ml-[15rem]")

            ui.markdown(f"### **{data[3]}**")
            ui.table(columns=[
                {"name": "Dato", "label": "Dato", "field": "Dato", "required": True, "align": "left"},
                {"name": "Contenuto", "label": "Contenuto", "field": "Contenuto", "required": True, "align": "right"}
            ], rows=[
                {
                    "Dato": "Scuola", "Contenuto": data[1]
                },
                {
                    "Dato": "Classe", "Contenuto": data[2]
                }
            ]).classes("h-full w-full sm:w-fit")

            with ui.row() as row:
                row.classes("mt-5 sm:mt-10")
                ui.markdown("#### **Compiti per domani**")

            with ui.element("div") as container:
                container.classes("flex flex-row gap-3")

                last_compito = Compiti.get_last_compito()
                with ui.card() as card:
                    card.classes("gap-0.5 max-w-md")
                    ui.markdown(f"**{last_compito[8]}**")
                    ui.markdown(f"*{last_compito[2]}*")
                    ui.separator().classes("mb-2")
                    ui.markdown(truncate_string(last_compito[6], max_length=60))
                
                with ui.row() as row_b:
                    row_b.classes("flex flex-col justify-center")
                    ui.button(text="Vedi tutti", icon="arrow_forward", on_click=lambda: ui.open("/area-studente/compiti")).props("flat").classes("h-10")
            

