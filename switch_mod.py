from tkinter import *

root = Tk()
root.title("Switch mode")
root.geometry("400x600")
root.config(background="white")

Button_mode = True

def switch():
    global Button_mode
    if Button_mode:
        button.config(image=off, bg="#26242f", activebackground="#26242f")
        root.config(bg="#26242f")
        Button_mode = False
    else:
        button.config(image=on, bg="white", activebackground="white")
        root.config(bg="white")
        Button_mode = True

on = PhotoImage(file='light.png')
off = PhotoImage(file='dark.png')

button = Button(root, image=on, bd=0, bg="white", activebackground="white", command=switch)
button.place(x=90, y=50)

root.mainloop()
