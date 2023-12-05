# IMPORTS
from nicegui import ui
import pages.public.Login as Login

# FUNCTIONS
def render_page():
    main_row_a = None

    ui.query('.nicegui-content').classes("p-0")
    ui.query("body").style("overflow: hidden")
    ui.add_head_html("""<style>
        .sidebar {
            display: inherit;
        }
                     
        .bottom-bar {
            display: none !important;
        }
                     
        .main-row {
            display: inherit;
        }

        @media screen and (max-width: 600px) {
            .sidebar {
                display: none;
            }
            .bottom-bar {
                display: inherit !important;
            }
            .main-row {
                display: flex;
                justify-content: center;
            }
        }
        </style>
    """)


    with ui.row() as main_row:
        main_row_a = main_row
        main_row.classes("w-full main-row")

        # Click Functions
        def home_clicked():
                ui.open("/area-studente/dashboard")

        def argomenti_di_lezione_clicked():
            ui.open("/area-studente/argomenti-di-lezione")

        def compiti_clicked():
            ui.open("/area-studente/compiti")

        def logout_clicked():
            Login.logout()

        # Sidebar
        with ui.column() as column:
            column.classes("gap-2 border-r-2 border-r-gray min-h-screen sidebar")

            ui.button(icon="home", text="Dashboard", on_click=home_clicked).props("flat square").classes("text-black mt-3 min-w-full flex flex-col items-start")
            ui.separator()
            ui.button(icon="insights", text="Argomenti di Lezione", on_click=argomenti_di_lezione_clicked).props("flat square").classes("text-black min-w-full flex flex-col items-start")
            ui.separator()
            ui.button(icon="checklist", text="Compiti", on_click=compiti_clicked).props("flat square").classes("text-black min-w-full flex flex-col items-start")
            ui.separator()
            
            ui.button(icon="logout", text="Logout", on_click=logout_clicked).props("flat square").classes("text-red mt-auto mb-2 min-w-full flex flex-col items-start")

        # Mobile navigation bar
        with ui.row() as row_a:
            row_a.classes("w-fit h-fit flex flex-row justify-center align center")
            row_a.classes("absolute z-10 bottom-5")
            row_a.classes("bg-gray-100 rounded-full outline outline-1 outline-black")
            row_a.classes("bottom-bar")

            with ui.row() as row_b:
                row_b.classes("px-5 py-4")
                ui.button(icon="home", on_click=home_clicked).props("outline rounded").classes("text-black")
                ui.button(icon="insights", on_click=argomenti_di_lezione_clicked).props("outline rounded").classes("text-black")
                ui.button(icon="checklist", on_click=compiti_clicked).props("outline rounded").classes("text-black")
                ui.button(icon="logout", on_click=logout_clicked).props("outline rounded").classes("text-red")

    return main_row_a