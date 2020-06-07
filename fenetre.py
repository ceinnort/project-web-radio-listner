# coding: utf-8
import tkinter as tk
import controler

RADIO_LIST = controler.get_list_radio()

class StationButton(tk.Button):
    def on_click(self):
        play(self['text'])

def play(radio):
    print(radio)
    controler.play(radio)

def stop():
    controler.stop()

window = tk.Tk()

label = tk.Label(window, text="Hello World")
label.pack()

# bouton de sortie
button = tk.Button(window, text="Fermer", command=window.quit)

frame = tk.Frame(window)

for ligne in range(len(RADIO_LIST)):
    print(ligne, RADIO_LIST[ligne])
    b = StationButton(frame, text=RADIO_LIST[ligne], borderwidth=1)
    b['command'] = b.on_click
    b.grid(row=ligne)

frame.pack()
tk.Button(window, text="stop", command=stop).pack()
button.pack()
window.mainloop()
