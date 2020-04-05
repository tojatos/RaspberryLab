from app import data
from app import logger

def generate_time_report():
    logger.log("Generating time report...")

    cr = data.get_card_readings()

    employee_ids_on_readings = set(x[0] for x in cr)
    cr_by_employee_id = {y:[(x[2], x[3]) for x in cr if x[0] == y] for y in employee_ids_on_readings}
    cr_by_employee_id_paired = {k:list(zip(v[::2], v[1::2])) for (k, v) in cr_by_employee_id.items()}
    i = cr_by_employee_id_paired.items()

    csv = "\n".join([",".join([str(k or "None"), t[0][0], t[0][1], t[1][0], t[1][1]]) for (k, v) in i for t in v])

    with open("time_report.csv", "w") as file:
        file.write(csv)

    logger.log("Time report generated.")

def register_client(name):
    data.insert_terminal(name)
    logger.log(f"{name} registered.")

def unregister_client(name):
    data.delete_terminal(name)
    logger.log(f"{name} unregistered.")

def register_card_reading(terminal_id, rfid):
    cards = data.get_cards()
    rfids = set(x[0] for x in cards)
    if rfid not in rfids:
        data.insert_card(rfid)

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

def associate_card_with_employee(rfid, employee_id):
    data.update_card_employee(rfid, employee_id)
    logger.log(f"Card {rfid} assigned to employee with id {employee_id}.")

def disassociate_card_with_employee(rfid):
    data.update_card_employee(rfid)
    logger.log(f"Card {rfid} disassigned.")
