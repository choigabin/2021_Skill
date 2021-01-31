from tkinter import *
import tkinter.font

window=Tk()

window.title("Skill")
window.geometry("640x400+100+100")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')

timerBtn = Button(window,text="타이머",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn=Button(window,text="플래너 보기",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

window.mainloop()