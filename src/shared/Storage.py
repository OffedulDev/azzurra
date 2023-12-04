# IMPORTS
from nicegui import app

# FUNCTIONS
def write_to_storage(key, value):
    app.storage.user[key] = value

def get_from_storage(key):
    return app.storage.user.get(key)