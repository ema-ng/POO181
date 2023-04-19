from asyncio import FIRST_EXCEPTION
import threading 
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()

    
insertar = Frame(note,width=400,height=400)
insertar.pack(expand=True,fill='both')
note.add(insertar,text="R. Clientes")
texto=Label(insertar,text="registro de clientes")