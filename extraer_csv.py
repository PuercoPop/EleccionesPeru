#!/usr/bin/python2.7
# -*- coding: utf-8
import csv


f_handle = open('resumen_padron_x_distritos_ERM2010.csv','r')
reader = csv.reader(f_handle)
start_flag = False

#Con esto extraigo todos los números de mesa

for row in reader:
  if start_flag is True:
    print( ''.join( [ 'http://www.elecciones2011.onpe.gob.pe/resultados2011/1ravuelta/onpe/presidente/rep_mesas_det_pre.php?cnume_acta=' ,row[0] ] ) )
  if row[0] == 'Ubigeo':
    start_flag = True
    print('Go Speed Racer Go')


#ahora compongo todas las URL para ver la info de mesa
#http://www.elecciones2011.onpe.gob.pe/resultados2011/1ravuelta/onpe/presidente/rep_mesas_det_pre.php?cnume_acta=167037


