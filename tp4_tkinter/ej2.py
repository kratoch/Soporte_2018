from tkinter import *

raiz = Tk()
raiz.title('Carlculadora')
operador = ''
text_input = StringVar()

def btnClick(numbers):
    global operador
    operador = operador + str(numbers)
    text_input.set(operador)
def btnIgual():
    global operador
    igual = str(eval(operador))
    text_input.set(igual)
    operador = ''


display = Entry(raiz,textvariable = text_input, font=(20), bd = 20,justify = 'right').grid(columnspan = 4)

#primera fila de botones

btn7=Button(raiz, font=20, command=lambda:btnClick(7), text = '7').grid(row=1, column=0)
btn8=Button(raiz, font= 20, command=lambda:btnClick(8), text = '8').grid(row=1, column=1)
btn9=Button(raiz, font=20, command=lambda:btnClick(9), text = '9').grid(row=1, column=2)
sumar=Button(raiz,font=20, command=lambda:btnClick('+'), text = '+').grid(row=1, column=3)

#segunda fila de botones

btn4=Button(raiz, font=20, command=lambda:btnClick(4), text = '4').grid(row=2, column=0)
btn5=Button(raiz, font=20, command=lambda:btnClick(5), text = '5').grid(row=2, column=1)
btn6=Button(raiz, font=20, command=lambda:btnClick(6), text = '6').grid(row=2, column=2)
restar=Button(raiz, font=20, command=lambda:btnClick('-'), text = '-').grid(row=2, column=3)

#tercera fila de botones

btn1=Button(raiz, font=20, command=lambda:btnClick(1), text = '1').grid(row=3, column=0)
btn2=Button(raiz, font=20, command=lambda:btnClick(2), text = '2').grid(row=3, column=1)
btn3=Button(raiz, font=20, command=lambda:btnClick(3), text = '3').grid(row=3, column=2)
division=Button(raiz, font=20, command=lambda:btnClick('/'), text = '/').grid(row=3, column=3)

#cuarta fila de botones

btn0=Button(raiz, font=20, command=lambda:btnClick(0), text = '0').grid(row=4, column=0)
igual=Button(raiz, font=20, command=lambda:btnIgual(), text = '=').grid(row=4, column=1, ipadx=36, columnspan = 2)
multiplicar=Button(raiz, font=20, command=lambda:btnClick('x'), text = 'x').grid(row=4, column=3)

raiz.mainloop()
