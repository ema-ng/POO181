from  tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self) -> None:
        pass
    
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/EMMANUEL NORIEGA/Desktop/github/POO181/practica 15/DBU usuarios.db")
            print("conectado a la base BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("no se pudo conectar")
    
    #metodos para guardar
       
    def guardarusuario (self,nom,cor,con):
        
        #1. usar conexin
       conx=self.conexionBD()
       
       #2.vaidar parametros vacios
       
       if(nom == "" or cor=="" or con ==""):
           messagebox.showwarning("aguas","fomulario incompleto")
           
       else:
           #3 preparar cursor, datos,querrysql
           
           cursor=conx.cursor()
           conH=self.encriptarcon(con)
           datos=(nom,cor,conH)
           qrisert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
           
           #4.ejecutar insert y cerrar conexion
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
        
    
    def encriptarcon(self,con):
        
        #peparar cn bytes 
        conPlana=con
        conPlana=conPlana.encode()#convertir con a bytes
        sal= bcrypt.gensalt()  
        
        #encryptar
        conha=bcrypt.hashpw(conPlana,sal) 
        print(conha)    
        return conha 
        
        