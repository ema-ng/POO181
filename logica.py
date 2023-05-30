from tkinter import*

def sumar():
    r.set(float(n1.get())+float(n2.get()))

def resta():
    r.set(float(n1.get())-float(n2.get()))

def producto():
    r.set(float(n1.get())+float(n2.get()))

def borrar():
    n1.set("")
    n2.set("")
    r.set("")

root=Tk()
root.config(bd=15)

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root, text="numero 1").pack()
Entry(root, justify="center",textvariable=n1).pack()

Label(root, text="numero 2").pack()
Entry(root, justify="center",textvariable=n2).pack()

Label(root, text="resultado").pack()
Entry(root, justify="center",textvariable=r,state="disabled").pack()

Label(root, text="").pack()

Button(root, text="sumar",command=sumar).pack(side="left")
Button(root, text="resta",command=resta).pack(side="left")
Button(root, text="producto",command=producto).pack(side="left")
Button(root, text="borrar",command=borrar).pack(side="left")

root.mainloop()