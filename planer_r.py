import tkinter as tk
from tkinter import *
import tkinter.font

window=Tk()
window.title("Skill")
window.geometry("640x400")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')

timerBtn = tk.Button(window,text="타이머",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = tk.Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn = tk.Button(window,text="플래너 보기",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

# 날짜+요일 레이블

# 목표레이블

# 누적시간 레이블

# 내용 레이블

# 체크 박스

# 버튼

window.mainloop()