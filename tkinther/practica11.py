
from tkinter import Tk, Frame, Button,messagebox

def mostrarMensaje():
    messagebox.showinfo("aviso","este mensaje es para avisar algo")
    messagebox.showerror("error","todo fallo con exito")
    print(messagebox.askokcancel("pregunta","el o ella jugo con tu corazon"))
    print(messagebox.askquestion("pregunta","el o ella jugo con tu corazon"))
    print(messagebox.askretrycancel("pregunta","el o ella jugo con tu corazon"))
    print(messagebox.askyesno("pregunta","el o ella jugo con tu corazon"))
    print(messagebox.askyesnocancel("pregunta","el o ella jugo con tu corazon"))
    
#funcion para agregar botones 

def agregarbotones():
    botonverde.config(text="+",bg="green",fg="white")
    botonnuevo=Button(seccion3,text="boton nuevo")
    botonnuevo.pack()

#1.instanciamon un objeto ventana 

ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")

#2 definir secciones de la ventana 

seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True,fill='both')


seccion2 = Frame(ventana, bg="blue")
seccion2.pack(expand=True,fill='both')


seccion3 = Frame(ventana,bg="green")
seccion3.pack(expand=True,fill='both')


#3.botones 

botonAzul= Button(seccion1, text="boton azul", fg="blue",command=mostrarMensaje)
botonAzul.place(x=60, y=60)

botonblanco= Button(seccion2, text="boton blanco", fg="pink",bg="#ffff1a")
botonblanco.grid(row=0,column=0)

botonnegro= Button(seccion2, text="boton negro", fg="white", bg="black")
botonnegro.grid(row=1,column=1)

botonverde= Button(seccion3, text="boton verde", fg="green",command=agregarbotones)
botonverde.pack()




#main de ejecucion de la ventana  (ultima)

ventana.mainloop()