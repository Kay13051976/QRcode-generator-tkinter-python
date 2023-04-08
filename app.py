from tkinter import *
import pyqrcode
import png
from PIL import ImageTK,Image


def generateQRCode():
    #fletch link to  built QRCode
    link_name = name_entry.get()
    link=link_entry.get()
    file_name=link_name+".png"
    #built QRCode
    url = pyqrcode.create(link)
    url.png(file_name,scale=5)
    #render QRCode
    image = ImageTk,PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,370,window=image_label)


root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root,width=400,height=500)
canvas.pack()

#Program name
app_label = Label(root,text="QRCode Generator",font=("Aril",20,"bold"))
canvas.create_window(200,50,window=app_label)

#name and link
name_label = Label(root,text="QRCode name")
canvas.create_window(200,100,window=name_label)

link_label = Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

#built text box
name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry = Entry(root)
canvas.create_window(200,180,window=link_entry)

#QRCode button
button = Button(text="Built QRCode",command=generateQRCode)
canvas.create_window(200,230,window=button)

root.mainloop()