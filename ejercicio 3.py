
from tkinter import*
from tkinter import messagebox

def registrar():
    messagebox.showinfo("registro exitoso",f'el producto es: {nombre.get()} \n precio: {precio.get()}\n hay {existencia.get()} en inventario')

root=Tk()
root.config(bd=15)

nombre=StringVar()
precio=StringVar()
existencia=StringVar()


Label(root, text="nombre del producto").pack()
Entry(root, justify="center",textvariable=nombre).pack()

Label(root, text="precio").pack()
Entry(root, justify="center",textvariable=precio).pack()

Label(root, text="existencia").pack()
Entry(root, justify="center",textvariable=existencia).pack()

Label(root, text="").pack()

Button(root, text="registrar",command=registrar).pack()


root.mainloop()


