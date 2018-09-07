from src.tp2.clases import *
import datetime

#Ejercicio 1
r1 = Rectangulo(2, 8)
assert r1.area() == 16
print("Ejercicio 1")
print('Area del rectángulo: ' + str(r1.area()))

#Ejercicio 2
c1 = Cirulo()
#assert c1.area() == 28.27
print('\n Ejercicio 2')
print('Area del círculo: ' + str(c1.area))
#assert c1.perimetro() == 18.85
print('Perímetro: ' + str(c1.perimetro))

#Ejercicio 4
p1 = Persona("claudio", 'm', 67, 1.74, 28)
print("\nEjercicio 3")
p1.es_mayor_edad()
p1.print_data()
print(p1.generar_dni())

#Ejercicio 4

e = Estudiante('Claudio', 'm', 67, 1.74, 28, None, 'sistemas', 2011, 36, 29)
print('\nEjercicio 4')
print('ha completado un ' + str(e.avance()) +'% de la carrera')
print('Ingreso a la universidad a los ' + str(e.edad_ingreso()) + ' años de edad')

#Ejercicio 5

listasEst = [Estudiante('estudiante1', 'm', 67, 1.74, 28, None, 'sistemas', 2011, 36, 29),
             Estudiante('estudiante2', 'm', 67, 1.74, 28, None, 'quimica', 2011, 36, 29),
             Estudiante('estudiante3', 'm', 67, 1.74, 28, None, 'mecanica', 2011, 36, 29),
             Estudiante('estudiante4', 'm', 67, 1.74, 28, None, 'sistemas', 2011, 36, 29),
             Estudiante('estudiante5', 'm', 67, 1.74, 28, None, 'civil', 2011, 36, 29)]

def listas_diccionarios(listasEst):
    carreras = {'sistemas':0, 'civil':0, 'quimica':0, 'electrica':0, 'mecanica':0}
    for e in listasEst:
        if e.nombCarrera in carreras.keys():
            carreras[e.nombCarrera] = carreras[e.nombCarrera] + 1
    return carreras

carreras = listas_diccionarios(listasEst)

print("\nEjercicio 5")
print("sistemas: " + str(carreras['sistemas']))
print("civil: " + str(carreras['civil']))
print("quimica: " + str(carreras['quimica']))
print("electrica: " + str(carreras['electrica']))
print("mecanica: " + str(carreras['mecanica']))

#Ejercicio 6

fechaNac = datetime.datetime(2004, 2, 16)
p2 = Persona('Paula', 'f', 49, 1.67, None, fechaNac)
print('\nEjercicio 6')
p2.print_data()
p2.es_mayor_edad()

#Ejercicio 7

fecha= datetime.date(2017,7,8)
ej=Ejercicio(fecha)

print('\nEjercicio 7')

fechaIni = ej.inicio()
fechaMuestra = "%s/%s/%s"%(fechaIni.day,fechaIni.month,fechaIni.year)
print('fecha de inicio: ', fechaMuestra)
print('fecha de fin: ', ej.fin())
print('cant de semanas ' + str(ej.semana()))
