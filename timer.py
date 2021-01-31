from tkinter import *
# from matplotlib import font_manager,rc
# import matplotlib
# import matplotlib.pyplot as plt
import tkinter.font

window=Tk()

window.title("Skill")
window.geometry("640x400+100+100")
window['bg'] = '#f2e2c6'
window.resizable(False, False)

# font_path = "C:\Users\gtaz0\AppData\Local\Microsoft\Windows\Fonts\THE_Oegyeinseolmyeongseo.TTF"
# font_name = font_manager.FontProperties(fname=font_path).get_name()
# matplotlib.rc('font',family=font_name)

font=tkinter.font.Font(family="HYHeadLine", size=10, weight='bold')

timerBtn = Button(window,text="타이머",justify="center", bg='#8eb695',fg='#4f4f4f',width=26, height=2, font=font)
timerBtn.grid(column=0, row=0)
planerWBtn = Button(window,text="플래너 작성",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
planerWBtn.grid(column=1, row=0)
plannerRBtn=Button(window,text="플래너 보기",justify="center", bg='#fbdea2',fg='#4f4f4f',width=26, height=2, font=font)
plannerRBtn.grid(column=2, row=0)

# abo = PhotoImage(fime="C:\abocado.png")
# abocado = Label(window, image=abo)

timeLabel=Label(window, text="안녕하세요.", justify="center", bg='#f2e2c6', fg='#4f4f4f', font=font)
timeLabel.place(x=275,y=100)

startBtn = Button(window, text="시작", padx=5, pady=5,width=10,bg='#8eb695', fg='#4f4f4f', font=font)
stopBtn = Button(window, text="중지", padx=5, pady=5,width=10,bg='#8eb695', fg='#4f4f4f', font=font)
endBtn = Button(window, text="종료", padx=5, pady=5,width=10,bg='#8eb695', fg='#4f4f4f', font=font)
startBtn.place(x=170,y=200)
stopBtn.place(x=290,y=200)
endBtn.place(x=410,y=200)

window.mainloop()