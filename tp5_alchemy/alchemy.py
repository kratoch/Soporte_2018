from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


Base = declarative_base() #--- clase padre para definir las tablas


class Socio(Base):
 __tablename__ = 'socio'  #--- indispensable.
 idSoc = Column(Integer, primary_key=True)
 nombre = Column(String(30))
 apellido = Column(String(20))
 dni = Column(Integer)

engine = create_engine('sqlite:///tp5.db', echo=True)

Base.metadata.create_all(engine)















