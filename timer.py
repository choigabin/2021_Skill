import tkinter
import tkinter as tk
from tkinter import *
import tkinter.font
import os

window=Tk()
window.title("Skill")
window.geometry("640x400")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')
timefont=tkinter.font.Font(family="HYHeadLine", size=40, weight='bold')

timerBtn = tk.Button(window,text="타이머",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = tk.Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn = tk.Button(window,text="플래너 보기",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

image = tk.PhotoImage(file="C:/2021_Skill/abokado.png",width=135, height=170)
label = tk.Label(window, image=image, width=135, height=170, bg='#f2e2c6')
label.place(x=50, y=110)

timeLabel = tk.Label(window, text="07:44:45", justify="center", bg='#f2e2c6', fg='#4f4f4f', font=timefont, width=8, height=1)
timeLabel.place(x=200,y=150)

startBtn = tk.Button(window, text="시작", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
startBtn.place(x=200,y=240)
stopBtn = tk.Button(window, text="중지", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
stopBtn.place(x=300,y=240)
endBtn = tk.Button(window, text="종료", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
endBtn.place(x=400,y=240)

image = tk.PhotoImage(file="C:/2021_Skill/kado.png",width=120, height=170)
label = tk.Label(window, image=image, width=120, height=170, bg='#f2e2c6')
label.place(x=400, y=110)

window.mainloop()