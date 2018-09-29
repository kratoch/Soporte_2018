from tkinter import *
from tkinter import ttk, font

#Defino las funciones

#en esta funcion se encuentra la ventana de alta socio
def alta():

    #creo el objeto ventana principal
    ventana = Tk()
    ventana.title("Alta")
    ventana.geometry("200x130")
    fuente = font.Font(weight='bold')
    #creo los controles
    idEtiqueta = Label(ventana,text="Id")
    nombreEtiqueta = Label(ventana,text="Nombre")
    apellidoEtiqueta = Label(ventana,text="Apellido")
    dniEtiqueta = Label(ventana,text="DNI")

    idvar = IntVar()
    nombreVar = StringVar()
    apellidoVar = StringVar()
    dniVar=IntVar()

    idEntry = Entry(ventana,textvariable=idvar)
    nombreEntry = Entry(ventana,textvariable=nombreVar)
    apellidoEntry=Entry(ventana,textvariable=apellidoVar)
    dniEntry = Entry(ventana,textvariable=dniVar)

    aceptarBoton = Button(ventana,text="Aceptar")
    cancelarBoton = Button(ventana,text="Cancelar",command=ventana.destroy)

    #Le doy geometria a los controles
    idEtiqueta.grid(column=0, row=0)
    nombreEtiqueta.grid(column=0,row=1)
    apellidoEtiqueta.grid(column=0,row=2)
    dniEtiqueta.grid(column=0,row=3)
    aceptarBoton.grid(column=0,row=5)
    cancelarBoton.grid(column=1,row=5)

    idEntry.grid(column=1,row=0)
    nombreEntry.grid(column=1,row=1)
    apellidoEntry.grid(column=1,row=2)
    dniEntry.grid(column=1,row=3)

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
botonAlta=Button(marco,text="Alta",command=alta)
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
