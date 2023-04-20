
from asyncio import FIRST_EXCEPTION
import threading 
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt

class logicae:
    
    def __init__(self) -> None:
        pass
    
    
    #conexion 
    
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/EMMANUEL NORIEGA/Desktop/github/POO181/examen3p/examen.db")
            print("conectado a la base BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("no se pudo conectar")
            
            
    def registrar (self,mat,can):
        
       conx=self.conexionBD()
       if (mat == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato material")
       if (can == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Cantidad")    
       else:
           
           cursor=conx.cursor()
           datos=(mat,can)
           qrisert="insert into MatConstruccion (Material,Cantidad) values (?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
           
           
    def acuaizar (self,id,matn,cann):
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
            
        if(matn== ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
            
        if(cann == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
       
        else:
            try:
        
                nuevomat=matn
                nuevacan=cann
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE MatConstruccion SET Material=?, Cantdad=? WHERE id=?", (nuevomat,nuevacan,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")
         