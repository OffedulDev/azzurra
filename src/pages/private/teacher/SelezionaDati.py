# IMPORTS
from nicegui import ui
import pages.public.Login as Login
import shared.Storage as Storage
import asyncio
import json

# FUNCTIONS
async def load_page():
    selected_school = None
    selected_class = None
    selected_subject = None

    with ui.column() as main_column:
        main_column.classes("w-full flex flex-col items-center justify-center overflow-hidden")
        main_column.style("height: calc(100vh - 2rem) !important")

        with ui.card() as select_card:
            select_card.classes("w-fit")
            select_card.style("padding: 0 !important")

            with ui.row() as stripe_row:
                stripe_row.classes("flex flex-row w-full items-center gap-2 bg-blue-700 text-white text-bold")
                stripe_row.classes("border-box p-2")

                ui.icon("location_city", size="2rem")
                ui.label("Seleziona istituto").classes("text-[1.5rem] pr-2")

            with ui.row() as access_row:
                access_row.classes("p-3 pt-0 w-full")

                labels = {}
                with ui.column() as steps_list:
                    steps_list.classes("gap-2")

                    ui.label("Passaggi per l'accesso").classes("text-gray-500")
                    labels["school"] = ui.button("Istituto", icon="school").props("rounded outline").classes("text-black")
                    labels["class"] = ui.button("Classe", icon="assignment_return").props("rounded outline disabled").classes("text-black")
                    labels["subject"] = ui.button("Materia", icon="work").props("rounded outline disabled").classes("text-black")

                with ui.column() as steps_collect:
                    steps_collect.classes("pl-2 ml-auto")

                    ui.label("Dati disponibili").classes("text-gray-500")

                    teacher_data = Login.get_teacher_data()

                    access_data = teacher_data[2]
                    access_data = json.loads(access_data)
                    
                    async def do_step(data_list):
                        selected_variable = None

                        with ui.column() as usable_data:
                            for entry in data_list:
                                def configure_button(entry_data):
                                    configured_button = ui.button(entry_data["name"]).classes("bg-white text-black w-full")                            
                                    def on_click():
                                        nonlocal selected_variable
                                        if selected_variable is not None:
                                            selected_variable["button"].classes("text-black", remove="bg-green text-white")

                                        configured_button.classes("bg-green text-white", remove="text-black")
                                        selected_variable = {
                                            "button": configured_button,
                                            "data": entry_data
                                        }

                                    configured_button.on("click", handler=on_click)

                                configure_button(entry_data=entry)

                            confirm_button = ui.button("Conferma", icon="done").props("outline rounded").classes("text-green w-full")
                            await confirm_button.clicked()

                        usable_data.delete()
                        if selected_variable is None:
                            ui.notify("Seleziona almeno un opzione!", type="info")
                            return await do_step(data_list=data_list)
                        
                        return selected_variable
                    
                    selected_school = await do_step(access_data)
                    labels["school"].props("disabled", remove="outline").classes("bg-green", remove="text-black")
                    labels["class"].props(remove="disabled")

                    selected_class = await do_step(selected_school["data"]["classes"])
                    labels["class"].props("disabled", remove="outline").classes("bg-green", remove="text-black")
                    labels["subject"].props(remove="disabled")

                    selected_subject = await do_step(selected_class["data"]["subjects"])
                    labels["subject"].props("disabled", remove="outline").classes("bg-green", remove="text-black")

                steps_collect.delete()
                ui.notify("Accesso in corso per " + teacher_data[1] + " in " + selected_school["data"]["name"] + " (" + selected_class["data"]["name"] + " | " + selected_subject["data"]["name"] + ")", type="ongoing", position="center")
                
                Storage.write_to_storage("teacher_data", {
                    "school": selected_school["data"]["name"],
                    "class": selected_class["data"]["name"],
                    "subject": selected_subject["data"]["name"]
                })

    await asyncio.sleep(2)
    return ui.open("/area-docente/dashboard")
                        