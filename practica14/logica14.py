from tkinter import*
from tkinter import messagebox
from tkinter import ttk

#usuario del deposito

usuario2=["1234","danubio"]
saldous2=[]

#usuario principal

usuario1=[]
saldous1=[]


class logica14 :
    
 
    def __init__(self):
        
        self
        
    #registrar un usuario
        
    def guardar (self,cuenta,titular,saldo,edad):
        
        a=str(cuenta)
        b=str(titular)
        c=int(saldo)
        d=str(edad)
        
        usuario1.append(a)
        usuario1.append(b)
        usuario1.append(d)
        usuario1.append(saldous1)
        saldous1.append(c)
          
    # consultar saldo
    def consulta (self):
        a=sum(saldous1)
        messagebox.showinfo("cuenta",f'el saldo de la cuenta es de: "{a}"')
        
    #depositar 
    
    def depositar (self,dep):
        mas=int(dep)
        saldous1.append(mas)
        messagebox.showinfo("deposito","deposito realizado")
        
    #retirar
        
    def retirar(self,ret):
        menos=int(ret)
        nega=(-menos)
        saldous1.append(nega)
        messagebox.showinfo("retiro","retiro realizado")       
        
    #depositar y guardar en otra cuenta 
    
    def depositarcuenta(self,depos,depc):
        if (str(depos) == str("1234")):
            depo=int(depc)
            negat=(-depo)
            saldous1.append(negat)
            saldous2.append(depo)
            messagebox.showinfo("deposito","deposito realizado")
            
        else:
            messagebox.showinfo("error","cuenta no encontrada")
    
