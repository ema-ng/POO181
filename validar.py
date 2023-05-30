
from tkinter import*
from tkinter import messagebox

usuario="alumno"
contra="sistemas2023"

def validar():

    if (nombre.get()==usuario and contraseña.get()==contra):
        messagebox.showinfo("bienvenido","usuario correcto")
    else:
        messagebox.showerror("error","usuario invalido")
        

    
root=Tk()
root.config(bd=15)

nombre=StringVar()
contraseña=StringVar()


Label(root, text="usuario").pack()
Entry(root, justify="center",textvariable=nombre).pack()

Label(root, text="contraseña").pack()
Entry(root, justify="center",textvariable=contraseña).pack()


Label(root, text="").pack()

Button(root, text="verficar",command=validar).pack()


root.mainloop()


