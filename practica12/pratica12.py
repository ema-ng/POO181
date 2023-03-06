from tkinter import *
from tkinter import messagebox


class pratica12:
            
    def __init__(self,corr,cont):
        
        self.__correo=corr
        self.__contraseña=cont
        
    
    def comprobar (self): 
        
        if (str(self.__correo())) == str("emma") and (str(self.__contraseña())) == str("1234"):
            messagebox.showinfo("bienvenido","bienvenido")
        elif (len(self.__contraseña() and self.__correo ()))== False:
            messagebox.showinfo("error","los campos estan vacios")
        else:
            messagebox.showinfo("error","usuario invalido")   
       
            
       
    
    def __getcorreo__(self):
        return self.__correo
    
    def __setcorreo__(self,corr):
        self.__correo=corr
    
    def __getcontraseña__(self):
        return self.__contraseña
    
    def __setcontraseña__(self,cont):
        self.__contraseña=cont
    
    
