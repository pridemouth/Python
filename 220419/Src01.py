
###  Err

from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("애완동물 선택하기")

def change():
	if var.get() == 1:
		lImage.configure(image = photo1)
	elif var.get() == 2:
		lImage.configure(image = photo2)
	elif var.get() == 3:
		lImage.configure(image = photo3)

lText = Label(window, text="좋아하는 동물", fg="blue", font=("궁서", 20))

var = IntVar()
rb1 = Radiobutton(window, text="고양이", variable=var, value=1)
rb2 = Radiobutton(window, text="강아지", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
btnOk = Button(window, text="선택", command=change)

photo1 = PhotoImage(file="../img/cat.gif")
photo2 = PhotoImage(file="../img/dog.gif")
photo3 = PhotoImage(file="../img/rabbit.gif")

lImage = Label(window, width=200, height=200, bg="yellow", anchor=SE, image=None)

lText.pack()
rb1.pack()
rb2.pack()
rb3.pack()
btnOk.pack()
lImage.pack()

window.mainloop()