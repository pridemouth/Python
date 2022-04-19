
from tkinter import *

window = Tk()
window.title("Hello")
window.geometry("210x210")
window.resizable(False, False)

fnameList = ["eclair.gif", "froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif"]
photoList = [None] * 9
btnList = [None] * 9
num = 0
xPos, yPos = 0, 0

for i in range(0, 9):
    photoList[i] = PhotoImage(file="../img/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for j in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70


window.mainloop()