
from tkinter import * 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from crontoladorBD import* #1. presentar archivo contolador

#2.crear objeto de la clase controlador

controlador=controladorBD()

#3.funcion para disparar el boton

def ejecutainsert():
    
    controlador.guardarusuario(nombre.get(),correo.get(),contraseña.get())

def ejecutarselect():
    usuario=controlador.consultar(varbus.get())
    for usu in usuario:
        cadena= str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+str(usu[3]) 
    
    if(usuario):
        
        print(cadena)
        texto.insert(tk.INSERT,cadena)
        
        
        
    else:
        messagebox.showwarning("no encontrado","ese usuario no existe")
    
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

boton=Button(agregar,text="agregar",command=ejecutainsert)
boton.pack()


#pestaña 2 buscar usuario 

titulo = Label(buscar,text="Registro de usuario",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(buscar,text="identificar usuario")
texto.pack()

varbus=StringVar()
subbus=Entry(buscar,textvariable=varbus)
subbus.pack()

botonb=Button(buscar,text="buscar",command=ejecutarselect)
botonb.pack()

titulo = Label(buscar,text="encontrado",fg='Blue',font=("modern",18))
titulo.pack()
texto=Text(buscar,height=5,width=52)

texto.pack()



ventana.mainloop()