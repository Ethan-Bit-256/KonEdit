""" Importing Tkinter """
import tkinter
from tkinter import *

""" Declaring the main Window variable """
MainWindow = tkinter.Tk()

""" Dimensions and Title """
MainWindow.geometry("400x400")
MainWindow.minsize(height=300, width=300)
MainWindow.title("KonEdit")

""" The Scrollbar """
Scroll = Scrollbar(MainWindow)
Scroll.pack(side=RIGHT, fill=Y)

