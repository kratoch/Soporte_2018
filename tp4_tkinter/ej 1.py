from tkinter import *

def boton_sumar():
    nvalor1 = nvar1.get()
    nvalor2 = nvar2.get()
    resultado = float(nvalor1) + float(nvalor2)
    nvalor3 = nvar3.set(str(resultado))
def boton_restar():
    nvalor1 = nvar1.get()
    nvalor2 = nvar2.get()
    resultado = float(nvalor1) - float(nvalor2)
    print (str(resultado))
def boton_multiplicar():
    nvalor1 = nvar1.get()
    nvalor2 = nvar2.get()
    resultado = float(nvalor1) * float(nvalor2)
    print (str(resultado))
def boton_dividir():
    nvalor1 = nvar1.get()
    nvalor2 = nvar2.get()
    resultado = float(nvalor1) / float(nvalor2)
    print (str(resultado))



raiz = Tk()
raiz.size=50
raiz.title ("Calculadora")

etiq1 = Label(raiz, text = "primer operando",)
etiq2 = Label(raiz, text = "segundo operando",)

nvar1 = StringVar()  # método de Tkinter devuelve obj string para usar con entry
nvar1.set("")        # se asigna valor al obj nvar

nvar2 = StringVar()
nvar2.set("")

nvar3 = StringVar()
nvar3.set("resultado")

oper1 = Entry(raiz, textvariable = nvar1)   # vincula una variable con la representación gráfica
oper2 = Entry(raiz, textvariable = nvar2)   #recibe un obj que va a akmacenar lo que escribe el usuario
res = Entry(raiz, textvariable = nvar3)

botonSum = Button(raiz, text="+", command = boton_sumar)
botonRes = Button(raiz, text="-", command = boton_restar)
botonMul = Button(raiz, text="x", command = boton_multiplicar)
botonDiv = Button(raiz, text="%", command = boton_dividir)

#etiq1.pack(side=LEFT)
etiq1.grid(column=0, row=0)
#etiq2.pack(side=LEFT)
etiq2.grid(column=1,row=0)
#oper1.pack(side=LEFT)
oper1.grid(column=0, row=1,  padx=(25,25))
#oper2.pack(side=LEFT)
oper2.grid(column=1, row=1)
#botonSum.pack(side=LEFT)
res.grid(column=1, row=3)
botonSum.grid(column=2,row=1, padx=(25,0))
#botonRes.pack(side=LEFT)
botonRes.grid(column=3, row=1)
#botonMul.pack(side=LEFT)
botonMul.grid(column=4, row=1)
#botonDiv.pack(side=LEFT)
botonDiv.grid(column=5, row=1)


raiz.mainloop()

print("nvar1=", nvar1.get())
print("nvar2=", nvar2.get())
