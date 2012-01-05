# -*- coding: utf-8 -*-
from sqlalchemy import *

#url = URL(drivername='postgresql', username='postgresql', password='testo', host='localhost', database='template1')
#eng = create_engine(url)
#eng.execute('CREATE DATABASE new_db;')


engine = create_engine('postgresql://postgres:testo@localhost:5432/eleccionesperu', encoding='utf-8', echo=True)
metadata = MetaData()

info_mesas = Table('info_mesas', metadata,
                   Column('num_mesa', Integer, primary_key = True),
                   Column('local', String),
                   Column('distrito', String),
                   Column('provincia', String),
                   Column('direccion', String),
                   Column('electores_habiles', String)
                   )

congreso = Table('congreso', metadata,
                 Column('congreso_id',Integer, primary_key = True),
                 Column('num_mesa', Integer, ForeignKey('info_mesas.num_mesa') ),
                 #GanaPeru,Fuerza_2011,etc. Nulos y Viciados en la posicion #1
                 Column('agrupacion', String),
                 Column('1', Integer),
                 Column('2', Integer),
                 Column('3', Integer, nullable=True),
                 Column('4', Integer),
                 Column('5', Integer),
                 Column('6', Integer),
                 Column('7', Integer),
                 Column('8', Integer),
                 Column('9', Integer),
                 Column('10', Integer),
                 Column('11', Integer),
                 Column('12', Integer),
                 Column('13', Integer),
                 Column('14', Integer),
                 Column('15', Integer),
                 Column('16', Integer),
                 Column('17', Integer),
                 Column('18', Integer),
                 Column('19', Integer),
                 Column('20', Integer),
                 Column('21', Integer),
                 Column('22', Integer),
                 Column('23', Integer),
                 Column('24', Integer),
                 Column('25', Integer),
                 Column('26', Integer),
                 Column('27', Integer),
                 Column('28', Integer),
                 Column('29', Integer),
                 Column('30', Integer),
                 Column('31', Integer),
                 Column('32', Integer),
                 Column('33', Integer),
                 Column('34', Integer),
                 Column('35', Integer),
                 Column('36', Integer),

                 )


primera_vuelta =  Table('primera_vuelta', metadata,
                   Column('primera_vuelta_id', Integer, primary_key = True),
                   Column('num_mesa', Integer, ForeignKey('info_mesas.num_mesa') ),
                   Column('agrupacion', String),
                   Column('votos', Integer),
                   )

segunda_vuelta =  Table('segunda_vuelta', metadata,
                   Column('segunda_vuelta_id', Integer, primary_key = True),
                   Column('num_mesa', Integer, ForeignKey('info_mesas.num_mesa') ),
                   Column('agrupacion', String),
                   Column('votos', Integer),
                   )

metadata.create_all(engine)
