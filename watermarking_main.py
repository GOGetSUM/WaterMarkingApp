import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw
import numpy as np


#------------------------------------Photo Overlay & Text Water Mark------------------------------------------
def watermark():
    img = Image.open(f'{filepath_var.get()}')
    logo = Image.open(f'{logo_var.get()}')
    watermark = text_entry.get()
    print(logo.size)
    #resize image
    size=logo.size
    img = img.resize(size,Image.Resampling.LANCZOS)
    img.paste(logo,(0,0),logo)
    img.save(f'{filepath_var.get()}-{logo_var.get()}.png')
    imag_=f'{filepath_var.get()}-{logo_var.get()}.png'
    # TEXT WATERMARK
    with Image.open(imag_) as im:
        width, height = im.size
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('arial.ttf', 40)
        text_width, text_height = draw.textsize(watermark, font)
        margin = 20
        x = width - text_width - margin
        y = height - text_height - margin
        color = kolor()
        draw.text((x, y), watermark, color, font=font)
        im.show()
        place = f"{imag_[:-4]}-WATERMARK{imag_[-4:]}"
        im.save(place)
        preview(place)

def kolor():
    if kol.get() == 1:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

def preview(photo):
    top = Toplevel(window)
    top.geometry("750x500")
    top.title("Preview")
    top.wm_attributes("-transparentcolor", 'grey')
    # --------------------------------------Pop Up window is Image-------------------------------------------------
    bg_ = PhotoImage(file=photo)
    user_img = Label(top, image=bg_,background='grey')
    user_img.image = bg_
    user_img.place(x=0, y=0,)



#------------------------------------GUI----------------------------------------------------
window = Tk()
window.title("Watermarker")
window.config(padx=50, pady=50)
window.geometry("750x650")


filepath_var = StringVar() #declaring variable for file path
logo_var = StringVar()

canvas = Canvas(height=240, width=325)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(160, 110, image=logo_img)
canvas.grid(row=0, column=1)

title_label = Label(text="Enter the file path to image & logo you would like to mark with,\n"
                         " (optional) you can also add text or not.")
title_label.grid(column=1,row=1,columnspan=2)

picture_location_label = Label(text="Picture location (filepath):").grid(row=2, column=0)
what_text_label = Label(text="Text of ur watermark:").grid(row=3, column=0)
logo_label = Label(text="Logo File location (filepath):").grid(row=4,column=0)

picture_location_entry = Entry(textvariable=filepath_var,width=54)
picture_location_entry.grid(row=2, column=1)
picture_location_entry.focus()

text_entry = Entry(width=54)
text_entry.grid(row=3, column=1)
text_entry.focus()

logo_entry = Entry(textvariable=logo_var,width=54)
logo_entry.grid(row=4, column=1)
logo_entry.focus()

kol = tkinter.IntVar()
c = tkinter.Checkbutton(window, text="Black watermark", variable = kol, onvalue=1, offvalue=0)
c.grid(row=5, column=0)

add_button = Button(text="Add watermark to picture", width=46,command=watermark).grid(row=5, column=1, columnspan=2)
quit_button = Button(text="Quit", command=window.destroy).grid(column=1, row=6)

window.mainloop()