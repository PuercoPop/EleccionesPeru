#-*- coding:utf-8
import sqlalchemy
from sqlalchemy import Column, Integer, String

Base = sqlalchemy.ext.declarative.declarative_base()
class elecciones_congreso(Base):
    __tablename__ = 'elecciones_congreso'

    #id = Column(Integer, primary_key=True)
    num_mesa = Column(Integer, primary_key=True)
    centro_educativo = Column(String)
    distrito = Column(String)
    provincia = Column(String)
    direccion = Column(String)
    electores_habiles = Column(Integer)
    
    def __init__(self,):
        pass

    def __repr__(self):
        return "%s de %s en %s, %s" % (self.num_mesa,self.centro_educativo,self.distrito,self.provincia)
    

if __name__ == "__main__":
    engine = sqlalchemy.create_engine('postgresql://pirata:pirata@localhost:5432/elecciones',encoding='utf-8')
