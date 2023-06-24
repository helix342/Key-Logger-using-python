# KEYLOGGER
from tkinter import *
window = Tk()

def duck(fickle):
     print(end=" ")
def KeyLogging(jokes):
    print(jokes.keysym,end="")
def Delete(gone):
    window.destroy()
window.bind('<space>', duck)
window.bind('<Key>',KeyLogging)
window.bind('<Escape>',Delete)

window.withdraw()
window.mainloop()
