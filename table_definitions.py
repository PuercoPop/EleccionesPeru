from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData, ForeignKey
import ConfigParser

def conf_engine():
  """
  Lee la configuracion sobre la pase de datos
  """
  conf = ConfigParser.ConfigParser()
  try:
    conf.readfp(open('database.conf'))
  except IOError as (errno, strerror):
    if errno == 2:
      return create_engine('sqlite:///:memory', echo=True)
    else:
      f_log = open('logs/error.log','w+')
      f_log.write( "I/O error({0}): {1}\n".format(errno, strerror) )
      f_log.close()
 
  backend = conf.get('Database','backend')
  
  

  return engine

def make_tables(metadata)
  ubigeos = Table( 'ubigeos', metadata,
    Column('Departamento',String(100)),
    Column('Provincia',String(100)),
    Column('Distrito',String(100)),
    Column('Local',String(100)),
    Column('num_mesa',Integer,primary_key=True)
  )
  
  pres_1ra = Table( 
  )
  
  pres_2da = Table( 'presidente_2da_vuelta', metadata,
    Column('Gana_Peru',Integer),
    Column('Fuerza_2011',Integer),
    Column('Votos_Blancos',Integer),
    Column('Votos_Nulos',Integer),
    Column('Votos_Impugnados',Integer),
    Column('num_mesa',ForeignKey("ubigeos.num_mesa")),
    Column('Estado_del_Acta',String(50)),
    Column('Electores_Hábiles',Integer),
    Column('Total_Ciudadanos',Integer)
  )
  
  cong = Table('congreso', metadata,
    Column('Gana_Peru',Integer),
    Column('Desptar_Nacional',Integer),
    Column('Fuerza_2011',Integer),
    Column('Peru_Posible',Integer),
    Column('Alianza_Solidaridad_Nacional',Integer),
    Column('Alianza_por_el_Gran_Cambio',Integer),
    Column('Adelante',Integer),
    Column('Partido_Aprista_Peruano',Integer),
    Column('Justicia_Tecnología_Ecología',Integer),
    Column('Fonavistas_de_Perú',Integer),
    Column('Fuerza_Nacional',Integer),
    Column('Partido_Descentralista_Fuerza_Social',Integer),
    Column('Cambio_Radical',Integer),
    Column('Votos_Blancos',Integer),
    Column('Votos_Nulos',Integer),
    Column('Votos_Impugnados',Integer),
    Column('num_mesa',ForeignKey("ubigeos.num_mesa")),
    Column('Estado_del_Acta',String(50)),
    Column('Electores_Hábiles',Integer),
    Column('Total_Ciudadanos',Integer)
  )
  
  cong_gana_peru = Table('congreso_gana_peru', metadata,
    Column('1',Integer),
    Column('2',Integer),
    Column('3',Integer),
    Column('4',Integer),
    Column('5',Integer),
    Column('6',Integer),
    Column('7',Integer),
    Column('8',Integer),
    Column('9',Integer),
    Column('10',Integer),
    Column('11',Integer),
    Column('12',Integer),
    Column('13',Integer),
    Column('14',Integer),
    Column('15',Integer),
    Column('16',Integer),
    Column('17',Integer),
    Column('18',Integer),
    Column('19',Integer),
    Column('20',Integer),
    Column('21',Integer),
    Column('22',Integer),
    Column('23',Integer),
    Column('24',Integer),
    Column('25',Integer),
    Column('26',Integer),
    Column('27',Integer),
    Column('28',Integer),
    Column('29',Integer),
    Column('30',Integer),
    Column('31',Integer),
    Column('33',Integer),
    Column('34',Integer),
    Column('35',Integer),
    Column('num_mesa',ForeignKey("ubigeos.num_mesa")),
    Column('Estado_del_Acta',String(50)),
    Column('Electores_Hábiles',Integer),
    Column('Total_Ciudadanos',Integer)
  )
  
  #metadata.create_all(engine)
  return metadata
  
engine = conf_engine()
metadata = MetaData()
