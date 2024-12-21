from MainWindow import *

""" Where the actual text editing will take place """
EditArea = Text(MainWindow, yscrollcommand = Scroll.set)
EditArea.pack(expand=True, fill=BOTH)

""" Making the scrollbar work with the EditArea """
Scroll.config(command=EditArea.yview)
