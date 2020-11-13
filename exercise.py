from tkinter import *


glass = Tk()
glass.title("AUTHENTIFICATION")
glass.geometry("450x400+120+120")
glass.configure(background="purple")

def exception():
    top = Toplevel()
    top.title("Exception Handling")
    top.geometry("400x300")
    label1 = Label(top, text="Please enter amount in your account:")
    label1.pack(row=1, column=0, columnspan=4, padx=12, ipady=14, rowspan=4)
    button = Button(top, text="Check Qualification", command=feed)
    button.pack()

def feed():
    top_fin = Toplevel()
    top_fin.title("Status Feedback")
    top_fin.geometry("400x300")



button = Button(glass, text="Login", command=exception)
button.pack()


glass.mainloop()