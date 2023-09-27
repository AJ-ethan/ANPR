from tkinter import *
import cv2
from PIL import Image, ImageTk

class gui:
	def __init__(self,root):
		self.root= root
		
		self.root.geometry("800x600+0+0")
		self.root.title("HElo")
		Button(self.root,text= "OpEn CaMeRA",command = self.new).pack()
		Button(self.root,text = "window",command = self.img).pack()
	def new(self):
		vid = cv2.VideoCapture(0)
  
		while(True):
			ret,frame= vid.read()
			cv2.imshow('frame', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		  
		vid.release()
		cv2.destroyAllWindows()
	def img(self):
		tk = Toplevel()
		#canvas = Canvas(tk,height=700,width = 500)
		#canvas.pack()
		Button(tk,text = "close",command = tk.destroy).grid(row = 0,column = 0)
		#fr = Frame(tk,bd=10)
		#fr.place(x=0,y = 40,height=300,width=500)
		label =Label(tk)
		label.grid(row=3, column=0)
		cap= cv2.VideoCapture(0)

		# Define function to show frame
		def show_frames():
			# Get the latest frame and convert into Image
			cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
			#ret,cv2image = cap.read()
			img = Image.fromarray(cv2image)
			# Convert image to PhotoImage
			imgtk = ImageTk.PhotoImage(image = img)
			label.imgtk = imgtk
			label.configure(image=imgtk)
			# Repeat after an interval to capture continiously
			label.after(20, show_frames)

		show_frames()
		tk.mainloop()
		#cap.release()
		#cv2.destroyAllWindows()
				
root = Tk()
gui(root)
root.mainloop()

