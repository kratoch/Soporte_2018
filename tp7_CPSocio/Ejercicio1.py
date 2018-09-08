from tkinter import *
from tkinter import ttk

#Defino las funciones
def alta():
    return 0
def baja():
    return 0
def modificacion():
    return 0

#programa principal
#creo el objeto ventana principal
ventana = Tk()
ventana.title("ABM Socio")
ventana.geometry("830x310")
#creo un marco para que contenga alta baja y modificacion (de esta forma puedo ordenar su geometria en conjunto y separado del treeview)
marco = Frame(ventana,relief=FLAT)
#creo el treview
treeview = ttk.Treeview(ventana,column=("nomb","apell","DNI"))
#treeview
treeview.heading("#0", text="Id")
treeview.heading("nomb", text="Nombre")
treeview.heading("apell", text="Apellido")
treeview.heading("DNI", text="DNI")


#creo los controles
botonAlta=Button(marco,text="Alta",command=alta())
botonBaja=Button(marco,text="Baja",command=baja())
botonModif=Button(marco,text="Modificacion",command=modificacion())

#agrego la geometria a los controles
treeview.grid(padx=15,pady=10)
marco.grid(padx=15,sticky=W,)
botonAlta.grid(column=0,row=0)
botonBaja.grid(column=1,row=0)
botonModif.grid(column=2,row=0)
#creo el lazo infinito de la ventana principal
ventana.mainloop()
