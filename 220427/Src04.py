


from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *

##  png
##      24bit를 기본으로 png-8은 gif 지원, png-16은 jpeg 지원.
##  gif
##      8bit 색상 지원
##  jpg
##      16bit 색상 지원


## functions ##
def displayImage(img, width, height):
	global window, canvas, paper, photo, photo2, oriX, oriY
	
	window.geometry(str(width) + "x" + str(height))
	if canvas != None:
		canvas.destroy()
		
	canvas = Canvas(window, width = width, height = height)
	paper = PhotoImage(width = width, height = height)
	canvas.create_image((width/2, height/2), image = paper, state = "normal")
	
	blob = img.make_blob(format = 'RGB')
	for i in range(0, width):
		for k in range(0, height):
			r = blob[(i * 3 * width) + (k * 3) + 0]
			g = blob[(i * 3 * width) + (k * 3) + 1]
			b = blob[(i * 3 * width) + (k * 3) + 2]
			paper.put("#%02x%02x%02x" % (r, g, b), (k, i))

	canvas.pack()

def func_exit():
	window.quit()
	window.destroy()
	
def func_open():
	global window, canvas, paper, photo, photo2, oriX, oriY
	
	readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
	photo = Image(filename = readFp)
	oriX = photo.width
	oriY = photo.height
	
	photo2 = photo.clone()
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_save():
	global window, canvas, paper, photo, photo2, oriX, oriY
	
	if photo2 == None:
		return

	saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes=(("JPG 파일", "*.jpg; *.jpeg"), ("모든 파일", "*.*")))
	savePhoto = photo2.convert("jpg")
	savePhoto.save(filename = saveFp.name)
	
def func_zoomIn():
	global window, canvas, paper, photo, photo2, oriX, oriY
	scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue = 2, maxvalue = 4)
	photo2 = photo.clone()
	photo2.resize(int(oriX * scale), int(oriY * scale))
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_zoomOut():
	global window, canvas, paper, photo, photo2, oriX, oriY
	scale = askinteger("축소배수", "축소할 배수를 입력하세요", minvalue = 2, maxvalue = 4)
	photo2 = photo.clone()
	photo2.resize(int(oriX / scale), int(oriY / scale))
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_symmHor():
	global window, canvas, paper, photo, photo2, oriX, oriY
	photo2 = photo.clone()
	photo2.flip()
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_symmVer():
	global window, canvas, paper, photo, photo2, oriX, oriY
	photo2 = photo.clone()
	photo2.flop()
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_rotate():
	global window, canvas, paper, photo, photo2, oriX, oriY
	degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue = 0, maxvalue = 360)
	photo2 = photo.clone()
	photo2.rotate(degree)
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_brighten():
	global window,canvas, paper, photo, photo2, oriX, oriY
	value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
	photo2 = photo.clone()
	photo2.modulate(value, 100, 100)
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_darken():
	global window,canvas, paper, photo, photo2, oriX, oriY
	value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
	photo2 = photo.clone()
	photo2.modulate(value, 100, 100)
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)
	
def func_clear():
	pass
	
def func_blur():
	pass
	
def func_bw():
	global window,canvas, paper, photo, photo2, oriX, oriY
	photo2 = photo.clone()
	photo2.type = "grayscale"
	newX = photo2.width
	newY = photo2.height
	displayImage(photo2, newX, newY)

## global vars ##
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

## main loop ##
window = Tk()
window.geometry("250x250")
window.title("title")

mainMenu = Menu(window)
window.config(menu = mainMenu)

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = func_exit)

handleMenu_1 = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리 1", menu = handleMenu_1)
handleMenu_1.add_command(label = "확대", command = func_zoomIn)
handleMenu_1.add_command(label = "축소", command = func_zoomOut)
handleMenu_1.add_separator()
handleMenu_1.add_command(label = "상하 반전", command = func_symmHor)
handleMenu_1.add_command(label = "좌우 반전", command = func_symmVer)
handleMenu_1.add_separator()
handleMenu_1.add_command(label = "회전", command = func_rotate)

handleMenu_2 = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리 2", menu = handleMenu_2)
handleMenu_2.add_command(label = "밝게", command = func_brighten)
handleMenu_2.add_command(label = "어둡게", command = func_darken)
handleMenu_2.add_command(label = "선명하게", command = func_clear)
handleMenu_2.add_command(label = "탁하게", command = func_blur)
handleMenu_2.add_command(label = "흑백", command = func_bw)

window.mainloop()