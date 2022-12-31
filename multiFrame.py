from tkinter import *
from PIL import ImageTk, Image
import time
import cv2
import easyocr
import threading
import sqlite3
import os
from tkinter import messagebox


class create_frame:
	def __init__(self,root):
		self.root= root
		
		self.root.geometry("800x600+0+0")
		self.root.title("ANPD")
		#self.root.configure(bg="white")
		self.forframe1 = Frame(self.root,bd = 10,relief = GROOVE,bg = 'white').place(x=20,y = 50,width = 340,height = 220)
		self.forFrame2 = Frame(self.root,bd = 10,relief = GROOVE,bg = 'white').place(x= 430,y=50,width = 340,height = 218)
		#Button(self.root,text= "OpEn CaMeRA",command = self.new).pack()
		Label(self.root,text="ANPD-Plate recognization software",font=("Helvetica",18),bg='black',fg='white').pack()
		Button(self.root,text = "window",command = self.newopenw).pack()
		#Button(self.forframe1, text= "window",command = self.img).pack()
		Button(self.forFrame2,text = "CAPTURE AND STORE ",bg = 'white',command= self.capture_and_store).place(x=510,y=132)
		Button(self.forframe1,bd = 8 ,text="Live Detection",bg = 'white',relief = SUNKEN,command=self.img).place(x =127,y=125)
		#self.licence_no  = StrignVar()
		self.reader = easyocr.Reader(['en'])
		self.image_frame = Frame(self.root,bd=15,bg = 'white').place(x =300,y=300,width =240, height=120)
		image = Image.open("ex.png")
		photo = ImageTk.PhotoImage(image.resize((240, 120), Image.Resampling.LANCZOS) )# it is inavlid by pillow 10 Image.ANTIALIAS))
		label = Label(self.image_frame, image=photo, bg='green')
		label.image = photo
		label.place(x=300,y =300)
		r = self.reader.readtext("ex.png",detail=0)
		r = "Sample:"+str(r)
		Label(self.root,text = r,fg = "green", font=("Helvetica",18)).place(x = 300 ,y = 440)
		
		self.flag = 0
	def newopenw(self):
		os.system("python 2frames.py")	
	def img(self):
		tk = Toplevel()
		tk.geometry("1300x700+0+0")
		
		tk.title("Multi frame")
		

		self.f1 = Frame(tk,bd = 10,relief =GROOVE)
		self.f1.place(x=0,y=0,width= 1300,height = 50)
		self.s = StringVar()
		self.s.set("default") 
		self.l = Label(tk,textvariable = self.s).pack()
		cap = cv2.VideoCapture(0)
		
		def label_check():
			self.s.set("changed") 
			self.f1.update()
			#self.root.update()
		
		#Button(self.f1,text = "Total",command = label_check).pack()
		def exit_btn():
        		tk.destroy()
        		tk.update()
        		#cv2.destroyAllWindows()
        		cap.release()
			
		Button(self.f1,text = "Exit ",command = exit_btn).pack()
		f2 = Frame(tk,bd = 8,relief = GROOVE,bg = "white")
		f2.place(x=0,y=50,width =900,height = 530)
		
		
		
		def show_camera():
			
			#label.grid(row=0,column = 0)
			label = Label(f2)
			label.grid(row=3, column=3)
			#cap = cv2.VideoCapture(0)
			face_cascde = cv2.CascadeClassifier('haarcascade_numberplate.xml')
			def show_frames():
			   # Get the latest frame and convert into Image
			   ret, frame = cap.read()
			   face_rects = face_cascde.detectMultiScale(frame,scaleFactor=1.3, minNeighbors=3)
			   
			   for (x,y,w,h) in face_rects:
			   	 cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 4)
			   	 cv2.imwrite('img.png', frame[y:y+h,x:x+w])
			   	 #threading.Thread(target=self.show_img()).start()
			   	 show_img()
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
			   f2.update()	
			 
			show_frames()
			#cap.release()
			f2.update()
			
		Button(f2,bd = 8 ,text="open camera",relief = SUNKEN,command=show_camera).place(x =400,y=0)
		
		
		f3 = Frame(tk,bd = 8 ,relief = GROOVE,bg = "white")
		f3.place(x = 900,y = 50,width= 400,height = 650)
		self.i = "0"
		frame = Frame(f3, width=300, height=200)
		frame.place(x=20, y = 30)
		#frame.place(anchor='center', relx=0.5, rely=0.5)
		
		f4  = Frame(tk,bd = 8,relief = GROOVE,bg = "white")
		f4.place(x  = 0 ,y= 580,width = 900,height = 120)
		
		
		
		def show_img():

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
			label = Label(frame, image=photo, bg='green')
			label.image = photo
			label.place(x=x,y =y)
			#time.sleep(5)
			#reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
			#result = reader.readtext('img.png',detail=0)
			#print(result)
			f3.update()
		Button(f3,text = "SHOW",relief=SUNKEN,command = show_img).pack()
		#Button(self.f3,text = "SHOW",relief=SUNKEN,command = self.show_img).pack()
		self.i = 0
		'''image = Image.open("1.jpg")
		photo = ImageTk.PhotoImage(image.resize((196, 196), Image.ANTIALIAS))
		label = Label(f2, image=photo, bg='green')
		label.image = photo
		label.pack()'''
		#self.show_camera()
		
		
		
			
		def show_label():
			if(i == "0"):
				i = "1"
			else:
				i = "0"
			Button(f3,text = i).place(x=0,y=0)
			
	def capture_and_store(self):
		tk = Toplevel()
		tk.geometry("1300x700+0+0")
		
		tk.title("Multi frame")
		cap = cv2.VideoCapture(0)

		self.f1 = Frame(tk,bd = 10,relief =GROOVE)
		self.f1.place(x=0,y=0,width= 1300,height = 50)
		self.s = StringVar()
		self.s.set("default") 
		self.l = Label(tk,textvariable = self.s).pack()
		def exit_btn():
        		tk.destroy()
        		tk.update()
        		#cv2.destroyAllWindows()
        		cap.release()
		
		def label_check():
			self.s.set("changed") 
			self.f1.update()
			#self.root.update()
		Button(self.f1,text = "Exit",command = exit_btn).pack()	
		
		
		f2 = Frame(tk,bd = 8,relief = GROOVE,bg = "white")
		f2.place(x=0,y=50,width =660,height = 500)
		#cap = cv2.VideoCapture(0)
		f4  = Frame(tk,bd = 8,relief = GROOVE,bg = "white")
		f4.place(x  = 0 ,y= 550,width = 660,height = 150)
		show = StringVar()
		show.set("")
		ss = StringVar()
		ss.set("")
		Label(f4,textvariable = show,relief = GROOVE,font=("Helvetica",18)).place(x=190,y=100,width = 220)
		Label(f4,textvariable = ss,relief = GROOVE,font=("Helvetica",18)).place(x=190,y=20,width = 220)
		def show_text():
			result = self.reader.readtext("cap.png",detail=0)
			ss.set(str(result))
			print(result)
		
		
		def show_camera():
			
			#label.grid(row=0,column = 0)
			
			def change():
				self.flag  = 1
			Button(f2,text="Capture",command = change,relief = GROOVE,font=("Helvetica",15)).place(x = 0,y= 0)
			
			label = Label(f2)
			label.pack()
			face_cascde = cv2.CascadeClassifier('haarcascade_numberplate.xml')
			def show_frames():
			   # Get the latest frame and convert into Image
			   ret, frame = cap.read()
			   face_rects = face_cascde.detectMultiScale(frame,scaleFactor=1.3, minNeighbors=3)
			   
			   if self.flag==1:
			   	self.flag = 0
			   	for (x,y,w,h) in face_rects: 
			   		cv2.imwrite('cap.png', frame[y:y+h,x:x+w])
			   	show_text()
				
			   cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
			   #ret,cv2image = cap.read()
			   img = Image.fromarray(cv2image)
			   # Convert image to PhotoImage
			   imgtk = ImageTk.PhotoImage(image = img)
			   label.imgtk = imgtk
			   label.configure(image=imgtk)
			   # Repeat after an interval to capture continiously
			   label.after(20, show_frames)
			   f2.update()	
			 
			show_frames()
			#cap.release()
			f2.update()	
			
		Button(f2,bd = 8 ,text="open camera",relief = SUNKEN,command=show_camera).pack()
		
		f3 = Frame(tk,bd = 8 ,relief = GROOVE,bg = "black")
		f3.place(x = 700,y = 50,width= 600,height = 650)
		self.i = "0"
		Label(f3,text = "Enter Licence Plate Number",fg= "White",bg = "black",font=("Helvetica",18)).pack()
		licence_no = StringVar()
		Entry(f3,fg="red",textvariable=licence_no,relief = GROOVE,font=("Helvetica",18)).place(x=150,y=50,width = 300)
		def store_in():
			s = licence_no.get()
			#print(type(s))
			#s = "".join(s)
			print(s)
			try:
				conn = sqlite3.connect("tutorial.db")
				cur = conn.cursor()
				sql = '''insert into licence_plate(num) values(?)'''
				cur.execute(sql,(s,))
				conn.commit()
				cur.execute("select * from licence_plate")
				print(cur.fetchall())
			#conn.close()
			except:
				messagebox.showerror("Error","Invalid Input or conncetion",parent=tk)
			
				
			licence_no.set("")
		#frame.place(anchor='center', relx=0.5, rely=0.5)
		Button(f3,bg="black",fg="white",text = "SAVE ",command = store_in,relief = GROOVE,font=("Helvetica",18)).place(x=190,y=100,width = 220)
		
		
		

root = Tk()
create_frame(root)
root.mainloop()

