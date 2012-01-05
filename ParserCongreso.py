# -*- coding: utf8 -*-

from BeautifulSoup import BeautifulSoup

"""
f_acta = open('test_cases/Ejemplo_Acta_Congreso_2.html','r')

soup = BeautifulSoup( f_acta.read() )

partidos = []
for item in soup.findAll('td',{'class':'borde_celda','align':'left'}):
  if item.has_key('colspan'):
    pass
  else:
    partidos.append( item.next.next )

for item in soup.findAll('tr',{'height':'40'}):
  #print "item:", item
  fPass = True
  #Hay que primero saber cuantos organizaciones hay
  for item2 in item.findAll('td',{'align':'center'}):
    #Get Info about max number of congressmen
    if item2.has_key('colspan'):
      if item2['colspan'] == "":
        fPass = False
    elif fPass == True:
      max_cong = item2.next.next
    else:
      break

counter_congresista = 0
counter_partido = 0
votacion = [ [] ]
for item in soup.findAll('td',{'align':'center'}):
  if item.has_key('colspan') or item.has_key('bgcolor') or item.has_key('rowspan'):
    pass
  else:
    if item.has_key('class') and item['class'] == 'arial_contenido':
      pass
    else:
      if item.next.has_key('class') and (u'negrita' in item.next['class'].split() or u'arial_contenido_negrita' in item.next['class'].split()):
        pass
      elif counter_partido < len(partidos):
        #Crea listas dentro de la lista de votación con las votaciones de los partidos en cadena
        votacion[-1].append( item.next.next )
        counter_congresista += 1
        if counter_congresista % int(max_cong) == 0:
          votacion.append( [] )
          counter_partido += 1
      else:
        #Votos Blancos, Nulos e Impugnados
        votacion[-1].append( item.next.next )

#Ahora traducir  la lista de listas de str a int
votacion_int = []
for li in votacion:
  votacion_int.append( [] )
  for item in li:
    if item == u'\n':
      votacion_int[-1].append( 0 )
    else:
      votacion_int[-1].append( int(item) )

#Votaciones Totales

votaciones_totales_partidos = []
for item in soup.findAll('td',{'align':'CENTER'}):
  votaciones_totales_partidos.append( item.next.next )

for item in soup.findAll('td',{'align':'center'}):
  if item.has_key('bgcolor') and item['bgcolor'] == '#CCCCCC':
    votos_totales= item.next.next

votaciones_totales_partidos_int = []
for item in votaciones_totales_partidos:
  if item == u'\n':
    votaciones_totales_partidos_int.append( 0 )
  else:
    votaciones_totales_partidos_int.append( int(item) )
 
#Ahora obtener la info de ubigeo
skipped_items = [u'Mesa N°', u'Departamento:', u'Provincia:', u'Distrito:', u'Local de Votación:', u'Dirección:', u'INFORMACIÓN DE MESA', u'Electores Hábiles:', u'Estado del acta:', u'Historial del acta:']
info_ubigeo = []
for item in soup.findAll('table',{'border':'0'}):
  if item.has_key('cellspacing'):
    pass
  else:
    for item2 in item.findAll('td', {'align':'left'} ):
      if item2.has_key('nowrap'):# or item2 is None:
        pass
      elif item2.next == u'&nbsp;' or item2.next == u'\n':
        pass
      elif item2.next.replace('\n','').replace('\t','').strip() in skipped_items:
        pass
      else:
        info_ubigeo.append( item2.next.replace('\n','').replace('\t','').strip() )
        

        
#Pones la info en un diccionario con la data

d_data = {}
#ubigeo
t_keys = [ 'mesa_num', 'copia', 'departamento', 'provincia', 'distrito', 'local', 'dirección', 'electores_hab', 'electores_tot', 'estado_acta', 'historia_acta']
for item, k in zip(info_ubigeo,t_keys):
  d_data[k] = item

#votacion por partido precedido de la votacion total del partido
for k,vot,vot_tot in zip( partidos + [ u'votos blancos', u'Nulos', u'Impugnados'] , votacion_int, votaciones_totales_partidos_int ):
  d_data[k] = vot
  d_data[k].insert(0,vot_tot)

#extra info
d_data['partidos'] = partidos
d_data['max_cong'] = max_cong
d_data['votos_totales'] = votos_totales

#print votacion
print "Info Ubigeo:",info_ubigeo
print "Votación por partidos:", votaciones_totales_partidos_int
print "Votación:",votacion_int
print "Votos Totales:", votos_totales
print "Número de Candidatos:", max_cong
print "Número de Partidos:", len(partidos)
print "Lista de Partidos:",partidos

print "Return Dict:",d_data
"""
def parse_acta_congreso( f_acta ):
  soup = BeautifulSoup( f_acta.read() )
  partidos = []
  for item in soup.findAll('td',{'class':'borde_celda','align':'left'}):
    if item.has_key('colspan'):
      pass
    else:
      partidos.append( item.next.next )

  for item in soup.findAll('tr',{'height':'40'}):
    fPass = True
    #Hay que primero saber cuantos organizaciones hay
    for item2 in item.findAll('td',{'align':'center'}):
      #Get Info about max number of congressmen
      if item2.has_key('colspan'):
        if item2['colspan'] == "":
          fPass = False
      elif fPass == True:
        max_cong = item2.next.next
      else:
        break

  counter_congresista = 0
  counter_partido = 0
  votacion = [ [] ]
  for item in soup.findAll('td',{'align':'center'}):
    if item.has_key('colspan') or item.has_key('bgcolor') or item.has_key('rowspan'):
      pass
    else:
      if item.has_key('class') and item['class'] == 'arial_contenido':
        pass
      else:
        if item.next.has_key('class') and (u'negrita' in item.next['class'].split() or u'arial_contenido_negrita' in item.next['class'].split()):
          pass
        elif counter_partido < len(partidos):
          #Crea listas dentro de la lista de votación con las votaciones de los partidos en cadena
          votacion[-1].append( item.next.next )
          counter_congresista += 1
          if counter_congresista % int(max_cong) == 0:
            votacion.append( [] )
            counter_partido += 1
        else:
          #Votos Blancos, Nulos e Impugnados
          votacion[-1].append( item.next.next )

  #Ahora traducir  la lista de listas de str a int
  votacion_int = []
  for li in votacion:
    votacion_int.append( [] )
    for item in li:
      if item == u'\n':
        votacion_int[-1].append( 0 )
      else:
        votacion_int[-1].append( int(item) )

  #Votaciones Totales

  votaciones_totales_partidos = []
  for item in soup.findAll('td',{'align':'CENTER'}):
    votaciones_totales_partidos.append( item.next.next )

  for item in soup.findAll('td',{'align':'center'}):
    if item.has_key('bgcolor') and item['bgcolor'] == '#CCCCCC':
      votos_totales= item.next.next

  votaciones_totales_partidos_int = []
  for item in votaciones_totales_partidos:
    if item == u'\n':
      votaciones_totales_partidos_int.append( 0 )
    else:
      votaciones_totales_partidos_int.append( int(item) )
 
  #Ahora obtener la info de ubigeo
  skipped_items = [u'Mesa N°', u'Departamento:', u'Provincia:', u'Distrito:', u'Local de Votación:', u'Dirección:', u'INFORMACIÓN DE MESA', u'Electores Hábiles:', u'Estado del acta:', u'Historial del acta:']
  info_ubigeo = []
  for item in soup.findAll('table',{'border':'0'}):
    if item.has_key('cellspacing'):
      pass
    else:
      for item2 in item.findAll('td', {'align':'left'} ):
        if item2.has_key('nowrap'):# or item2 is None:
          pass
        elif item2.next == u'&nbsp;' or item2.next == u'\n':
          pass
        elif item2.next.replace('\n','').replace('\t','').strip() in skipped_items:
          pass
        else:
          info_ubigeo.append( item2.next.replace('\n','').replace('\t','').strip() )
        
  #Pones la info en un diccionario con la data

  d_data = {}
  #ubigeo
  t_keys = [ 'mesa_num', 'copia', 'departamento', 'provincia', 'distrito', 'local', 'dirección', 'electores_hab', 'electores_tot', 'estado_acta', 'historia_acta']
  for item, k in zip(info_ubigeo,t_keys):
    d_data[k] = item

  #votacion por partido precedido de la votacion total del partido
  for k,vot,vot_tot in zip( partidos + [ u'votos blancos', u'Nulos', u'Impugnados'] , votacion_int, votaciones_totales_partidos_int ):
    d_data[k] = vot
    d_data[k].insert(0,vot_tot)

  #extra info
  d_data['partidos'] = partidos
  d_data['max_cong'] = max_cong
  d_data['votos_totales'] = votos_totales

  return d_data

if __name__ == "__main__":
  f_acta = open('test_cases/Ejemplo_Acta_Congreso_2.html','r')
  data = parse_acta_congreso( f_acta)
  for k_iter in data.keys():
    print k_iter,' : ',data[k_iter]
  f_acta.close()