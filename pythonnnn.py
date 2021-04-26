from tkinter import *
import sqlite3

win= Tk()
win.title("database")

#database

#creating a database or connect to one

conn= sqlite3.connect("address_book.db")
#
# #creating cursor
# #cursor class is an instance using which you can invoke using method that executes SQLITE,
# #fetch data from results sets of queries
#
# curser= conn.cursor()
# curser.execute("""CREATE TABLE student_data(
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zipcode integer
# """)
# print("table created successfully")

#creating function
