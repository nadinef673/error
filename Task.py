from tkinter import *

def exception():
    top = Toplevel()
    top.title("Exception Handling")
    top.geometry("400x300")
    button = Button(top, text="Check Qualification", command=feed)
    button.pack(side=BOTTOM)

def feed():
    top_fin = Toplevel()
    top_fin.title("Status Feedback")
    top_fin.geometry("400x300")




window = Tk()

head = Label(window, text="Please enter login details")
head.pack(side=TOP)



button = Button(window, text="Login", command=exception)
button.pack(side=BOTTOM)
window.geometry("500x500+120+120")
window.title("Authentification")




window.mainloop()


