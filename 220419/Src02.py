
from tkinter import *

window = Tk()
window.geometry("500x500")
window.resizable(False, False)

btnList = [None] * 3

for i in range(0, 3):
    btnList[i] = Button(window, text="버튼" + str(i+1))
    btnList[i].pack(side=TOP, fill=X, ipadx=5, ipady=5)

window.mainloop()