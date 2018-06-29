import random
import datetime
from math import pi


class Rectangulo:
    def __init__(self, base, altura):
        self.b = base
        self.h = altura

    def area(self):
        return self.b * self.h


class Cirulo:
    def __init__(self):
        self.radio = 3

    @property
    def area(self):
        return round(pi * (self.radio ** 2), 2)

    @property
    def perimetro(self):
        return round(pi * self.radio * 2, 2)


class Persona:
    def __init__(self, nombre, sexo, peso, altura, edad=None, fechaNac=None):
        self.nombre = nombre
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generar_dni()
        if not (fechaNac == None):
            self.edad = self.getEdad((fechaNac))
        elif not (edad == None):
            self.edad = edad
        else:
            self.edad = 0

    def getEdad(self, fechaNac):

        ahora = datetime.datetime.now()
        if ahora.month > fechaNac.month:
            self.edad = (ahora.year - fechaNac.year)
        elif ahora.month == fechaNac.month and ahora.day >= fechaNac.day:
            self.edad = (ahora.year - fechaNac.year)
        else:
            self.edad = (ahora.year - fechaNac.year) - 1

        return self.edad

    def es_mayor_edad(self):
        if (self.edad >= 18):
            print(str(self.nombre) + " es mayor de edad")
        elif self.edad == 0:
            print("No edad")
        else:
            print(str(self.nombre) + " es menor de edad")

    def print_data(self):
        if self.sexo == "m":
            genero = "hombre"
        else:
            genero = "mujer"

        print(self.nombre + ": " + genero + " de " + str(self.edad) + " años de edad, pesa " + str(
            self.peso) + "kg y mide " + str(self.altura) + "mts de altura")
        print("DNI: " + str(self.dni))

    def generar_dni(self):
        self.dni = random.randint(15000000, 42000000)
        return self.dni


class Estudiante(Persona):
    def __init__(self, nombre, sexo, peso, altura, edad, fechaNac, nombCarrera, anioIng, cantMat, cantMatAprob):
        Persona.__init__(self, nombre, sexo, peso, altura, edad, fechaNac)
        self.listadoCarreras = ['sistemas', 'civil', 'quimica', 'electrica', 'mecanica']
        self.nombCarrera = nombCarrera
        self.anioIng = anioIng
        self.cantMat = cantMat
        self.cantMatAprob = cantMatAprob

    def avance(self):
        return round(self.cantMatAprob / self.cantMat * 100)

    def edad_ingreso(self):
        return self.edad - (2018 - self.anioIng)


class Ejercicio():
    def __init__(self, fecha):
        self.anio=fecha.year
        self.dia = fecha.day
        self.mes = fecha.month
    def inicio(self):
        if self.mes >= 7:
            fechaIni = datetime.date(self.anio,7,1)
            return fechaIni
        else:
            anio= self.anio - 1
            fechaIni =datetime.date(anio,7,1)
            return fechaIni
    def fin(self):
        if self.mes > 6:
            fechaFin = "%s/%s/%s"%(30,6,self.anio + 1)
        elif self.mes == 6 and self.dia == 30:
            fechaFin = "%s/%s/%s"%(30,6,self.anio + 1)
        else:
            fechaFin = "%s/%s/%s"%(30,6,self.anio)
        return fechaFin
    def semana(self):
         inicio = self.inicio()
         fin = datetime.date(self.anio,self.mes,self.dia)
         semana = (fin - inicio)//7
         return semana.days




