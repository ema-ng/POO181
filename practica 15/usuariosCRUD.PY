
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()

agregar = Frame(note,width=400,height=400)
agregar.pack(expand=True,fill='both')
buscar = Frame(note,width=400,height=400)
buscar.pack(expand=True,fill='both')
consultar = Frame(note,width=400,height=400)
consultar.pack(expand=True,fill='both')
actualizar = Frame(note,width=400,height=400)
actualizar.pack(expand=True,fill='both')


note.add(agregar,text="agregar Usuario")
note.add(buscar,text="Buscar Usuario")
note.add(consultar,text="Consultar Usuario")
note.add(actualizar,text="Actualizar Usuario")

titulo = Label(agregar,text="Registro de usuario",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(agregar,text="nombre")
texto.pack()

nombre=StringVar()
nombre1=Entry(agregar,textvariable=nombre)
nombre1.pack()

texto=Label(agregar,text="correo")
texto.pack()

correo=StringVar()
correo1=Entry(agregar,textvariable=correo)
correo1.pack()


texto=Label(agregar,text="contraseña")
texto.pack()

contraseña=StringVar()
contraseña1=Entry(agregar,textvariable=contraseña)
contraseña1.pack()

boton=Button(agregar,text="agregar")
boton.pack()

ventana.mainloop()