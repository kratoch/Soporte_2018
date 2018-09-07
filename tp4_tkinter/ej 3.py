import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Vista de árbol en Tkinter")

        self.treeview = ttk.Treeview(self)

        ciudades = {'2000':'Rosario', '3600':'Formosa', '4650':'La Quiaca', '3000':'Santa Fe'}
        pais = self.treeview.insert("", tk.END, text="Argentina")
        for i in ciudades:
            ciudad1 = self.treeview.insert(pais, tk.END, text= ciudades[i])
            self.treeview.insert(ciudad1, tk.END, text= i)




        self.treeview.selection_add(pais)
        self.treeview.pack()

        self.pack()
        def borrarSelec():
           selected_item = self.treeview.selection()[0]
           self.treeview.delete(selected_item)
        def agregarItem():
            ciudad = input("ingrese nombre de la ciudad: ")
            codPostal = input("ingrese codigo postal: ")
            ciudad2 = self.treeview.insert(pais, tk.END, text= ciudad)
            self.treeview.insert(ciudad2, tk.END, text= codPostal)
        def editarItems():
            ciudad = input("ingrese nombre de la ciudad: ")
            codPostal = input("ingrese codigo postal: ")
            selected_item = self.treeview.selection()[0]
            self.treeview.delete(selected_item)
            ciudad2 = self.treeview.insert(pais, tk.END, text= ciudad)
            self.treeview.insert(ciudad2, tk.END, text= codPostal)

        borrar = tk.Button(main_window, text= "BORRAR", command=borrarSelec)
        borrar.pack()
        agregar = tk.Button(main_window, text= "AGREGAR", command=agregarItem)
        agregar.pack()
        editar = tk.Button(main_window, text= "EDITAR", command=editarItems)
        editar.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
