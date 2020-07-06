

'''
from Tkinter import Label,Tk
from PIL import Image, ImageTk
import tkFileDialog
root = Tk()

path=tkFileDialog.askopenfilename(filetypes=[("Image File",'.jpg')])
im = Image.open(path)
tkimage = ImageTk.PhotoImage(im)
myvar=Label(root,image = tkimage)
myvar.image = tkimage
myvar.pack()

root.mainloop()
'''
from Tkinter import *
from Tkinter import Label,Tk
from PIL import Image, ImageTk
ventana = Tk()
ventana.geometry("1000x700")
ventana.title("Menus")
PILFile = Image.open("image.jpg")
Image = ImageTk.PhotoImage(PILFile)
imagenL = Image
lblImagen=Label(ventana, image=imagenL).place(x=100,y=100)
ventana.mainloop()