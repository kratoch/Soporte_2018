from src.tp5_alchemy.clases import CDSocio, Socio, CNSocio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///tp5.db', echo=True)
DBSession = sessionmaker(bind=engine,autoflush=True)
session = DBSession()

'''cdsocio=CDSocio()
cdsocio.altaSocio(session)
cdsocio.muestraSocio(session)
cdsocio.buscar(session)
socio = Socio(idSoc = 4, nombre="Diego", apellido="Maradroga", dni = 111111111)
bool=cdsocio.modificar(session, socio)
print(bool)
bool=cdsocio.borrar(session)
print(bool)
cdsocio.buscarDNI(session, dni = int(input('ingrese dni: ')))
cdsocio.muestraSocio(session)'''

cnsocio= CNSocio()
cnsocio.altaSocio(session)
