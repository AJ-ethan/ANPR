from tkinter import * 
from random import randint
from PIL import Image, ImageTk
root=Tk()
lab= Label(root)
lab.pack()

def update():
	#l['text'] = randint(0,1000)
	l = ["2.jpg","1.jpg","3.jpeg"]
	for i in l:
		image = Image.open(i)
		photo = ImageTk.PhotoImage(image.resize((150, 100), Image.ANTIALIAS))
		#label = Label(self.frame, image=photo, bg='green')
		lab["image"] = photo
		#label.place(x=x,y =y)
		root.after(1000,update)
	
update()

root.mainloop()
