from tkinter import *

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
ventana.geometry("640x340")

top = Toplevel()
#creo un marco
#marco = Frame(ventana,relief="sunken")

#creo los controles
etiqueta= Label(top,text="SOCIOS").pack
botonAlta=Button(ventana,text="Alta",command=alta())
botonBaja=Button(ventana,text="Baja",command=baja())
botonModif=Button(ventana,text="Modificacion",command=modificacion())

#agrego la geometria a los controles
"""botonAlta.pack()
botonBaja.pack()
botonModif.pack()"""
#creo el lazo infinito de la ventana principal
ventana.mainloop()
