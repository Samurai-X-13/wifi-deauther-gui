from tkinter import *

def start():
	print("ok")

def sqlmap():
    window = Tk()
    window.title("13 dos")
    window.geometry("300x200+10+20")
    window.configure(bg="grey")

    btn = Button(window, text="Go", fg="black", bg="red", borderwidth=0,
                 activebackground="red", highlightthickness=0, command=start)
    btn.place(x=240, y=21)

    site = Entry(window, width=15, bg="grey", highlightthickness=0, fg="red")
    site.place(x=75, y=24)

    txt1 = Label(window, text="Address:", fg="red", bg="grey")
    txt1.place(x=7, y=23.3)


    window.mainloop()