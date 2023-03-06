
from pratica12 import*
from tkinter import StringVar

def comprobar (): 
        
        if (str(corr1.get())) == str("emma") and (str(cont1.get())) == str("1234"):
            messagebox.showinfo("bienvenido","bienvenido")
        elif (len(corr1.get() and cont1.get  ()))== False:
            messagebox.showinfo("error","los campos estan vacios")
        else:
            messagebox.showinfo("error","usuario invalido")   
            


ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")

seccion1 = Frame(ventana, bg="white")
seccion1.pack(expand=True,fill='both')



titulo=Label(seccion1,text="correo:")
titulo.pack()
corr1=StringVar()
corr2= Entry(seccion1,textvariable=corr1)
corr2.pack()

titulo1=Label(seccion1,text="contraseña:")
titulo1.pack()

cont1=StringVar()
cont2= Entry(seccion1,show="*",textvariable=cont1)
cont2.pack()

usuario=pratica12(cont1,corr1)

login= Button(seccion1,text="iniciar secion", fg="black",command=comprobar)
login.pack()     




ventana.mainloop()