""" Required Imports """
from MainWindow import *
from OpenSave import *

""" Declaring the Menubar """
MenuBar = Menu(MainWindow)

""" Declaring the File Menu """
File = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label = 'File', menu = File)

""" The Open Button, which uses the OpenFile() function delcared in OpenSave.py """
File.add_command(label = "Open", command = OpenFile)

""" The Save Button, which uses the SaveFile() function delcared in OpenSave.py """
File.add_command(label = "Save", command = SaveFile)

""" The Exit Button, which closes the application """
File.add_command(label = "Exit", command = MainWindow.destroy)
