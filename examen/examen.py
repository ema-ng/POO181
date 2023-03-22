from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import random

nombrel=[]
carrera=[]

aleatorio="1234567890"
año=23

def generar():
    
    a=str(nombre.get())
    b=str(apellidop.get())
    c=str(apellidom.get())
    d=str(nacimiento.get())
    f=str(carrera.get())

    
    j=a[0]
    k=f[0]
    l=f[1]
    m=f[2]
    o=d[2]
    p=d[3]

    h=b[0]
    i=b[1]
    q=c[0]
    r=c[1]
    g=str([random.choices (aleatorio) for i in range (2)])
    
    u=g[3]
    v=g[10]
   
    w=(j,q,r,h,i,o,p,año,k,l,m,u,v)
    
    messagebox.showinfo("matricula" ,f'la matricula es: "{j}{q}{r}{h}{i}{o}{p}{año}{k}{l}{m}{u}{v}"')



    
  

 

    
    
ventana = Tk()
ventana.title("general")
ventana.geometry("600x400")

seccion1 = Frame(ventana, bg="white")
seccion1.pack(expand=True,fill='both')

texto=Label(seccion1,text="generador de matricula")
texto.pack()

texto=Label(seccion1)
texto.pack()


texto=Label(seccion1,text="nombre")
texto.pack()

nombre=StringVar()
nombre1=Entry(seccion1,textvariable=nombre)
nombre1.pack()

texto=Label(seccion1,text="apellido paterno")
texto.pack()

apellidom=StringVar()
apellidom1=Entry(seccion1,textvariable=apellidom)
apellidom1.pack()

texto=Label(seccion1,text="apellido materno")
texto.pack()

apellidop=StringVar()
apellidop1=Entry(seccion1,textvariable=apellidop)
apellidop1.pack()

texto=Label(seccion1,text="año de nacimiento")
texto.pack()

nacimiento=StringVar()
nacimiento1=Entry(seccion1,textvariable=nacimiento)
nacimiento1.pack()

texto=Label(seccion1,text="carrera")
texto.pack()

carrera=StringVar()
carrera1=Entry(seccion1,textvariable=carrera)
carrera1.pack()


boton=Button(seccion1,text="generar",command=generar)
boton.pack()

ventana.mainloop()

