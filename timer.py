import tkinter as tk
from tkinter import *
import tkinter.font
import time

window=Tk()
window.title("Skill")
window.geometry("640x400")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')
timeFont=tkinter.font.Font(family="HYHeadLine", size=40, weight='bold')

timerBtn = tk.Button(window,text="타이머",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = tk.Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn = tk.Button(window,text="플래너 보기",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

def startTimer():
    if(running):
        global timer
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10, startTimer)

#시작버튼을 누르면,
def start():
    global running
    #running을 True 상태로 변환
    running = True

#중지버튼을 누르면,
def stop():
    global running
    #running을 False 상태로 변환
    running = False

#running의 초기값은 False로 지정
running = False
#0부터 시작하게 timer의 초기값을 0으로 지정
timer = 0

timeText = tk.Label(window, text="0", justify="center", bg='#f2e2c6', fg='#4f4f4f', font=timeFont, width=8, height=1)
timeText.place(x=200, y=150)

BigKado = tk.PhotoImage(file="C:/Users/gabin/Desktop/헤헤/PYTHON/SKILL/abokado.png",width=135, height=170)
BigKadoLabel = tk.Label(window, image=BigKado, width=135, height=170, bg='#f2e2c6')
BigKadoLabel.place(x=50, y=110)

smallKado = tk.PhotoImage(file="C:/Users/gabin/Desktop/헤헤/PYTHON/SKILL/kado.png",width=120, height=120)
smallKadoLabel = tk.Label(window, image=smallKado, width=113, height=113, bg='#f2e2c6')
smallKadoLabel.place(x=460, y=120)

startBtn = tk.Button(window, text="시작", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font, command=start)
startBtn.place(x=200,y=250)
stopBtn = tk.Button(window, text="중지", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font, command=stop)
stopBtn.place(x=300,y=250)
endBtn = tk.Button(window, text="종료", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
endBtn.place(x=400,y=250)

startTimer()
window.mainloop()