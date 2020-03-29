from app import data
from app import logger

def generate_time_report():
    logger.log("Generating time report...")
    pass

def register_client(name):
    data.insert_terminal(name)
    logger.log(f"{name} registered.")

def unregister_client(name):
    data.delete_terminal(name)
    logger.log(f"{name} unregistered.")

def register_card_reading(terminal_id, rfid):
    try:
        terminal_name = next(terminal[1] for terminal in data.get_terminals() if terminal[0] == terminal_id)
        data.insert_card_reading(terminal_id, rfid)
        logger.log(f"Registered card reading on {terminal_name}.")
    except StopIteration:
        logger.log(f"Terminal with id {terminal_id} not found!")

def register_employee(name):
    data.insert_employee(name)
    logger.log(f"{name} registered.")

def unregister_employee(employee_id):
    data.delete_employee(employee_id)
    logger.log(f"Employee with id {employee_id} unregistered.")
