# from tkinter import *
#
# window = tkinter.Tk()
# window.title("rara")
# window.geometry("700x500+300+100")
# window.mainloop()
import tkinter

window=tkinter.Tk()

window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="안녕하세요.")
label.pack()

window.mainloop()