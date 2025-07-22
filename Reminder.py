from cProfile import label
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import time
import pygame
from Scripts.Lekzia18 import window

window = Tk()
window.title('Напоминание')
label = Label(text='Установите напоминание')
label.pack(pady=10)
set.button = Button(text='Установить напоминание', command=set)
set.button.pack()

window.mainloop()

