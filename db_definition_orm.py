# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Info(Base):
    __tablename__ = 'info_mesas'
    
    num_mesa = Column(Integer, primary_key=True, nullable = False)
    local = Column(String, nullable = False)
    distrito = Column(String, nullable = False)
    provincia = Column(String, nullable = False)
    departamento = Column(String, nullable = False)
    direccion = Column(String, nullable = False)
    electores_habiles = Column(String, nullable = False)

    def __init__(self, num_mesa, local, distrito, provincia, direccion, electores_habiles):
        self.num_mesa = num_mesa
        self.local = local
        self.distrito = distrito
        self.provincia = provincia
        self.direccion = direccion
        self.electores_habiles = electores_habiles

    def __repr__(self):
        return "%s en %s" % (self.num_mesa, self.local)

class Primera_Vuelta(Base):
    __tablename__ = 'primera_vuelta'

    id = Column(Integer, primary_key = True)
    num_mesa = Column( Integer, ForeignKey('info_mesas.num_mesa'), nullable=False)
    agrupacion = Column( String, nullable=False )
    votos = Column( Integer, nullable=False)
    
    info = relationship("Info", backref=backref('info_mesas', order_by='num_mesa'))
    
    def __init__(self, num_mesa, agrupacion, votos):
        self.num_mesa = num_mesa
        self.agrupacion = agrupacion
        self.votos = votos

    def __repr__(self):
        return '%s : %s' % (self.agrupacion, self.votos)

class Segunda_Vuelta(Base):
    __tablename__ = 'segunda_vuelta'

    id = Column(Integer, primary_key = True)
    num_mesa = Column( Integer, ForeignKey('info_mesas.num_mesa'), nullable=False)
    agrupacion = Column( String, nullable=False )
    votos = Column( Integer, nullable=False)

    info = relationship("Info", backref=backref('info_mesas', order_by='num_mesa'))

    def __init__(self, num_mesa, agrupacion, votos):
        self.num_mesa = num_mesa
        self.agrupacion = agrupacion
        self.votos = votos

    def __repr__(self):
        return '%s : %s' % (self.agrupacion, self.votos)

class Congreso(Base):
    __tablename__ = 'congreso'

    info = relationship("Info", backref=backref('info_mesas', order_by='num_mesa'))

    id = Column(Integer, primary_key = True)
    num_mesa = Column(Integer, ForeignKey('info_mesas.num_mesa'))
    agrupacion = Column(String, nullable=False)
    candidato_1 = Column(Integer, nullable=False)
    candidato_2 = Column(Integer, nullable=True)
    candidato_3 = Column(Integer, nullable=True)
    candidato_4 = Column(Integer, nullable=True)
    candidato_5 = Column(Integer, nullable=True)
    candidato_6 = Column(Integer, nullable=True)
    candidato_7 = Column(Integer, nullable=True)
    candidato_8 = Column(Integer, nullable=True)
    candidato_9 = Column(Integer, nullable=True)
    candidato_10 = Column(Integer, nullable=True)
    candidato_11 = Column(Integer, nullable=True)
    candidato_12 = Column(Integer, nullable=True)
    candidato_13 = Column(Integer, nullable=True)
    candidato_14 = Column(Integer, nullable=True)
    candidato_15 = Column(Integer, nullable=True)
    candidato_16 = Column(Integer, nullable=True)
    candidato_17 = Column(Integer, nullable=True)
    candidato_18 = Column(Integer, nullable=True)
    candidato_19 = Column(Integer, nullable=True)
    candidato_20 = Column(Integer, nullable=True)
    candidato_21 = Column(Integer, nullable=True)
    candidato_22 = Column(Integer, nullable=True)
    candidato_23 = Column(Integer, nullable=True)
    candidato_24 = Column(Integer, nullable=True)
    candidato_25 = Column(Integer, nullable=True)
    candidato_26 = Column(Integer, nullable=True)
    candidato_27 = Column(Integer, nullable=True)
    candidato_28 = Column(Integer, nullable=True)
    candidato_29 = Column(Integer, nullable=True)
    candidato_30 = Column(Integer, nullable=True)
    candidato_31 = Column(Integer, nullable=True)
    candidato_32 = Column(Integer, nullable=True)
    candidato_33 = Column(Integer, nullable=True)
    candidato_34 = Column(Integer, nullable=True)
    candidato_35 = Column(Integer, nullable=True)
    candidato_36 = Column(Integer, nullable=True)

    def __init(self, num_mesa, agrupacion, candidato_1,
               candidato_2='Null',
               candidato_3='Null',
               candidato_4='Null',
               candidato_5='Null',
               candidato_6='Null',
               candidato_7='Null',
               candidato_8='Null',
               candidato_9='Null',
               candidato_10='Null',
               candidato_11='Null',
               candidato_12='Null',
               candidato_13='Null',
               candidato_14='Null',
               candidato_15='Null',
               candidato_16='Null',
               candidato_17='Null',
               candidato_18='Null',
               candidato_19='Null',
               candidato_20='Null',
               candidato_21='Null',
               candidato_22='Null',
               candidato_23='Null',
               candidato_24='Null',
               candidato_25='Null',
               candidato_26='Null',
               candidato_27='Null',
               candidato_28='Null',
               candidato_29='Null',
               candidato_30='Null',
               candidato_31='Null',
               candidato_32='Null',
               candidato_33='Null',
               candidato_34='Null',
               candidato_35='Null',
               candidato_36='Null'):
        self.num_mesa = num_mesa
        self.agrupacion = agrupacion
        self.candidato_1 = candidato_1
        self.candidato_2 = candidato_2
        self.candidato_3 = candidato_3
        self.candidato_4 = candidato_4
        self.candidato_5 = candidato_5
        self.candidato_6 = candidato_6
        self.candidato_7 = candidato_7
        self.candidato_8 = candidato_8
        self.candidato_9 = candidato_9
        self.candidato_10 = candidato_10
        self.candidato_11 = candidato_11
        self.candidato_12 = candidato_12
        self.candidato_13 = candidato_13
        self.candidato_14 = candidato_14
        self.candidato_15 = candidato_15
        self.candidato_16 = candidato_16
        self.candidato_17 = candidato_17
        self.candidato_18 = candidato_18
        self.candidato_19 = candidato_19
        self.candidato_20 = candidato_20
        self.candidato_21 = candidato_21
        self.candidato_22 = candidato_22
        self.candidato_23 = candidato_23
        self.candidato_24 = candidato_24
        self.candidato_25 = candidato_25
        self.candidato_26 = candidato_26
        self.candidato_27 = candidato_27
        self.candidato_28 = candidato_28
        self.candidato_29 = candidato_29
        self.candidato_30 = candidato_30
        self.candidato_31 = candidato_31
        self.candidato_32 = candidato_32
        self.candidato_33 = candidato_33
        self.candidato_34 = candidato_34
        self.candidato_35 = candidato_35
        self.candidato_36 = candidato_36

    def __repr(self):
        return u"%s en %s" % (self.agrupacion, self.num_mesa)

if __name__ == "__main__":
    pass
