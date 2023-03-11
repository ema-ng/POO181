from tkinter import*
from tkinter import messagebox
from tkinter import ttk





usuarios=[]

def guardar ():
    
    a=str(cuenta.get())
    b=str(titular.get())
    c=str(saldo.get())
    d=str(edad.get())
    
    usuarios.append(a)
    usuarios.append(b)
    usuarios.append(d)
    
    c=b


    print(usuarios)
    

ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")

registro= ttk.Notebook(ventana)
registro.pack()


seccion1 = Frame(registro,width=400,height=280)
seccion1.pack(expand=True,fill='both')

seccion2 = Frame(registro,width=400,height=280)
seccion2.pack(expand=True,fill='both')

registro.add(seccion1,text="registro de usuario")
registro.add(seccion2,text="acciones")

texto=Label(seccion1,text="registrar usuario")
texto.pack()

texto1=Label(seccion1,text="NO. de cuenta")
texto1.pack()

cuenta=StringVar()
cuenta1=Entry(seccion1,textvariable=cuenta)
cuenta1.pack()

texto2=Label(seccion1,text="titular")
texto2.pack()

titular=StringVar()
titular1=Entry(seccion1,textvariable=titular)
titular1.pack()

texto3=Label(seccion1,text="saldo")
texto3.pack()

saldo=StringVar()
saldo1=Entry(seccion1,textvariable=saldo)
saldo1.pack()

texto4=Label(seccion1,text="edad")
texto4.pack()

edad=StringVar()
edad1=Entry(seccion1,textvariable=edad)
edad1.pack()


boton=Button(seccion1,text="guardar",command=guardar)
boton.pack()

#2////////


def menu ():
    
    saldo=[500]
    
    if str(acciones1.get()) == str("1"):
        print(saldo)
        
    elif str(acciones1.get()) == str("2"):
        saldo.append(100)
        print(saldo)
        a=sum(saldo)
        
        print(a)
    elif str(acciones1.get()) == str("3"):
        print(saldo)
        saldo.remove(100)
        print(saldo)
         
    elif str(acciones1.get()) == str("4"):
        usuarios.append(saldo)
    
        

texto=Label(seccion2,text="¿que deseas realizar")
texto.pack()
texto=Label(seccion2,text="1.consultar saldo")
texto.pack()
texto=Label(seccion2,text="2.ingresar efectivo")
texto.pack()
texto=Label(seccion2,text="3.retirar efectivo")
texto.pack()
texto=Label(seccion2,text="4.depositar a otra cuenta")
texto.pack()

acciones1=StringVar()
acciones=Entry(seccion2,textvariable=acciones1)
acciones.pack()

boton=Button(seccion2,text="seleccionar",command=menu)
boton.pack()

ventana.mainloop()