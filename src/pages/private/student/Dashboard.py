# IMPORTS
from nicegui import ui
import pages.private.student.Root as Root

# FUNCTIONS
def render_page(data):
    with Root.render_page() as main_row: 
        with ui.column() as column:
            column.classes("pt-2 px-6")

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
                with ui.card() as card:
                    card.classes("gap-0.5 max-w-md")
                    ui.markdown("**LINGUA INGLESE**")
                    ui.markdown("*Maria Sanzullo*")
                    ui.separator().classes("mb-2")
                    ui.markdown("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")
                
                with ui.row() as row_b:
                    row_b.classes("flex flex-col justify-center")
                    ui.button(text="Vedi tutti", icon="arrow_forward").props("flat").classes("h-10")
            

