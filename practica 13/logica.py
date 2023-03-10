from tkinter import*
from tkinter import messagebox
import random


class logica:
    
    lista=[]
    
    def __init__(self):
        
        self.__caracteres="abcdefghijklmnñopqrstuvwxyz"
        self.__numeros="1234567890"
        self.__especiales="@!#$%&/=?¡¿'¿´+*-|°¬"
        self.__mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    def generar (self,long,mayus,espec):
        a=int(long)
        c=str(espec)
        d=str(mayus)
        
        if (c) == str("si"):
            b = [random.choices(self.__especiales +self.__caracteres+self.__numeros) for i in range(a)]
            messagebox.askokcancel("contraseña",f'la contraseña es"{b}"')
            
        elif (d)== str("si"):
            b = [random.choices(self.__mayusculas+self.__numeros+self.__caracteres) for i in range(a)]
            messagebox.askokcancel("contraseña",f'la contraseña es"{b}"')
            
        elif (d)== str("si") and  (c)== str("si"):
            b = [random.choices(self.__mayusculas+self.__numeros+self.__caracteres+self.__especiales) for i in range(a)]
            messagebox.askokcancel("contraseña",f'la contraseña es"{b}"')
          
            
        else:
            b = [random.choice(self.__caracteres) for i in range(a)]
            f=print( messagebox.askokcancel("contraseña",f'la contraseña es"{b}"'))
            if f == True:
                print("si")
            

            
    
    
    

            
            

 
           
    