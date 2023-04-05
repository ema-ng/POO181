from  tkinter import messagebox
import sqlite3
import bcrypt
from tkinter import * 



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
    
    
    #buscar un usuario 
    
    def consultar(self,id):
        
        #1.preparar conexion 
        conx=self.conexionBD()
        if(id==""):
            messagebox.showwarning("cuidado","id vacio scribe algo valido")
            conx.close()
        else:
            try:
                
                cursor=conx.cursor()
                selecqry= "select * from TBRegistrados where id="+id
                cursor.execute(selecqry)
                rsusuario=cursor.fetchall()
                conx.close()
                
                return rsusuario
            
            except sqlite3.OperationalError:
                print ("error de consulta")
                
    def prueba1(self,tree):
        conx=self.conexionBD()
        cur = conx.cursor()
        cur.execute('SELECT * FROM TBRegistrados;')
        records = cur.fetchall()
    
        for record in records:
            
            tree.insert(values=(record))
            print(record)
            
    def eliminarusuario (self,id):
        
        conx=self.conexionBD()
        curs=conx.cursor() 
        sql=f"delete from TBRegistrados where id={id}"
        curs.execute(sql)
        conx.commit()
        conx.close()
        messagebox.showwarning("cuidado","usuario eliminado")
        
    def actualizar (self,id,nombre,correo,contra):
        
        conx=self.conexionBD()
        curs=conx.cursor() 
        a=f"update TBRegistrados set nombre ='{nombre}', correo = '{correo}', contra='{contra}'where id={id}"
        curs.execute(a)
        conx.commit()
        conx.close()
        messagebox.showwarning("cuidado","usuario eliminado")
    
        
   
             
            
    
        
                

        
        