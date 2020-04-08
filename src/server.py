#!/usr/bin/env python3

from app import controller, data, logger
import paho.mqtt.client as mqtt
import tkinter as tk
import tkinter.messagebox
from tkinter import simpledialog as sd
import traceback

def callback_error(self, *args):
    message = 'Generic error:\n\n'
    message += traceback.format_exc()
    tkinter.messagebox.showerror('Error', message)

tk.Tk.report_callback_exception = callback_error

broker = 'localhost'

root = tk.Tk()
client = mqtt.Client()

def print_data(title, data_to_print):
    print_window = tk.Tk()
    print_window.title(title)
    print_window.attributes('-type', 'dialog')
    print_window['bg'] = 'grey'
    data_labels = [[tk.Label(print_window, text=str(y), bg='black', fg='white') for y in x] for x in data_to_print]
    for i, labels in enumerate(data_labels):
        for j, label in enumerate(labels):
            label.grid(row=i, column=j, sticky='nesw', padx=1, pady=1)

def register_client():
    client_name = sd.askstring('Input', 'What name to add?', parent=root)
    if not client_name:
        return
    controller.register_client(client_name)

def unregister_client():
    client_name = sd.askstring('Input', 'What name to remove?', parent=root)
    if not client_name:
        return
    controller.unregister_client(client_name)

def register_employee():
    employee_name = sd.askstring('Input', 'What name to add?', parent=root)
    if not employee_name:
        return
    controller.register_employee(employee_name)

def unregister_employee():
    employee_id = sd.askinteger('Input', 'What id to remove?', parent=root)
    if not employee_id:
        return
    controller.unregister_employee(employee_id)

def associate_card_with_employee():
    rfid = sd.askinteger('Input', 'What rfid to associate?', parent=root)
    if not rfid:
        return
    employee_id = sd.askinteger('Input', 'What employee id to associate?', parent=root)
    if not employee_id:
        return
    controller.associate_card_with_employee(rfid, employee_id)

def disassociate_card_with_employee():
    rfid = sd.askinteger('Input', 'What rfid to disassociate?', parent=root)
    if not rfid:
        return
    controller.disassociate_card_with_employee(rfid)

def generate_time_report():
    controller.generate_time_report()

def create_main_root():
    root.title('SERVER')
    root.attributes('-type', 'dialog')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root['bg'] = 'black'
    label = tk.Label(root, text='Listening to the MQTT', bg='black', fg='white')
    buttons_data = [
        ('Register client', register_client),
        ('Unregister client', unregister_client),
        ('Register employee', register_employee),
        ('Unregister employee', unregister_employee),
        ('Associate card with employee', associate_card_with_employee),
        ('Disassociate card with employee', disassociate_card_with_employee),
        ('Generate time report', generate_time_report),
        ('Print employees', lambda: print_data('Employees', data.get_employees())),
        ('Print cards', lambda: print_data('Cards', data.get_cards())),
        ('Print terminals', lambda: print_data('Terminals', data.get_terminals())),
        ('Print card readings', lambda: print_data('Card readings', data.get_card_readings())),
        ('Stop', root.quit),
    ]
    label.grid(pady=10)
    buttons = [tk.Button(root, text=b[0], command=b[1],
                         bg='black', fg='white', activebackground='#3e3e3e', activeforeground='white')
               for b in buttons_data]
    for button in buttons:
        button.grid(sticky='nesw', padx=5)

def process_message(client, userdata, message):
    message_decoded = str(message.payload.decode('utf-8'))
    logger.log(f'Message received: {message_decoded}')
    (terminal_id, rfid) = message_decoded.split(' ')
    controller.register_card_reading(int(terminal_id), int(rfid))

def run_server():
    client.connect(broker)
    client.on_message = process_message
    client.loop_start()
    client.subscribe('app/card_reading')

    create_main_root()
    root.mainloop()

    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    run_server()
