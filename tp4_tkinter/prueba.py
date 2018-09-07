from tkinter import *



def boton_aceptar():
    nvalor = nvar.get()
    print ("Valor ingresado: " + nvalor)



raiz = Tk()
raiz.size=50
raiz.title ("Mi primer ventana")

etiq1 = Label(raiz, text = "Etiqueta")

nvar = StringVar()  # método de Tkinter devuelve obj string para usar con entry
nvar.set(20)        # se asigna valor al obj nvar
txtnro = Entry(raiz, textvariable = nvar)   # vincula una variable con la representación gráfica

boton = Button(raiz, text="Ingresar", command = boton_aceptar)

etiq1.pack()
txtnro.pack()
boton.pack()

raiz.mainloop()

print("nvar=", nvar.get())
