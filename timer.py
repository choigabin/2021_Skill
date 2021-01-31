from tkinter import *
import tkinter.font

window=Tk()

window.title("Skill")
window.geometry("640x400+100+100")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')
timefont=tkinter.font.Font(family="HYHeadLine", size=30, weight='bold')

timerBtn = Button(window,text="타이머",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn=Button(window,text="플래너 보기",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

#아보카도 그림 놓기
#abo = PhotoImage(fime="abocado.png")
#abocado = Label(window, image=abo)
#abocado.place(x=120, y=200)

timeLabel=Label(window, text="07:44:45", justify="center", bg='#f2e2c6', fg='#4f4f4f', font=timefont, width=10, height=1)
timeLabel.place(x=210,y=100)

startBtn = Button(window, text="시작", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
stopBtn = Button(window, text="중지", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
endBtn = Button(window, text="종료", padx=5, pady=5,width=7,bg='#8eb695', fg='#4f4f4f', font=font)
startBtn.place(x=200,y=200)
stopBtn.place(x=300,y=200)
endBtn.place(x=400,y=200)

window.mainloop()