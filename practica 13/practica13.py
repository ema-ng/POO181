from logica import *


axc=logica()


def funciones():
    axc.generar(longitud.get(),mayu.get(),espe.get())





ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")



seccion1 = Frame(ventana, bg="white")
seccion1.pack(expand=True,fill='both')

texto=Label(seccion1,text="generador de contraseñas")
texto.pack()

texto=Label(seccion1)
texto.pack()

texto=Label(seccion1,text="ingrese la longitud")
texto.pack()
longitud=StringVar()
lon=Entry(seccion1,textvariable=longitud)
lon.pack()


texto=Label(seccion1,text="¿usar caracteres especiales?")
texto.pack()
espe=StringVar()
esp=Entry(seccion1,textvariable=espe)
esp.pack()

texto=Label(seccion1,text="¿usar mayusculas?")
texto.pack()
mayu=StringVar()
may=Entry(seccion1,textvariable=mayu)
may.pack()

comp=Button(seccion1,text="crear", fg="black",command=funciones)
comp.pack()

comp=Button(seccion1,text="comprobar", fg="black",command=funciones)
comp.pack()




ventana.mainloop()
