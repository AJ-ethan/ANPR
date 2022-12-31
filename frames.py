from tkinter import *
from PIL import ImageTk, Image
import time
import cv2
import easyocr
import threading

class create_frame:
	def __init__(self,root):
		self.root  = root
		self.root.geometry("1300x700+0+0")
		
		self.root.title("Multi frame")
		

		self.f1 = Frame(self.root,bd = 10,relief =GROOVE)
		self.f1.place(x=0,y=0,width= 1300,height = 50)
		self.s = StringVar()
		self.s.set("default") 
		self.l = Label(self.f1,textvariable = self.s).pack()
		Button(self.f1,text = "Total",command = self.label_check).pack()	
		
		self.f2 = Frame(self.root,bd = 8,relief = GROOVE,bg = "white")
		self.f2.place(x=0,y=50,width =900,height = 530)
		Button(self.f2,bd = 8 ,text="open camera",relief = SUNKEN,command=self.show_camera).place(x =400,y=0)
		
		
		self.f3 = Frame(self.root,bd = 8 ,relief = GROOVE,bg = "white")
		self.f3.place(x = 900,y = 50,width= 400,height = 650)
		self.i = "0"
		self.frame = Frame(self.f3, width=300, height=200)
		self.frame.place(x=20, y = 30)
		#frame.place(anchor='center', relx=0.5, rely=0.5)
		
		f4  = Frame(self.root,bd = 8,relief = GROOVE,bg = "white")
		f4.place(x  = 0 ,y= 580,width = 900,height = 120)
		Button(self.f3,text = "SHOW",relief=SUNKEN,command = self.show_img).pack()
		#Button(self.f3,text = "SHOW",relief=SUNKEN,command = self.show_img).pack()
		self.i = 0
		'''image = Image.open("1.jpg")
		photo = ImageTk.PhotoImage(image.resize((196, 196), Image.ANTIALIAS))
		label = Label(f2, image=photo, bg='green')
		label.image = photo
		label.pack()'''
		#self.show_camera()
		
        	
	def show_img(self):

		'''canvas = Canvas(self.frame, width = 220, height = 200)      
		canvas.pack()      
		load = Image.open("1.jpg")
		load = load.resize((220, 180))
		img = ImageTk.PhotoImage(load)  
		canvas.create_image(20, 20, anchor=NW, image=img)  NOT WORKING'''
		'''if self.i == 0:
			l = ["2.jpg","1.jpg","3.jpeg"]
			self.i = 1
		else:
			l = ["3.jpeg","2.jpg","1.jpg"]
			self.i = 0'''
		x = 0
		y=0
		#for i in l:
		image = Image.open("img.png")
		photo = ImageTk.PhotoImage(image.resize((300, 200), Image.Resampling.LANCZOS) )# it is inavlid by pillow 10 Image.ANTIALIAS))
		label = Label(self.frame, image=photo, bg='green')
		label.image = photo
		label.place(x=x,y =y)
		#time.sleep(5)
		#reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
		#result = reader.readtext('img.png',detail=0)
		#print(result)
		self.f3.update()
		
	def show_label(self):
		if(self.i == "0"):
			self.i = "1"
		else:
			self.i = "0"
		Button(self.f3,text = self.i).place(x=0,y=0)
	
	def show_camera(self):
		
		#label.grid(row=0,column = 0)
		label = Label(self.f2)
		label.grid(row=3, column=3)
		cap = cv2.VideoCapture(0)
		face_cascde = cv2.CascadeClassifier('haarcascade_numberplate.xml')
		def show_frames():
		   # Get the latest frame and convert into Image
		   ret, frame = cap.read()
		   face_rects = face_cascde.detectMultiScale(frame,scaleFactor=1.3, minNeighbors=3)
		   
		   for (x,y,w,h) in face_rects: 
        		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 4)
        		cv2.imwrite('img.png', frame[y:y+h,x:x+w])
        		#threading.Thread(target=self.show_img()).start()
        		self.show_img()
        		#time.sleep(100)
        		
		   cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		   #ret,cv2image = cap.read()
		   img = Image.fromarray(cv2image)
		   # Convert image to PhotoImage
		   imgtk = ImageTk.PhotoImage(image = img)
		   label.imgtk = imgtk
		   label.configure(image=imgtk)
		   # Repeat after an interval to capture continiously
		   label.after(20, show_frames)
		   self.f2.update()	
		 
		show_frames()
		self.f2.update()		

	def label_check(self):
		self.s.set("changed") 
		self.f1.update()
		#self.root.update()
		

root = Tk()
create_frame(root)
root.mainloop()

