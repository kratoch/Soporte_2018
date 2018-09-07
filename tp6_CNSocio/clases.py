from src.tp5_CDSocio.clases import CDSocio
from src.tp5_CDSocio.alchemy import Socio

class CNSocio():

    def altaSocio(self, session):
        self.s = session
        self.socio = Socio()
        self.cdsocio= CDSocio()
        self.socio.dni = int(input('ingrese dni: ') or '0')
        while self.socio.dni == 0:
            self.socio.dni = int(input('ingrese dni (obligatorio): ') or '0')
        self.socio.nombre = input('ingrese nombre (debe contener mas de 3 caracteres y menos de 15): ')
        while len(self.socio.nombre) < 3 or len(self.socio.nombre) > 15:
            self.socio.nombre = input('error, ingrese el nombre nuevamente (debe contener mas de 3 caracteres y menos de'
                                      ' 15): ')
        self.socio.apellido = input('ingrese apellido: ')
        while len(self.socio.apellido) < 3 or len(self.socio.apellido) > 15:
            self.socio.apellido = input('error, ingrese el nombre nuevamente (debe contener mas de 3 caracteres y menos de'
                                      ' 15): ')
        #self.socios = self.s.query(Socio).filter(Socio.dni == self.dni).first()
        if self.cdsocio.buscarDNI(self.s,self.socio.dni) == 1:
            print('ya existe un socio con ese nro de documento')
        else:
            print('carga')
            self.cdsocio.altaSocio(self.s, self.socio)

    def borrarSocio(self,session):
        self.s = session
        self.cdsocio = CDSocio()
        self.cdsocio.muestraSocio(self.s)
        self.cdsocio.borrar(self.s)

    def modificarSocio(self,session):
        self.s = session
        self.cdsocio=CDSocio()
        self.cdsocio.muestraSocio(self.s)
        self.id = int(input('ingrese id del socio a modificar: '))
        if self.cdsocio.buscar(self.s, self.id) == False:
            print("error! Usuario inexistente! ")
        else:
            self.dni = int(input('ingrese dni: ') or '0')
            while self.dni == 0:
                self.dni = int(input('ingrese dni (obligatorio): ') or '0')
            self.nombre = input('nombre: ')
            while len(self.nombre) < 3 or len(self.nombre) > 15:
                self.nombre = input('error, ingrese el nombre nuevamente (debe contener mas de 3 caracteres y menos '
                                    'de 15): ')
            self.apellido = input('apellido: ')
            while len(self.apellido) < 3 or len(self.apellido) > 15:
                self.apellido = input('error, ingrese el nombre nuevamente (debe contener mas de 3 caracteres y menos '
                                      'de 15): ')
            self.cdsocio.modificar(self.s,
                                   Socio(idSoc= self.id, nombre= self.nombre, apellido= self.apellido, dni= self.dni))
            print('Se ha modificado con exito')


