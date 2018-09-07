from src.tp5_alchemy.alchemy import Socio

class CDSocio:

    def altaSocio(self,session,socio):

          self.socio = socio
          self.s = session
          self.s.add(self.socio)
          self.s.commit()

    def muestraSocio(self,session):
        self.s = session
        self.socios = self.s.query(Socio).all()
        for i in self.socios:
            print('id: ' + str(i.idSoc) + ' ' + i.nombre + ' ' + i.apellido + ' DNI: ' + str(i.dni))

    def buscar(self, session, id):
        self.s = session
        self.id = id
        self.socios = self.s.query(Socio).filter(Socio.idSoc == self.id).first()
        if self.socios:
            print(self.socios.nombre + ' ' + self.socios.apellido)
            return True
        else:
            return False


    def modificar(self, session, socio):
        self.s=session
        self.socio = socio
        self.socios = self.s.query(Socio).filter(Socio.idSoc==self.socio.idSoc).all()
        if self.socios:
            self.s.query(Socio).filter(Socio.idSoc == self.socio.idSoc).delete()
            self.s.add(self.socio)
            self.s.commit()
            return True
        else:
            return False

    def borrar(self,session):
        self.s=session
        self.id = int(input('ingrese id de la persona que desea dar de baja'))
        self.socio=self.s.query(Socio).filter(Socio.idSoc==self.id).all()
        if self.socio:
            self.s.query(Socio).filter(Socio.idSoc==self.id).delete()
            self.s.commit()
            return True
        else:
            return False

    def buscarDNI(self,session,dni):
        self.s = session
        self.dni = dni
        self.cant = self.s.query(Socio).filter(Socio.dni==self.dni).count()
        return self.cant








