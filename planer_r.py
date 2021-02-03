import tkinter as tk
from tkinter import *
import tkinter.font

window = Tk()
window.title("Skill")
window.geometry("640x400")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font = tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')
labelFont = tkinter.font.Font(family="HYHeadLine", size=11, weight='bold')
timeFont = tkinter.font.Font(family="HYHeadLine", size=14, weight='bold')
sideFont = tk.font.Font(size=30, weight='bold')

timerBtn = tk.Button(window,text="타이머",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = tk.Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn = tk.Button(window,text="플래너 보기",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

# bg='#fbdea2'
# fram = tk.Frame(window, bg='#ffffff', bd=40)
# fram.pack()
# 날짜+요일 레이블
DateLabel = tkinter.Label(window, text="2021.01.28.화요일",bg='#f2e2c6', fg='#4f4f4f', font=labelFont)
DateLabel.place(x=260, y=60)

# 뒤로 넘기는 버튼
# backBtn = tk.Button(window, test='〈', bg='#f2e2c6', fg='#8eb695', font=sideFont, width=10, y=10)
# backBtn.place(x=30, y=200)

# 목표레이블
PlanLabel = tkinter.Label(window, text="목표",bg='#f2e2c6', fg='#4f4f4f', font=labelFont)
PlanLabel.place(x=180, y=100)
# 누적시간 레이블
SumTimeLabel = tkinter.Label(window, text="07:44:45", justify="center", bg='#f2e2c6', fg='#4f4f4f', font=timeFont, width=8, height=1)
SumTimeLabel.place(x=400, y=95)
# 내용 레이블
contentLabel = tkinter.Label(window, text="내용", bg='#f2e2c6', fg='#4f4f4f', font=labelFont)
contentLabel.place(x=180, y=130)
# 체크 박스
check1 = tk.Checkbutton(window, bg='#f2e2c6')
check1.place(x=430, y=130)

check2 = tk.Checkbutton(window, bg='#f2e2c6')
check2.place(x=430, y=160)

check3 = tk.Checkbutton(window, bg='#f2e2c6')
check3.place(x=430, y=190)

check4 = tk.Checkbutton(window, bg='#f2e2c6')
check4.place(x=430, y=220)

check5 = tk.Checkbutton(window, bg='#f2e2c6')
check5.place(x=430, y=250)

check6 = tk.Checkbutton(window, bg='#f2e2c6')
check6.place(x=430, y=280)

check7 = tk.Checkbutton(window, bg='#f2e2c6')
check7.place(x=430, y=310)

# 앞으로 가는 버튼
# frontBtn = tk.Button(window, test='〈', bg='#f2e2c6', fg='#8eb695', font=sideFont, width=10, y=10)
# frontBtn.place(x=30, y=200)

# 저장 버튼
saveBtn = tk.Button(window, bg='#8eb695', text='저장', width=5, height=1)
saveBtn.place(x=300, y=340)

window.mainloop()