import datetime
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import time
import pygame


t = 0

def set():
    global t
    rem = sd.askstring('Время напоминания', 'Введите время напоминания в формате чч:мм в 24 часовом формате')
    if rem:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}')

def check():
    global t  ##время напоминания
    if t:
        now = time.time()  ## хранит текущее время
        if now >= t:
            play.snd()
            t = 0
    window.after(10000, check)  ## функция не нагружает комп


window = Tk()
window.title('Напоминание')
label = Label(text='Установите напоминание')
label.pack(pady=10)
set.button = Button(text='Установить напоминание', command=set)
set.button.pack()

window.mainloop()

