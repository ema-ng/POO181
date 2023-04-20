from asyncio import FIRST_EXCEPTION
import threading 
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt
from logica import*

a=logicae()

def insertarobj():
    a.registrar(material.get(),cantidad.get())
    
def actualizarobj():
    a.acuaizar(id.get(),materialn.get(),cantidadn.get())

#crear ventana 

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()


#insertar objetos
    
insertar = Frame(note,width=400,height=400)
insertar.pack(expand=True,fill='both')
note.add(insertar,text="insertar")

texto=Label(insertar,text="material")
texto.place(x=20, y=60)
material=StringVar()
material1=Entry(insertar,textvariable=material)
material1.place(x=110, y=60)

texto=Label(insertar,text="cantidad")
texto.place(x=20, y=100)
cantidad=StringVar()
cantidad1=Entry(insertar,textvariable=cantidad)
cantidad1.place(x=110, y=100)

boton=Button(insertar,text="registrar",command=insertarobj)
boton.place(x=150, y=140)


#actualizar
    
actualizar = Frame(note,width=400,height=400)
actualizar.pack(expand=True,fill='both')
note.add(actualizar,text="actualizar")

titulo=Label(actualizar,text="Actualizar datos",fg="red").place(x=20, y=0)


titulo=Label(actualizar,text="Ingrese ID que desee Actualizar").pack()
id=StringVar()
id1=Entry(actualizar,textvariable=id).pack()

titulo=Label(actualizar,text="Ingrese nuevo material").pack()

materialn=StringVar()
material1=Entry(actualizar,textvariable=materialn).pack()

tutulo=Label(actualizar,text="Ingrese nueva cantidad").pack()
cantidadn=StringVar()
cant=Entry(actualizar,textvariable=cantidadn).pack()
titulo=Label(actualizar,text="Ingrese nueva cantidad").pack()
botonact=Button(actualizar,text="Actualizar",command=actualizarobj).pack()


    
    
    
mostrar = Frame(note,width=400,height=400)
mostrar.pack(expand=True,fill='both')
note.add(mostrar,text="mostrar")
texto=Label(mostrar,text="mostrar")

ventana.mainloop()
