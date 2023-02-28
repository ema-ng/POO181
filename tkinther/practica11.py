
from tkinter import Tk, Frame, Button

#1.instanciamon un objeto ventana 

ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")

#2 definir secciones de la ventana 

seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True,fill='both')


seccion2 = Frame(ventana, bg="orange")
seccion2.pack(expand=True,fill='both')


seccion3 = Frame(ventana,bg="yellow")
seccion3.pack(expand=True,fill='both')


#3.botones 

botonAzul= Button(seccion1, text="boton azul", fg="blue")
botonAzul.place(x=60, y=60)

botonblanco= Button(seccion2, text="boton blanco", fg="pink")
botonblanco.grid(row=0,column=0)

botonnegro= Button(seccion2, text="boton negro", fg="black", bg="white")
botonnegro.grid(row=1,column=1)

botonverde= Button(seccion3, text="boton verde", fg="green")
botonverde.pack()




#main de ejecucion de la ventana  (ultima)

ventana.mainloop()