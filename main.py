from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import pymysql
import sql
from datetime import datetime
import numpy as np
import pandas as pd

window = tkinter.Tk()
window.title("Stock Management System")
window.geometry("820x640")
my_tree = ttk.Treeview(window, show = 'headings', height = 20)
style = ttk.Style()


placeholderArray = ['','','','','']

for i in range(0, 5):
    placeholderArray[i] = tkinter.StringVar()


dummydata = [
    
    ['125123', '123sd', '123sd', '123sd', '123sd', '123sd'],
    ['123sds11223', '123sd', '123sd', '123sd', '123sd', '123sd'],
    ['123s123', '123sd', '123sd', '123sd', '123sd', '123sd'],
    ['123a123', '123sd', '123sd', '123sd', '123sd', '123sd'],
    ['123b123', '123sd', '123sd', '123sd', '123sd', '123sd'],
    ['123c123', '123sd', '123sd', '123sd', '123sd', '123sd'],
    ['123d123', '123sd', '123sd', '123sd', '123sd', '123sd'],

]

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in dummydata:
        my_tree.insert(parent = '', index = 'end', iid = array, text = "", values = (array), tags="orow")
    my_tree.tag_configure('orow', background = "#EEEEEE")
    my_tree.pack()

frame = tkinter.Frame(window, bg = "#02577A")
frame.pack()

btnColor = "#196E78"

manageFrame = tkinter.LabelFrame(frame, text = "Manage", borderwidth=5)
manageFrame.grid(row = 0, column = 0, sticky ="w", padx=[10, 200], pady = 20, ipadx=[6])

saveBtn = Button(manageFrame, text ="SAVE", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')
updateBtn = Button(manageFrame, text ="UPDATE", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')
deleteBtn = Button(manageFrame, text ="DELETE", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')
selectBtn = Button(manageFrame, text ="SELECT", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')
findBtn = Button(manageFrame, text ="FIND", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')
clearBtn = Button(manageFrame, text ="CLEAR", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')
exportBtn = Button(manageFrame, text ="EXPORT EXCEL", width = 10, borderwidth = 10, bg = btnColor, fg = 'white')

saveBtn.grid(row = 0, column = 0, padx = 5, pady = 5)
updateBtn.grid(row = 0, column = 1, padx = 5, pady = 5)
deleteBtn.grid(row = 0, column = 2, padx = 5, pady = 5)
selectBtn.grid(row = 0, column = 3, padx = 5, pady = 5)
findBtn.grid(row = 0, column =4, padx = 5, pady = 5)
clearBtn.grid(row = 0, column = 5, padx = 5, pady = 5)
exportBtn.grid(row = 0, column = 6, padx = 5, pady = 5)

entriesFrame = tkinter.LabelFrame(frame, text = 'Form', borderwidth = 5)
entriesFrame.grid(row = 1, column = 0, sticky = "w", padx=[10, 200], pady = [0, 20], ipadx = [6])

itemIdLabel = Label(entriesFrame, text = "ITEM ID", anchor ="e", width = 10)
nameLabel = Label(entriesFrame, text = "NAME", anchor ="e", width = 10)
priceLabel = Label(entriesFrame, text = "PRICE", anchor ="e", width = 10)
qntLabel = Label(entriesFrame, text = "QNT", anchor ="e", width = 10)
categoryLabel = Label(entriesFrame, text = "CATEGORY", anchor ="e", width = 10)

itemIdLabel.grid(row = 0, column = 0, padx = 10)
nameLabel.grid(row = 1, column = 0, padx = 10)
priceLabel.grid(row = 2, column = 0, padx = 10)
qntLabel.grid(row = 3, column = 0, padx = 10)
categoryLabel.grid(row = 4, column = 0, padx = 10)

categoryArray = ['Networking Tools', 'Computer Parts', 'Repair tools', 'Gadgets']

itemIdEntry = Entry(entriesFrame, width = 50, textvariable = placeholderArray[0])
nameEntry = Entry(entriesFrame, width = 50, textvariable = placeholderArray[1])
priceEntry = Entry(entriesFrame, width = 50, textvariable = placeholderArray[2])
qntEntry = Entry(entriesFrame, width = 50, textvariable = placeholderArray[3])
categoryCombo = ttk.Combobox(entriesFrame, width = 47, textvariable = placeholderArray[4], values = categoryArray)

itemIdEntry.grid(row = 0, column = 2, padx = 10)
nameEntry.grid(row = 1, column = 2, padx = 10)
priceEntry.grid(row = 2, column = 2, padx = 10)
qntEntry.grid(row = 3, column = 2, padx = 10)
categoryCombo.grid(row = 4, column = 2, padx = 10)

generateIdBtn = Button(entriesFrame, text = "GENERATE ID", borderwidth=3, bg = btnColor, fg = "white")
generateIdBtn.grid(row = 0, column = 1, padx = 5, pady = 5)

style.configure(window)

my_tree['columns'] = ("Item Id", "Name", "Price", "Quantity", "Category", "Date")


my_tree.column('#0', width = 0, stretch = NO)
my_tree.column("Item Id", anchor = W, width = 70)
my_tree.column("Name", anchor = W, width = 70)
my_tree.column("Price", anchor = W, width = 70)
my_tree.column("Quantity", anchor = W, width = 70)
my_tree.column("Category", anchor = W, width = 70)
my_tree.column("Date", anchor = W, width = 70)

my_tree.heading("Item Id", text = "Item Id", anchor = W)
my_tree.heading("Name", text = "Name", anchor = W)
my_tree.heading("Price", text = "Price", anchor = W)
my_tree.heading("Quantity", text = "Quantity", anchor = W)
my_tree.heading("Category", text = "Category", anchor = W)
my_tree.heading("Date", text = "Date", anchor = W)

#15:46

refreshTable()

window.resizable(False, False)
window.mainloop()

