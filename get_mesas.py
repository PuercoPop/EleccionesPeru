#!/usr/bin/python2.7
# -*- coding: utf-8

import httplib
import urllib
import urllib2
import Parser
from BeautifulSoup import BeautifulSoup
import pdb

"""
<option value="010000">AMAZONAS</option> 
<option value="020000">ANCASH</option> 
<option value="030000">APURIMAC</option> 
<option value="040000">AREQUIPA</option> 
<option value="050000">AYACUCHO</option> 
<option value="060000">CAJAMARCA</option> 
<option value="240000">CALLAO</option> 
<option value="070000">CUSCO</option> 
<option value="080000">HUANCAVELICA</option> 
<option value="090000">HUANUCO</option> 
<option value="100000">ICA</option> 
<option value="110000">JUNIN</option> 
<option value="120000">LA LIBERTAD</option> 
<option value="130000">LAMBAYEQUE</option> 
<option value="140000">LIMA</option> 
<option value="150000">LORETO</option> 
<option value="160000">MADRE DE DIOS</option> 
<option value="170000">MOQUEGUA</option> 
<option value="180000">PASCO</option> 
<option value="190000">PIURA</option> 
<option value="200000">PUNO</option> 
<option value="210000">SAN MARTIN</option> 
<option value="220000">TACNA</option> 
<option value="230000">TUMBES</option> 
<option value="250000">UCAYALI</option>
"""


#d_provincias = {'Amazonas':'010000','Ancash':020000,'Apurimac':030000,'Arequipa':'040000', 'Ayacucho':'050000', 'Cajamarca':'060000', 'Callao':'240000', 'Cusco':'070000', 'Huancavelica':'080000', 'Huanuco':'090000', 'Ica':'100000', 'Junin':'110000', 'La Libertad':'120000', 'Lambayeque':'130000', 'Lima':'140000', 'Loreto':'150000', 'Madre de Dios':'160000', 'Moquegua':'170000', 'Pasco':'180000', 'Piura':'190000', 'Puno':'200000', 'San Martin':'210000', 'Tacna':'220000', 'Tumbes':'230000', 'Ucayali':'250000'}
d_regiones = {'Amazonas':'010000','Ancash':'020000','Apurimac':'030000','Arequipa':'040000', 'Ayacucho':'050000', 'Cajamarca':'060000', 'Callao':'240000', 'Cusco':'070000', 'Huancavelica':'080000', 'Huanuco':'090000', 'Ica':'100000', 'Junin':'110000', 'La Libertad':'120000', 'Lambayeque':'130000', 'Lima':'140000', 'Loreto':'150000', 'Madre de Dios':'160000', 'Moquegua':'170000', 'Pasco':'180000', 'Piura':'190000', 'Puno':'200000', 'San Martin':'210000', 'Tacna':'220000', 'Tumbes':'230000', 'Ucayali':'250000'}



str_2da_vuelta = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/"
str_1ra_vuelta = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/presidente/"
str_congreso   = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/"

url_query_2da_vuelta = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/extras/provincias.php"

def from_reg_get_provs( region):
    data = {}
    dict = {}
    data['elegido'] = region
    en_data = urllib.urlencode(data)  
    req = urllib2.Request('http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/extras/provincias.php', en_data )
    f = urllib2.urlopen(req)
    soup= BeautifulSoup(f.read() )
    for item in soup.findAll('option'):
        if item.string is not None:
            dict[ item.string]= item['value'] 
    return dict

def from_prov_get_districts( provincia ):
    data = {}
    dict = {}
    data['elegido'] = provincia
    en_data = urllib.urlencode(data)  
    req = urllib2.Request('http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/extras/distritos.php', en_data )
    f = urllib2.urlopen(req)
    soup= BeautifulSoup(f.read() )
    for item in soup.findAll('option'):
        if item.string is not None:
          dict[ item.string]= item['value'] 
    return dict
    
def from_district_get_centros(distrito):
    data = {}
    dict = {}
    data['elegido'] = distrito
    en_data = urllib.urlencode(data)  
    req = urllib2.Request('http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/extras/locales.php', en_data )
    f = urllib2.urlopen(req)
    soup= BeautifulSoup(f.read() )
    for item in soup.findAll('option'):
        if item.string is not None:
          dict[ item.string]= item['value'] 
    return dict
    
def from_centro_get_mesas( departamento, provincia,  distrito,  centro):
    data = {}
    dict = {}
    data['tipo_consulta1'] = 'UBIGEO'
    data['cnume_acta'] = ''
    data['ambito1'] = 'P'
    data['dpto'] = departamento
    data['prov'] = provincia
    data['dist'] = distrito
    data['local'] = centro
    data['estado'] = 'T'
    data['continente'] = ''
    data['pais'] = ''
    data['ciudad'] = ''
    data['embajada'] = ''
    data['estado2'] = 'T'
    en_data = urllib.urlencode(data)  
    req = urllib2.Request('http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/extras/buscar_ubigeo_actas.php', en_data )
    f = urllib2.urlopen(req)
    #print f.read()
    return f

def from_mesas_get_actas(f_html,str_prefix):
  """
  Del html extrae los links para cada acta
  """
  
  #str_prefix="http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/2davuelta/onpe/presidente/"
  #str_prefix="http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/presidente/"
  #str_prefix="http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/"
  url_actas = []
  soup = BeautifulSoup( f_html.read() )
  for item in soup.findAll('a'):
    url_actas.append( ''.join( [ str_prefix , item.attrs[0][1] ] ) )
  
  return url_actas
  

  
def from_acta_get_info():
  """
  Implementado en ParseDB parse_acta()
  """
  pass
    
""""
tipo_consulta1:UBIGEO
cnume_acta:
ambito1:P
dpto:010000
prov:010100
dist:010111
local:0012
estado:T
continente:
pais:
ciudad:
embajada:
estado2:T
"""

if __name__ == "__main__":
    
    #d = from_reg_get_provs( d_regiones['Amazonas'])
    #s = from_prov_get_districts( d['CHACHAPOYAS'] )
    #e = from_district_get_centros(s['LEVANTO'])
    #results = from_centro_get_mesas(d_regiones['Amazonas'], d['CHACHAPOYAS'],  s['LEVANTO'], e.values()[0])
    #links = from_mesas_get_actas( results, str_2da_vuelta )
    #print links
    #print results
    #for url in links:
    #  html_acta = urllib2.urlopen(url)
    #  f_tmp = open( url[-5:] + '.txt','w')
    #  Parser.parse_acta( html_acta , f_tmp )
    #  f_tmp.close()
    #f_results = open( 'tmp_resultados.html','w')
     
    #for line in results.read():
    #  f_results.write(line)
    
    html_acta = open('Ejemplo_Acta_Segunda_Vuelta.html','r')
    f_tmp = open('test.out','w')
    Parser.parse_acta( html_acta, f_tmp) 
    html_acta.close()
    f_tmp.close()
