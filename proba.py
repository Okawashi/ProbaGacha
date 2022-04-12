import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Probabilités")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Probabilité :").grid(column=0, row=0)
entryProba = ttk.Entry(frm)
entryProba.grid(column=1, row=0)
entryProba.insert(0, "0.05")

ttk.Label(frm, text="Nombre voulu :").grid(column=0, row=1)
entryPulls = ttk.Entry(frm)
entryPulls.grid(column=1, row=1)
entryPulls.insert(0, "3")

labelResultat = ttk.Label(frm, text="")
labelResultat.grid(column=0, row=2)

boutonCalculer = ttk.Button(frm, text="Calculer")
boutonCalculer.grid(column=0, row=3)

def calculNbTirages(n, p):
    tirage = 0
    nombreTirageEffectues = 0
    nombreTirageCorrects = 0
    while(nombreTirageCorrects < n):
        nombreTirageEffectues += 1
        tirage = random.random()
        if(tirage <= p):
            nombreTirageCorrects += 1
    return nombreTirageEffectues

def calculTiragesMoyens():
    i = 0
    tiragesTotaux = 0
    while(i < 100):
        tiragesTotaux += calculNbTirages(int(entryPulls.get()), float(entryProba.get()))
        i += 1
    message = "Environ " + str(tiragesTotaux/100) + " pulls"
    labelResultat["text"] = message
    print(message)

boutonCalculer["command"] = calculTiragesMoyens

ttk.Button(frm, text="Quitter", command=root.destroy).grid(column=1, row=3)

root.mainloop()