from logica14 import*


# importar metodos 

axc=logica14()

def usuario():
    axc.guardar(cuenta.get(),titular.get(),saldo.get(),edad.get())
      
def consulta1 ():
    axc.consulta()
    
 
def depositar1 ():
    axc.depositar(dep.get())
        
def retirar1():
    axc.retirar(ret.get())  

def depositarcuenta1():
    axc.depositarcuenta(depos.get(),depc.get())
    
    
# interfaz del registro usuario 1:


user = Tk()
user.title("practica 11:3 Frames")
user.geometry("600x400")

seccion1 = Frame(user,width=400,height=280)
seccion1.pack(expand=True,fill='both')

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


boton=Button(seccion1,text="guardar",command=usuario)
boton.pack()


    
# interfaz guardar usuario



note= ttk.Notebook(user)
note.pack()

consultar = Frame(note,width=400,height=280)
consultar.pack(expand=True,fill='both')

depositos = Frame(note,width=400,height=280)
depositos.pack(expand=True,fill='both')

retiros = Frame(note,width=400,height=280)
retiros.pack(expand=True,fill='both')

depositocuenta = Frame(note,width=400,height=280)
depositocuenta.pack(expand=True,fill='both')

note.add(consultar,text="consultar saldo")
note.add(depositos,text="depositar")
note.add(retiros,text="retirar")
note.add(depositocuenta,text="depositar a otra cuenta")


#consultar saldo 

texto=Label(consultar,text="consultar saldo")
texto.pack()

texto=Label(consultar,text="")
texto.pack()

boton=Button(consultar,text="consultar",command=consulta1)
boton.pack()

texto=Label(consultar,text="")
texto.pack()

# depositar

texto=Label(depositos,text="depositar efectivo")
texto.pack()
texto=Label(depositos,text="")
texto.pack()
texto=Label(depositos,text="cuanto desea depositar")
texto.pack()
dep=StringVar()
deposito=Entry(depositos,textvariable=dep)
deposito.pack()

boton=Button(depositos,text="depositar",command=depositar1)
boton.pack()
texto=Label(depositos,text="")
texto.pack()

# retirar

texto=Label(retiros,text="retirar efectivo")
texto.pack()
texto=Label(retiros,text="")
texto.pack()
texto=Label(retiros,text="cuanto desea retirar")
texto.pack()
ret=StringVar()
retiro=Entry(retiros,textvariable=ret)
retiro.pack()
boton=Button(retiros,text="retirar",command=retirar1)
boton.pack()
texto=Label(retiros,text="")
texto.pack()

#depositar a otra cuenta

texto=Label(depositocuenta,text="depositar a otra cuenta")
texto.pack()
texto=Label(depositocuenta,text="")
texto.pack()
texto=Label(depositocuenta,text="cuenta")
texto.pack()

depos=StringVar()
depo=Entry(depositocuenta,textvariable=depos)
depo.pack()

texto=Label(depositocuenta,text="titular")
texto.pack()
titula=StringVar()
tit=Entry(depositocuenta)
tit.pack()
texto=Label(depositocuenta,text="cantidad a depositar")
texto.pack()
depc=StringVar()
depcuenta=Entry(depositocuenta,textvariable=depc)
depcuenta.pack()

boton=Button(depositocuenta,text="depositar",command=depositarcuenta1)
boton.pack()
texto=Label(depositocuenta,text="")
texto.pack()

user.mainloop()

