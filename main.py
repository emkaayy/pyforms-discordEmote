import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import PIL
import PIL.Image
import PIL.ImageTk

start_coords = []
squarex = 0
squarey = 0
displayImage = ""
filename = ""
mydict = {"imagetk": None}

def imageSelect(r):
    global filename
    filename = filedialog.askopenfile()
    filename = filename.name
    image = PIL.Image.open(filename)
    r["imagetk"] = PIL.ImageTk.PhotoImage(image)
    canvas.itemconfig(displayImage, image=r['imagetk'])
    return filename

def motion(e):
    global squarex
    global squarey
    x = e.x
    y = e.y
    canvas.moveto(square, x, y)
    squarex = x
    squarey = y

root = Tk()
root.title = "Discord Emoji Cropper and Exporter"

menu = Menu(root)

def mywrapper():
    imageSelect(mydict)

filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="open", command=mywrapper)
filemenu.add_command(label="exit", command=root.quit)

menu.add_cascade(label="file", menu=filemenu)

frame = ttk.Frame(root, padding="1 1 1 1")

# change image to be selected image

# adjust canvas from image res

# create canvas
canvas = Canvas(root, width=496, height=480)
canvas.pack()

canvas.bind('<B1-Motion>', motion)

# display image
filename = imageSelect(r=mydict)
print("filename: " + filename)
image = PIL.Image.open(filename)
imagetk = PIL.ImageTk.PhotoImage(image)
displayImage = canvas.create_image(20, 20, anchor=NW, image=imagetk)

# draw selection square
square = canvas.create_rectangle(squarex, squarey, 128, 128, fill="black", outline="gray", width=3, stipple='gray25')

root.config(menu=menu)
root.mainloop()

# export image
croppedimage = image.crop((squarex, squarey, squarex+128, squarey+128))
croppedimage.save(image.filename.split("\\")[-1].split(".")[0] + "_cropped." + image.filename.split("\\")[-1].split(".")[1])