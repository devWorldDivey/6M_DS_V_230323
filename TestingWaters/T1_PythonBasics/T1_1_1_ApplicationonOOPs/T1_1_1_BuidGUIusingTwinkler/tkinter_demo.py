from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Login Form")
root.iconbitmap("i1.ico")
root.minsize(400,400)
root.geometry("200x500")
root.configure(background="#0096DC")
img = ImageTk.PhotoImage(Image.open("Vanamo_Logo.png"))
resized_img = img.resize(10,10)
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady= (10,10))





root.mainloop()