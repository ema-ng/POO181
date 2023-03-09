from tkinter import*
from tkinter import messagebox
import random
import string

def generar ():
    b = [random.choice(a) for i in range(8)]
    print(b)
    




ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")




seccion1 = Frame(ventana, bg="white")
seccion1.pack(expand=True,fill='both')

texto=Label(seccion1,text="ingresa los caracteres:")
texto.pack()

password = ''

contraseña1=StringVar()
contraseña= Entry(seccion1,textvariable=contraseña1)
contraseña.pack()

c=str(contraseña1.get)
a= [str(c)]
crear= Button(seccion1,text="crear", fg="black",command=generar)
crear.pack()


ventana.mainloop()
