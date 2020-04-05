#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

def create_main_root():
    root.title('CLIENT')
    root.attributes('-type', 'dialog')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root['bg'] = 'black'
    label = tk.Label(root, text='Listening to the MQTT', bg='black', fg='white')
    terminal_ids = [1, 2, 3, 4]
    buttons_data = [(f'Set terminal to {id}', lambda i=id: print(i)) for id in terminal_ids]
    buttons_data.append(('Stop', root.quit))
    label.grid(pady=10)
    buttons = [tk.Button(root, text=b[0], command=b[1],
                         bg='black', fg='white', activebackground='#3e3e3e', activeforeground='white')
               for b in buttons_data]
    for button in buttons:
        button.grid(sticky='nesw', padx=5)

def run_client():
    create_main_root()
    root.mainloop()

if __name__ == '__main__':
    run_client()
