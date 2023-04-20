
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
            messagebox.showwarning("Cuidado","El campo id esta vacio")
            
        if(matn== ""):
            messagebox.showwarning("Cuidado","El campo material esta vacio")
            
        if(cann == ""):
            messagebox.showwarning("Cuidado","El campo cantidad esta vacio")
       
        else:
            try:
        
                nom=matn
                can=cann
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE MatConstruccion SET Material=?, Cantidad=? WHERE IDMat=?", (nom,can,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")
                
                
    
    def act(self):

            conx=self.conexionBD()
            cursor=conx.cursor()
            selectQry="select IDMat,Material,Cantidad from MatConstruccion"
            cursor.execute(selectQry)
            resultado=cursor.fetchall()
            conx.close()
            datos=[]
            for row in resultado:
                datos.append(list(row))
            return datos
         