from cgitb import text
import string
from tkinter import*


def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = 'Error'

        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("260x550")
root.title("Calculator")
# p1 = PhotoImage(file='Mycalculator.png')
# root.iconphoto(True, p1)
root.resizable(False, False)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="Cascadia 25")
screen.pack(fill=X, ipadx=10, pady=12, padx=20)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT,  pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="7", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT,  pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="4", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="3", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT,  pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=14, pady=3, font="Cascadia 25")
b.pack(side=LEFT,  pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="+", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=2)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="/", padx=14, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=13, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=0.5, pady=2)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=10, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=5, pady=2)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="C", padx=6, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=6, pady=3)
b.bind("<Button-1>", click)
b = Button(f, text="%", padx=4, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=1, pady=3)
b.bind("<Button-1>", click)
b = Button(f, text=".", padx=15, pady=3, font="Cascadia 25")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()
