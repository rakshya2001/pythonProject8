from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import connection

class user_registration:
    """Making class for registration which defines the object"""

    def __init__(self):  # Making Function using __init__ method as a constructor for the object
        self.root = Tk()
        self.root.title("User Registration Portal")  # To create a window for the registration
        self.root.geometry("1650x1350+0+0")

        ####=====Image======####
        self.img = 'school.png'  # inserting image
        self.bg = ImageTk.PhotoImage(Image.open(self.img))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        ####==========FRAME==========#####
        # '''These are made to give graphical visuality to the program'''

        Frame_backdrop = Frame(self.root, bg="medium blue")
        Frame_backdrop.place(x=80, y=90, height=680, width=1140)

        Frame_reg = Frame(self.root, bg="white")
        Frame_reg.place(x=100, y=140, height=590, width=1100)

        title = Label(Frame_reg, text="New User Register Here !!!", font=("Impact", 70), bg="white", fg="medium blue")
        title.place(x=20, y=20)

        description = Label(Frame_reg, text="Student Management Portal", font=("goudy", 20, "bold"), bg="white",
                            fg="Dark orange")
        description.place(x=595, y=130)

        ####============COLUMN 1===============##########
        # '''All the entities that are used while registering user in are created below'''

        lbl_fname = Label(Frame_reg, text="First Name", font=("goudy", 18, "bold"), bg="white", fg="black", )
        lbl_fname.place(x=30, y=200)
        self.lbl_fentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="white smoke", relief=GROOVE)
        self.lbl_fentry.place(x=180, y=205, width=300)

        lbl_Lname = Label(Frame_reg, text="Last Name", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_Lname.place(x=30, y=250)
        self.lbl_lentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="white smoke", relief=GROOVE)
        self.lbl_lentry.place(x=180, y=255, width=300)

        lbl_contact = Label(Frame_reg, text="Contact", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_contact.place(x=30, y=300)
        self.lbl_conentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="white smoke", relief=GROOVE)
        self.lbl_conentry.place(x=180, y=305, width=300)

        lbl_Email = Label(Frame_reg, text="Email", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_Email.place(x=30, y=350)
        self.lbl_Emailentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="white smoke", relief=GROOVE)
        self.lbl_Emailentry.place(x=180, y=355, width=300)

        lbl_ques = Label(Frame_reg, text="Security Question", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_ques.place(x=30, y=400)
        self.combo_ques = ttk.Combobox(Frame_reg, font=("arial", 15, "bold"), state="readonly")
        self.combo_ques["values"] = (
            "Select Question", "Your Dream job", "Your Favourite Food", "Your First Pet Name", "Your Favourite Place")
        self.combo_ques.place(x=250, y=405, width=230, height=27)
        self.combo_ques.current(0)  # creating combobox

        ####============COLUMN 2===============##########
        # '''All the entities that are used while registering user in are created below'''

        lbl_pass = Label(Frame_reg, text="Password", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_pass.place(x=550, y=200)
        self.lbl_passentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="whitesmoke", relief=GROOVE)
        self.lbl_passentry.place(x=685, y=205, width=300)

        lbl_cpass = Label(Frame_reg, text="Confirm Password", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_cpass.place(x=550, y=250)
        self.lbl_cpassentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="whitesmoke", relief=GROOVE)
        self.lbl_cpassentry.place(x=780, y=255, width=208)

        lbl_dob = Label(Frame_reg, text="D.O.B", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_dob.place(x=550, y=300)
        self.lbl_dobentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="whitesmoke", relief=GROOVE)
        self.lbl_dobentry.place(x=685, y=305, width=300)

        lbl_gender = Label(Frame_reg, text="Gender", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_gender.place(x=550, y=350)
        self.combo_Gender = ttk.Combobox(Frame_reg, font=("arial", 15, "bold"), state="readonly")
        self.combo_Gender["values"] = ("Select Gender", "Male", "Female", "Other")
        self.combo_Gender.place(x=685, y=355, width=300, height=27)
        self.combo_Gender.current(0)  # creating combobox

        lbl_ans = Label(Frame_reg, text="Answer", font=("goudy", 18, "bold"), bg="white", fg="black")
        lbl_ans.place(x=550, y=400)
        self.lbl_ansentry = Entry(Frame_reg, font=("arial", 14), fg="black", bg="whitesmoke", relief=GROOVE)
        self.lbl_ansentry.place(x=685, y=405, width=300)

        ####=========BUTTONS==============####
        self.var_check = IntVar()
        check = Checkbutton(Frame_reg, variable=self.var_check, text="I  Agree To The Terms And Conditions",
                            onvalue=1, offvalue=0, cursor="hand2", bg="white", font=("goudy", 12))
        check.place(x=30, y=455)

        #####==========BANNER FRAME==========####
        Frame_ban = Frame(Frame_reg, bg="mediumblue")
        Frame_ban.place(x=0, y=505, height=70, width=1100)

        ####==========BUTTONS ABOVE BLUE BANNER=================####

        regbtn = Button(Frame_ban, command=self.register, font=("arial", 12, "bold"), cursor="hand2", text="Register",
                        bg="white", fg="black", width=20)
        regbtn.place(x=290, y=20)

        clrbtn = Button(Frame_ban, font=("arial", 12, "bold"), cursor="hand2", command=self.clear_btn, text="Clear",
                        bg="white", fg="black", width=20)
        clrbtn.place(x=590, y=20)

        ####=======FRAMES FOR CREATING BANNER DESIGN============###
        Frame_ban1 = Frame(Frame_reg, bg="darkorange")
        Frame_ban1.place(x=0, y=180, height=5, width=1100)

        Frame_ban2 = Frame(Frame_reg, bg="darkorange")
        Frame_ban2.place(x=0, y=580, height=8, width=1100)

        Frame_ban3 = Frame(Frame_reg, bg="mediumblue")
        Frame_ban3.place(x=0, y=170, height=8, width=1100)

        def register(self):
            """Function below is created to store all the entered information to th database, to give validation
                and exceptional handling is also done """
            if self.lbl_fentry.get() == "" or self.lbl_lentry.get() == "" or self.lbl_conentry.get() == "" \
                    or self.lbl_Emailentry.get() == "" or self.combo_ques.get() == "Select Question" \
                    or self.lbl_passentry.get() == "" or self.lbl_cpassentry.get() == "" or self.lbl_dobentry.get() == "" \
                    or self.combo_Gender.get() == "Select Gender" or self.lbl_ansentry.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)

            elif self.lbl_passentry.get() != self.lbl_cpassentry.get():
                messagebox.showerror("Error", "Password and Confirm Password must be same", parent=self.root)

            elif self.var_check.get() == 0:
                messagebox.showerror("Error", "Terms and Conditions must be agreed", parent=self.root)
            else:
                try:
                    conn.Students().register_data(self.lbl_fentry.get(),
                                                  self.lbl_lentry.get(),
                                                  self.lbl_conentry.get(),
                                                  self.lbl_Emailentry.get(),
                                                  self.lbl_dobentry.get(),
                                                  self.combo_ques.get(),
                                                  self.lbl_ansentry.get(),
                                                  self.lbl_passentry.get())

                    messagebox.showinfo("Success", "New User Successfully Registered", parent=self.root)

                    self.root.destroy()

                    import log

                except Exception as es:
                    messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

        def clear_btn(self):
            """The function below is made to delete all the entered data from registration form
                 when a user clicks on clear button and exceptional handling is also done"""
            try:

                op = messagebox.askyesno("Clear", "Do you want to clear data?")
                if op > 0:
                    self.lbl_fentry.delete(0, END)
                    self.lbl_lentry.delete(0, END)
                    self.lbl_conentry.delete(0, END)
                    self.lbl_Emailentry.delete(0, END)
                    self.combo_ques.current(0)
                    self.lbl_passentry.delete(0, END)
                    self.lbl_cpassentry.delete(0, END)
                    self.lbl_dobentry.delete(0, END)
                    self.combo_Gender.current(0)
                    self.lbl_ansentry.delete(0, END)
            except Exception as es:
                print(es)

    # root = Tk()
    # obj = User_Registration()
    # root.mainloop()
