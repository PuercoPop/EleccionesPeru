# -*- coding: utf8 -*-

from BeautifulSoup import BeautifulSoup
import re

exp1 = re.compile(r"<td class=\"borde_celda\" align=\"left\"><span class=\"arial_contenido\">(.*)</span></td>")
exp = re.compile(r"<td class=\"borde_celda\" align=\"left\">")

f_acta = open('test_cases/Ejemplo_Acta_Congreso_2.html','r')

"""for line in f_acta:
  m = exp1.search(line)
  if m is None:
    pass
  else:
    print m.groups()
"""

soup = BeautifulSoup( f_acta.read() )
"""
for item in soup.findAll('td',{"class":"borde_celda","align":"left"}):
  print item
  for item2 in item.findAll('span',{"class":"arial_contenido"}):
    for item3 in item2.findAll('td',{"align":"center"}):
      print item3
  for item2 in item.findAll('span',{"class":"arial_contenido_negrita"}):
    print item2
"""
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
          print "break"
          counter_partido += 1
      else:
        #Votos Blancos, Nulos e Impgunados
        votacion[-1].append( item.next.next )
          
print votacion
print "Número de Candidatos:", max_cong
print "Número de Partidos:", len(partidos)
print "Lista de Partidos:",partidos