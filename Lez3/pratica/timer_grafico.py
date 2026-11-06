import tkinter as tk
from tkinter import messagebox

ore = minuti = secondi = 0
job = None

def aggiorna():
    display.config(text=f"{ore:02d}:{minuti:02d}:{secondi:02d}")

def avvia():
    global ore, minuti, secondi, job
    ore = int(e_ore.get() or 0)
    minuti = int(e_min.get() or 0)
    secondi = int(e_sec.get() or 0)

    if ore == minuti == secondi == 0:
        messagebox.showinfo("Timer", "Metti un tempo > 0")
        return
    tick()

def tick():
    global ore, minuti, secondi, job
    
    aggiorna()
    
    if ore == minuti == secondi == 0:
        root.bell()
        messagebox.showinfo("Timer", "Tempo Scatudo")
        return
    
    if secondi > 0:
        secondi -= 1
    elif minuti > 0:
        minuti -= 1
        secondi = 59
    elif ore > 0:
        ore -= 1
        minuti = 59
        secondi = 59
    
    job = root.after(1000, tick)

def stop():
    global job
    if job:
        root.after_cancel(job)
        job = None

root = tk.Tk()

root.title("TIMER")
root.geometry("400x350")

tk.Label(root, text="Ore").grid(row=0, column=0)
tk.Label(root, text="Min").grid(row=0, column=1)
tk.Label(root, text="Sec").grid(row=0, column=2)

e_ore = tk.Entry(root, width=5)
e_ore.grid(row=1, column=0)

e_min = tk.Entry(root, width=5)
e_min.grid(row=1, column=1)

e_sec = tk.Entry(root, width=5)
e_sec.grid(row=1, column=2)

e_ore.insert(0, '0')
e_min.insert(0, '0')
e_sec.insert(0, '0')

display = tk.Label(root, text="00:00:00")
display.grid(row=2, column=0, columnspan=3, pady=10)

tk.Button(root, text="Avvia", command=avvia).grid(row=3, column=0)
tk.Button(root, text="Stop", command=stop).grid(row=3, column=2)

root.mainloop()

