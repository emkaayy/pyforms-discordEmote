import tkinter as tk
from tkinter import *
from tkinter import ttk
import PIL
import PIL.Image
import PIL.ImageTk

start_coords = []
squarex = 0
squarey = 0

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

frame = ttk.Frame(root, padding="1 1 1 1")

# create canvas
# adjust canvas from image res
canvas = Canvas(root, width=496, height=480)
canvas.pack()

canvas.bind('<B1-Motion>', motion)

# display image
# change image to be selected image
image = PIL.Image.open("Bea_hajiraia2.png")
imagetk = PIL.ImageTk.PhotoImage(image)
canvas.create_image(20, 20, anchor=NW, image=imagetk)

# draw selection square
square = canvas.create_rectangle(squarex, squarey, 128, 128, fill="black", outline="gray", width=3, stipple='gray25')

root.mainloop()

# export image
croppedimage = image.crop((squarex, squarey, squarex+128, squarey+128))
croppedimage.save(image.filename.split("\\")[-1].split(".")[0] + "_cropped." + image.filename.split("\\")[-1].split(".")[1])