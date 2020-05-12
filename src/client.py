#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import tkinter as tk

broker = 'MightyTos4'
port = 8883

terminal_ids = [1, 2, 3, 4]
current_terminal_id = terminal_ids[0]

root = tk.Tk()
client = mqtt.Client()

def set_current_terminal(id):
    global current_terminal_id
    current_terminal_id = id
    root.title(f'Terminal {current_terminal_id}')

def send_card_reading(rfid):
    global current_terminal_id
    client.publish('app/card_reading', ' '.join(str(x) for x in [current_terminal_id, rfid]))

def create_main_root():
    root.attributes('-type', 'dialog')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root['bg'] = 'black'
    label = tk.Label(root, text='Listening to the MQTT', bg='black', fg='white')
    entry_label = tk.Label(root, text='RFID to send:', bg='black', fg='white')
    entry = tk.Entry(root, bg='black', fg='white')
    entry.insert(0, '1234')
    buttons_data = [(f'Set terminal to {id}', lambda i=id: set_current_terminal(i)) for id in terminal_ids]
    buttons_data.append(('Send message', lambda: send_card_reading(entry.get())))
    buttons_data.append(('Stop', root.quit))
    label.grid(pady=10)
    entry_label.grid(sticky='s', pady=10)
    entry.grid(sticky='nesw', padx=5)
    buttons = [tk.Button(root, text=b[0], command=b[1],
                         bg='black', fg='white', activebackground='#3e3e3e', activeforeground='white')
               for b in buttons_data]
    for button in buttons:
        button.grid(sticky='nesw', padx=5)

def run_client():
    client.tls_set('ca.crt')
    client.username_pw_set(username='client', password='qwe123')
    client.connect(broker, port)
    create_main_root()
    set_current_terminal(terminal_ids[0])
    root.mainloop()
    client.disconnect()

if __name__ == '__main__':
    run_client()
