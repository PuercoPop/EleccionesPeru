#!/usr/bin/python2.7
# -*- coding: utf-8

from BeautifulSoup import BeautifulSoup
import pdb

#f_handle = open('test.html','r')
f_handle = open('tmp2.html','r')
"""
Dentro de una tabla de align center esta la información de ubigeo

Dentro de la tabla de clase "borde_tabla" estan los resultados.
De los tr heigh="40" en el span dentro del td align left esta el nombre de la organización
Del 2do td align=center dentro del span de class arial_contenido esta el número
"""
 
soup = BeautifulSoup( f_handle )
a = soup.findAll('tr',height="40")

Organ = [u'GANA PERU',u'DESPERTAR NACIONAL', u'FUERZA 2011', u'PERU POSIBLE', u'ALIANZA SOLIDARIDAD NACIONAL', u'ALIANZA POR EL GRAN CAMBIO', u'ADELANTE', u'JUSTICIA, TECNOLOGIA, ECOLOGIA', u'FONAVISTAS DEL PERU', u'FUERZA NACIONAL', u'PARTIDO DESCENTRALISTA FUERZA SOCIAL', u'Votos Blancos', u'Votos Nulos', u'Votos Impugnados']

T_Flag = False
for item in soup.findAll('tr'):
  for item2 in BeautifulSoup(str(item)).findAll('span',{'class':'arial_contenido_negrita'}):
    if T_Flag == True:
      if item2.contents == []:
        votacion = 0
      else:
        votacion = int(item2.contents[0])
      print curr_Organ , ':' , votacion 
      T_Flag = False
    if not(item2.contents == []):
      if item2.contents[0] in Organ:
       T_Flag = True 
       curr_Organ = item2.contents[0]

  for item2 in BeautifulSoup(str(item)).findAll('span',{'class':'arial_contenido'}):
    if T_Flag == True:
      if item2.contents == []:
        votacion = 0
      else:
        votacion = int(item2.contents[0])
      print curr_Organ , ':' , votacion 
      T_Flag = False
    if not(item2.contents == []):
      if item2.contents[0] in Organ:
       T_Flag = True 
       curr_Organ = item2.contents[0]

print '------------' 

Categorias = [ u'Departamento:', u'Provincia:', u'Distrito:', u'Local de Votaci&oacute;n: ', u'Direcci&oacute;n: ', u'Electores H&aacute;biles: ', u'Total de Ciudadanos que Votaron: ']  #, u'Estado del acta: ', u'Historial del acta: ']

Printable_Categorias = []

T_Flag = False

tmp_soup = BeautifulSoup( str( soup.findAll('table',{'align':'center', 'border':'0'})[0] ) )

for item in tmp_soup.findAll('td',{'class':'arial_contenido'}):
  if not(item.contents[0] == u'&nbsp;'):
    if T_Flag == True:
      print curr_Categoria,':',item.contents[0]
      T_Flag = False
    if item.contents[0] in Categorias:
      T_Flag = True
      curr_Categoria = item.contents[0]
print '-------------'


for item in tmp_soup.findAll('td',{'class':'arial_contenido_negrita'}):
  if not(item.contents[0] == u'&nbsp;'):
    pass
    #print item.contents

for item in tmp_soup.findAll('td',{'class':'arial_titulo'}):
  if not(item.contents[0] == u'&nbsp;'):
    pass
    #print item.contents
#b = BeautifulSoup.BeautifulSoup(str(a))
#c = BeautifulSoup.BeautifulSoup( str( b.find('td',align="left" ) ) )

#print b.find('td',align="left")
#pdb.set_trace()
#print soup.prettify()
