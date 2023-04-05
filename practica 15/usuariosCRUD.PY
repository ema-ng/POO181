from tkinter import * 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from crontoladorBD import* #1. presentar archivo contolador
import threading

#2.crear objeto de la clase controlador

controlador=controladorBD()

#3.funcion para disparar el boton

def ejecutainsert():
    
    controlador.guardarusuario(nombre.get(),correo.get(),contraseña.get())


def ejecutarselect():
    usuario=controlador.consultar(varbus.get())
    for usu in usuario:
        cadena= str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+str(usu[3]) 
    
    if(usuario):
        
        print(cadena)
        texto1.insert(tk.INSERT,cadena)
        
        
        
    else:
        messagebox.showwarning("no encontrado","ese usuario no existe")
        
def act ():
    controlador.actualizar(aid.get(),anombre.get(),acorreo.get(),acontra.get())
    
def eliminarusu():
    controlador.eliminarusuario(elimina.get())
  
"""  
def tabla():
    return controlador.actualizar()


def act_tabla():
    for uno in tree.get_children():
        tree.delete(uno)
    registros=tabla()
    for b,row in enumerate(registros):
        tree.insert('','end',text=str(b+1),values=(row))
    if registros==[]:
        messagebox.showwarning("error","no hay datos")
        
def nuevo():
    act=threading.Thread(target=act_tabla)
    act.start()
    
"""

    

    
ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()

agregar = Frame(note,width=400,height=400)
agregar.pack(expand=True,fill='both')
buscar = Frame(note,width=400,height=400)
buscar.pack(expand=True,fill='both')
consultar = Frame(note,width=400,height=400)
consultar.pack(expand=True,fill='both')
eliminar = Frame(note,width=400,height=400)
eliminar.pack(expand=True,fill='both')
actu = Frame(note,width=400,height=400)
actu.pack(expand=True,fill='both')

note.add(agregar,text="agregar Usuario")
note.add(buscar,text="Buscar Usuario")
note.add(consultar,text="Consultar Usuario")
note.add(eliminar,text="eliminar registro")
note.add(actu,text="actualizar registro")


titulo = Label(agregar,text="Registro de usuario",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(agregar,text="nombre")
texto.pack()

nombre=StringVar()
nombre1=Entry(agregar,textvariable=nombre)
nombre1.pack()

texto=Label(agregar,text="correo")
texto.pack()

correo=StringVar()
correo1=Entry(agregar,textvariable=correo)
correo1.pack()


texto=Label(agregar,text="contraseña")
texto.pack()

contraseña=StringVar()
contraseña1=Entry(agregar,textvariable=contraseña)
contraseña1.pack()

boton=Button(agregar,text="agregar",command=ejecutainsert)
boton.pack()


#pestaña 2 buscar usuario 

titulo = Label(buscar,text="Registro de usuario",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(buscar,text="identificar usuario")
texto.pack()

varbus=StringVar()
subbus=Entry(buscar,textvariable=varbus)
subbus.pack()

botonb=Button(buscar,text="buscar",command=ejecutarselect)
botonb.pack()

titulo = Label(buscar,text="encontrado",fg='Blue',font=("modern",18))
titulo.pack()
texto1=Text(buscar,height=5,width=52)

texto1.pack()

#consultar 

"""
col=('id','nombre','correo','contra')
tree=ttk.Treeview(consultar,col=col,show='headings',height=20)
tree.heading('id',text='id',anchor=CENTER)
tree.heading('nombre',text='nombre',anchor=CENTER)
tree.heading('correo',text='correo',anchor=CENTER)
tree.heading('contra',text='contra',anchor=CENTER)
tree.pack(padx=10, pady=10)
registros=tabla()

for b,row in enumerate(registros):
    tree.insert('','end',text=str(b+1),values=(row))
    if registros==[]:
        messagebox.showwarning("error","no hay datos") 
"""

#boton=Button(consultar,text="actualizar",command=nuevo).pack()

                                      

#eliminar 


titulo = Label(eliminar,text="eliminar un usuario",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(eliminar,text="que usuario")
texto.pack()

elimina=StringVar()
elimin=Entry(eliminar,textvariable=elimina)
elimin.pack()

botonb=Button(eliminar,text="buscar",command=eliminarusu)
botonb.pack()

#actualizar

titulo = Label(actu,text="actualizar un usuario",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(actu,text="que usuario")
texto.pack()

aid=StringVar()
aid1=Entry(actu,textvariable=aid)
aid1.pack()

titulo = Label(actu,text="ingresa los nuevos datos",fg='Blue',font=("modern",18))
titulo.pack()

texto=Label(actu,text="nombre")
texto.pack()

anombre=StringVar()
anombre1=Entry(actu,textvariable=anombre)
anombre1.pack()

texto=Label(actu,text="correo")
texto.pack()

acorreo=StringVar()
acorreo1=Entry(actu,textvariable=acorreo)
acorreo1.pack()

texto=Label(actu,text="contraseña")
texto.pack()

acontra=StringVar()
acontra1=Entry(actu,textvariable=acontra)
acontra1.pack()

botn=Button(actu,text="actualizar",command=act).pack()



ventana.mainloop()
