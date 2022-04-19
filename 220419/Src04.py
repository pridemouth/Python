
from tkinter import *

window = Tk()
window.title("사진앨범보기")
window.geometry("660x500")
window.resizable(True, True)

def prev():
    if var.get() <= 0:
        var.set(10)
    else:
        var.set(var.get() - 1)
    image.configure(image=imgList[var.get()])

def post():
    if var.get() >= 10:
        var.set(0)
    else:
        var.set(var.get() + 1)
    image.configure(image=imgList[var.get()])
    
var = IntVar()
var.set(0)
imgList = [None] * 11
btnList = [None] * 2

for i in range(0, 11):
	imgList[i] = PhotoImage(file=f"./img/jeju{i+1}.gif")
    
btnList[0] = Button(window, width=25, text="<< 이전", command=prev)
btnList[1] = Button(window, width=25, text="이후 >>", command=post)

image = Label(window, width=660, height=440, anchor=SE, image=imgList[var.get()])

image.pack(side=BOTTOM)
btnList[0].place(x=0, y=7, width=100, height=45)
btnList[1].place(x=560, y=7, width=100, height=45)

window.mainloop()