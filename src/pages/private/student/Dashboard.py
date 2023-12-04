# IMPORTS
from nicegui import ui

# FUNCTIONS
def render_page(data):
    ui.query('.nicegui-content').classes("p-0")

    print(data)
    with ui.row():
        with ui.column() as column:
            column.classes("gap-2 border-r-2 border-r-gray min-h-screen flex flex-col")

            ui.button(icon="home", text="Dashboard").props("flat square").classes("text-black mt-3 min-w-full flex flex-col items-start")
            ui.separator()
            ui.button(icon="insights", text="Argomenti di Lezione").props("flat square").classes("text-black min-w-full flex flex-col items-start")
            ui.separator()
            ui.button(icon="checklist", text="Compiti").props("flat square").classes("text-black min-w-full flex flex-col items-start")
            ui.separator()
            

            
            ui.button(icon="logout", text="Logout").props("flat square").classes("text-red mt-auto mb-2 min-w-full flex flex-col items-start")

        with ui.column() as column:
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
            ])

            with ui.row() as row:
                row.classes("mt-10")
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
            
        