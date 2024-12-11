""" Required Imports """
from tkinter.filedialog import askopenfilename, asksaveasfilename
from MainWindow import *
from Editor import *

""" The OpenFile function which allows KonEdit to open and read files """
def OpenFile():
    FilePath = askopenfilename()
    if not FilePath:
        return
    EditArea.delete(1.0, tkinter.END)
    with open(FilePath, "r") as input_file:
        Text = input_file.read()
        EditArea.insert(tkinter.END, Text)

""" The SaveFile function which allows KonEdit to write files """
def SaveFile():
    FilePath = asksaveasfilename()
    if not FilePath:
        return
    with open(FilePath, "w") as output_file:
        Text = EditArea.get(1.0, tkinter.END)
        output_file.write(Text)
