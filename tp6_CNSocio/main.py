from src.tp5_alchemy.clases import CDSocio, Socio
from src.tp6_CNSocio.clases import CNSocio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///C:/Users/claud/Google Drive/Python/Soporte2018/src/tp5_alchemy/tp5.db', echo=True)
DBSession = sessionmaker(bind=engine,autoflush=True)
session = DBSession()


cdsocio=CDSocio()
cnsocio= CNSocio()

#cnsocio.altaSocio(session)

#cnsocio.borrarSocio(session)

cnsocio.modificarSocio(session)

stop = input('presione enter para continuar')
cdsocio.muestraSocio(session)

