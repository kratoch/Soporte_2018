from src.tp5_CDSocio.clases import CDSocio, Socio
from src.tp6_CNSocio.clases import CNSocio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///tp5.db', echo=True)
DBSession = sessionmaker(bind=engine,autoflush=True)
session = DBSession()

cdsocio=CDSocio()

#cdsocio.altaSocio(session)

#cdsocio.muestraSocio(session)

#cdsocio.buscar(session)



#print(cdsocio.modificar(session, Socio (idSoc = 1, nombre= "Cristiano", apellido= "Ronaldo", dni= 11111111)))


#print(cdsocio.borrar(session))


#print(cdsocio.buscarDNI(session, dni = int(input('ingrese dni: '))))


cdsocio.muestraSocio(session)