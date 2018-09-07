from tkinter import *
from tkinter import ttk, font
#programa principal

#creo el objeto ventana principal
ventana = Tk()
ventana.title("Alta")
ventana.geometry("200x130")
fuente = font.Font(weight='bold')
#creo los controles

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
cancelarBoton = Button(ventana,text="Cancelar")

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
ventana.mainloop()
