# Importing all the required python Library

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import connection
import reg
from SchholRecords import Students_records


class Login_System:
    """Making class for login which defines the object"""

    def __init__(self):  # Making Function using __init__ method as a constructor for the object
        self.root = Tk()
        self.root.title("LOGIN")  # To create a window for the login
        self.root.geometry("1000x900+400+50")
        self.root.resizable(False, False)

        ###============IMAGES===============###
        self.img = '.school.png'  # inserting image
        self.bg_drop = ImageTk.PhotoImage(Image.open(self.img))
        self.bg_image = Label(self.root, image=self.bg_drop).place(x=0, y=0, relwidth=1, relheight=1)

        ###===========FRAME=============####
        # These are made to give graphical visuality to the program
        Frame_outline = Frame(self.root, bg="medium blue")
        Frame_outline.place(x=200, y=150, height=450, width=600)
        Frame_login = Frame(Frame_outline, bg="white")
        Frame_login.place(x=20, y=25, height=400, width=560)
        Frame_banner = Frame(Frame_login, bg="dark blue")
        Frame_banner.place(x=0, y=50, height=10, width=600)
        Frame_banner1 = Frame(Frame_login, bg="medium blue")
        Frame_banner1.place(x=0, y=65, height=6, width=600)
        Frame_banner2 = Frame(Frame_login, bg="medium blue")
        Frame_banner2.place(x=0, y=382, height=5, width=600)
        Frame_banner3 = Frame(Frame_login, bg="dark blue")
        Frame_banner3.place(x=0, y=390, height=5, width=600)

        ####Login Frame####
        # All the entities that are used while login in are created below

        title = Label(Frame_login, text="Login Here",
                      font=("Impact", 35, "bold"), fg="mediumblue", bg="grey").place(x=90, y=30)
        desc = Label(Frame_login, text="Student Management Portal",
                     font=("arial", 15, "bold"), fg="darkorange", bg="white").place(x=190, y=87)
        lbl_user = Label(Frame_login, text="Email", font=("goudy", 16, "bold"),
                         fg="black", bg="white")
        lbl_user.place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("arial", 15), bg="whitesmoke")
        self.txt_user.place(x=90, y=180, width=350, height=35)
        lbl_pass = Label(Frame_login, text="Password", font=("goudy", 16, "bold"),
                         fg="black", bg="grey")
        lbl_pass.place(x=90, y=220)
        self.txt_pass = Entry(Frame_login, font=("arial", 15), bg="whitesmoke")
        self.txt_pass.place(x=90, y=260, width=350, height=35)
        signup_btn = Button(Frame_login, text="Sign up", cursor="hand2", font=("goudy", 9), bg="white", fg="black",
                            bd=0, command=self.register)
        signup_btn.place(x=90, y=300)
        login_btn = Button(self.root, text="Login", cursor="hand2", font=("goudy", 14, "bold"), bg="grey", fg="black",
                           relief=GROOVE, command=self.check)
        login_btn.place(x=405, y=550, width=180, height=60)

        self.root.mainloop()

    def check(self):
        """The function below is made to create validation, fetch data from the database
                     and for exceptional handling and it will take user to the SchoolRecords when the user clicks
                     login button """
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "Please enter all the fields", parent=self.root)
        else:
            try:
                user = connection.Students().login(self.txt_user.get(), self.txt_pass.get())
                if user:
                    if connection.Students().login(self.txt_user.get(), self.txt_pass.get()):
                        messagebox.showinfo('Success', 'Welcome to the Students Management Portal')

                        self.root.destroy()
                        root = Tk()
                        obj = Students_records(root)

                else:
                    messagebox.showerror('Error', 'Invalid Id Or Password')

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def register(self):
        """This function below is created to go to the registration form when the user clicks on signup button"""
        try:
            self.root.destroy()
            reg.User_Registration()
        except Exception as es:
            print(es)


Login_System()
