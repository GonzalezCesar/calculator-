from tkinter import messagebox, Label,Tk,ttk
from time import strftime
#from typing import List
from pygame import mixer

window = Tk()
window.config(bg = 'black')
window.geometry('500x250')
window.title('Alarm')
window.minsize(width = 500, height = 250)
mixer.init()

list_hours = []
list_minutes = []
list_seconds = []

for i in range(0,24):
    list_hours.append(i)

for i in range(0,60):
    list_minutes.append(i)

for i in range(0,60):
    list_seconds.append(i)

text1 = Label(window, text = 'Hour', bg = 'black', fg = 'magenta', font = ('Arial', 12, 'bold'))
text1.grid(row=1, column=0, padx=5, pady=5)
text2 = Label(window, text = 'Minutes', bg = 'black', fg = 'magenta', font = ('Arial', 12, 'bold'))
text2.grid(row=1, column=1, padx=5, pady=5)
text3 = Label(window, text = 'Seconds', bg = 'black', fg = 'magenta', font = ('Arial', 12, 'bold'))
text3.grid(row=1, column=2, padx=5, pady=5)

combobox1 = ttk.Combobox(window, values = list_hours , style = "TCombobox", justify='center',width='12', font='Arial')
combobox1.grid(row=2, column=0, padx =15, pady=5)
combobox1.current(0)
combobox2 = ttk.Combobox(window, values = list_minutes , style = "TCombobox", justify='center',width='12', font='Arial')
combobox2.grid(row=2, column=1, padx =15, pady=5)
combobox2.current(0)
combobox3 = ttk.Combobox(window, values = list_seconds , style = "TCombobox", justify='center',width='12', font='Arial')
combobox3.grid(row=2, column=2, padx =15, pady=5)
combobox3.current(0)



style = ttk.Style()
style.theme_create('combostyle', parent='alt',settings = {'TCombobox':
                                   {'configure':
                                    {'selectbackground': 'red',
                                    'fieldbackground': 'gold',
                                    'background': 'blue'
                                    }}})
style.theme_use('combostyle')

window.option_add('*TCombobox*Listbox*Background', 'white')
window.option_add('*TCombobox*Listbox*Foreground', 'black')
window.option_add('*TCombobox*Listbox*selectBackground', 'green2')
window.option_add('*TCombobox*Listbox*selectBackground', 'black')


alarm = Label(window, fg = 'violet', bg='black', font = ('Radioland', 20))
alarm.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)
repeat = Label(window, fg = 'white', bg='black', text = 'repeat', font='Arial')
repeat.grid(column=1, row=3, ipadx=5, ipady=20)
cantidad = ttk.Combobox(window, values = (1,2,3,4,5), justify='center',width='8', font='Arial')
cantidad.grid(row=3, column=2, padx =5, pady=5)
cantidad.current(0)



def obtener_tiempo():
    x_hour = combobox1.get()
    x_minutes = combobox2.get()
    x_seconds = combobox3.get()

    hour = strftime('%H')
    minutes = strftime('%M')
    seconds = strftime('%S')

    total_hour = (hour + ' : '+ minutes+ ' : '+ seconds)
    text_hour.config(text=total_hour, font = ('Radioland', 25))

    alarm_time = x_hour +' : '+ x_minutes +' : '+ x_seconds
    alarm['text']= alarm_time

    if int(hour) == int(x_hour):
        if int(minutes) == int(x_minutes):
            if int(seconds) == int(x_seconds):
                mixer.music.load("odioiralinstituto.mp3")
                mixer.music.play(loops= int(cantidad.get()))
                messagebox.showinfo(message=alarm_time, tittle="Alarm")
    
    text_hour.after(100, obtener_tiempo)

text_hour = Label(window, fg = 'green2', bg='black')
text_hour.grid(columnspan=3, row=0,sticky="nsew", ipadx=5, ipady=20)


obtener_tiempo()

window.mainloop()