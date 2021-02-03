import tkinter as tk
from tkinter import *
import tkinter.font

window=Tk()
window.title("Skill")
window.geometry("640x400")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')
labelFont =tkinter.font.Font(family="HYHeadLine", size=11, weight='bold')
timeFont=tkinter.font.Font(family="HYHeadLine", size=14, weight='bold')

timerBtn = tk.Button(window,text="타이머",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = tk.Button(window,text="플래너 작성",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn = tk.Button(window,text="플래너 보기",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

# 레이블(날짜)
DateLabel = tkinter.Label(window, text="2021.01.28",bg='#f2e2c6', fg='#4f4f4f', font=labelFont)
DateLabel.place(x=30, y=80)

# textEdit(목표)
PlanLabel = tkinter.Label(window, text="목표",bg='#f2e2c6', fg='#4f4f4f', font=labelFont)
PlanLabel.place(x=30, y=126)
PlanTextEdit = tkinter.Entry(window,font=font,width=55, bg='#f7efe1')
PlanTextEdit.place(x=70, y=130)

# 레이블(누적 시간)
SumTimeLabel = tkinter.Label(window, text="07:44:45", justify="center", bg='#f2e2c6', fg='#4f4f4f', font=timeFont, width=8, height=1)
SumTimeLabel.place(x=500, y=125)

# textEdit(내용)
contentLabel = tkinter.Label(window, text="내용",bg='#f2e2c6', fg='#4f4f4f', font=labelFont)
contentLabel.place(x=30, y = 165)
contentText = tkinter.Text(window, bg='#f7efe1', width=55, height=13)
contentText.place(x=70, y=170)

# 버튼
writeBtn = tkinter.Button(window, text="작성",justify="center", bg='#8eb695', fg='#4f4f4f',width=7, height=1, font=font)
writeBtn.place(x=515, y=317)

window.mainloop()