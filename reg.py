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