import tkinter as tk
import os
from tkinter.constants import TRUE
import GameSimulator as gm
from tkinter import messagebox  

root = tk.Tk()

root.title("Game Simulation")
root.geometry("300x200")

label = tk.Label(root, fg="blue")
label.pack()
label.config(text="Game Simulation Using Hand Guesture",pady=0)

label2 = tk.Label(root, fg="blue")
label2.pack(pady=20)
label2.config(text="By Tushar and Priyanshu Patel")



def startSimulator():
    messagebox.showinfo("Ready to Simulate ?","You will need to press ESC button to exit from Simulation Window!")  
    gm.startSimulationTask(True)
    gm.startSimulationTask(False)

frame = tk.Frame(root)
frame.pack(pady=20)
button = tk.Button(frame, text="START", fg="green",command=startSimulator)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="EXIT",fg="red",command=root.destroy)
slogan.pack(side=tk.LEFT,padx=10)




root.mainloop()