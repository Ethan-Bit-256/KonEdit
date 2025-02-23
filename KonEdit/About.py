""" Required imports """
from MainWindow import *

""" Declaring the function for the about window """
def AboutWindow():
    About = Tk()
    About.geometry("300x300")
    About.wm_title("About KonEdit")
    About.resizable(False, False)

""" The version text in the middle of it all """
    Version = Label(About, text="KonEdit 0.1.1")
    Version.pack(side="top", fill="both", expand=True, padx=100, pady=100)
