# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# from tkinter import filedialog
#
# root= Tk()
# root.title('Dialog Box')
# root.iconbitmap('rocket_space_icon_185954.ico')
#
# def open():
#     global my_image
#     root.filename= filedialog.askopenfilename(initialdir="/Downloads", title="Select a file", filetypes=(("png files",
#                                                                             "*.png"),("all files","*.*")))
#     my_label=Label(root, text=root.filename).pack()
#     my_image= ImageTk.PhotoImage(Image.open(root.filename))
#
# my_btn= Button(root,text="Open file",command=open).pack()
#
# root.mainloop()



#slider
# from tkinter import *
# root= Tk()
# root.iconbitmap('rocket_space_icon_185954.ico')

#vertical slider
# vertical= Scale(root, from_=0,to=300)
# vertical.pack()
#
# #horizontal slider
# horizontal = Scale(root, from_=0, to=300, orient= HORIZONTAL)
# horizontal.pack()
#
# def slide():
#     my_label= Label(root, text= horizontal.get()).pack()
#     root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
#
# my_btn= Button(root, text="Click me",command=slide).pack()
#
# root.mainloop()

#check button
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# from tkinter import filedialog
#
# root= Tk()
# root.title('Check Box')
# root.iconbitmap('rocket_space_icon_185954.ico')
#
# def show():
#     myLabel= Label(root, text= var.get()).pack()
#
# var=StringVar()
# checkButton= Checkbutton(root, text="Check this box",variable_=var,onvalue="On",offvalue="Off")
# checkButton.deselect()
# checkButton.pack()
#
# myButton= Button(root, text="Show Selection",command=show).pack()
#
# root.mainloop()

#dropdown menu
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root= Tk()
root.title('Dropdown Menu')
root.iconbitmap('rocket_space_icon_185954.ico')

def show():
    mylabel= Label(root, text=clicked.get()).pack()

clicked= StringVar()
clicked.set("Monday")

drop= OptionMenu(root, clicked, "Monday","Tuesday","Wednesday","Thursday","Friday")
drop.pack()

myButton= Button(root, text="Show Selection", command=show).pack()

root.mainloop()




