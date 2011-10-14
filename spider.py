#!/usr/bin/python2.7
# -*- coding: utf-8
"""
Command Lines
print diccionaries
start from: ---
"""

import psycopg2
import ParserDB,get_mesas
import re,urllib2,sys,argparse

class Args:
  pass
options = Args()

parser = argparse.ArgumentParser()
parser.add_argument("--skip-until",action="store", dest="target")
parser.add_argument("--post-codes",action="store_true", dest="get_post_codes")
parser.add_argument("--store-ubigeos", action="store_true", dest="get_ubigeos")
parser.add_argument("--crawl-province",action="store", dest="target_province")
parser.add_argument("--crawl-region", action="store", dest="target_region")
parser.add_argument("--crawl-district", action="store", dest="target_district")
parser.add_argument("--database", action="store",dest="database",help="database:user")
parser.parse_args(namespace=options)
d_opt = vars(options)

def main(d_args):
  if d_opt[database]:
    [ dbname, user ] = d_opt[database].split(':')
    conn = psycopg2.connect("dbname="+dbname+"user="+user)
  else:
    conn = psycopg2.connect("dbname=eleccionesperu2011 user=pirata")
  cursor = conn.cursor()


  if d_args['get_ubigeos']:
    for k_reg in get_mesas.d_regiones.keys():
      prov = get_mesas.from_reg_get_provs( get_mesas.d_regions[k_reg] )
      for k_prov in prov.keys():
        dist = get_mesas.from_prov_get_districts( prov[k_prov] )
        for k_dist in dist.keys():
          centros = get_mesas.from_district_get_centros( dist[k_dist] )
          for k_centro in centros.keys()
            ParserDB.insert_post_codes(k_reg,k_prov,k_dist,k_centro,cursor)
  elif d_args['get_post_codes']:
    pass
  else:
    for k_reg in get_mesas.d_regiones.keys():
      prov = get_mesas.from_reg_get_provs( get_mesas.d_regiones[k_reg] )
      for k_prov in prov.keys():
        dist = get_mesas.from_prov_get_districts( prov[k_prov] )
        for k_dist in dist.keys():
          centros = get_mesas.from_district_get_centros( dist[k_dist] )
          for k_centro in centros.keys():
            mesas = get_mesas.from_centro_get_mesas( get_mesas.d_regiones[k_reg], prov[k_prov], dist[k_dist], centros[k_centro] )
            url_actas = get_mesas.from_mesas_get_actas( mesas, get_mesas.str_2da_vuelta)
            for url in url_actas:
              r_acta = exp.search(url)
              try:
                html_acta = urllib2.urlopen(url)
              except urllib2.HTTPError, e:
                f_log = open('error.log','a')
                f_log.write(''.join( [ str(r_acta),',',centros[k_centro],',',dist[k_dist],',',prov[k_prov],'\n']))
                f_log.close()
              data = ParserDB.parse_acta(html_acta)
              ParserDB.insert_data_SVP(r_acta.group(2),data,cursor)
              conn.commit()
    

  cursor.close()
  conn.close()

    
"""
conn = psycopg2.connect("dbname=eleccionesperu2011 user=pirata")
cursor = conn.cursor()
exp = re.compile('^(.*)cnume_acta=(\d+)$')

if len(sys.argv) > 1:
  if sys.argv[1] == "dictionaries":
    for k_reg in get_mesas.d_regiones.keys():
      prov = get_mesas.from_reg_get_provs( get_mesas.d_regiones[k_reg] )
      for k_prov in prov.keys():
        dist = get_mesas.from_prov_get_districts( prov[k_prov] )
        for k_dist in dist.keys():
          centros = get_mesas.from_district_get_centros( dist[k_dist] )
          print centros
    sys.exit(0)

  if sys.argv[1] == "skip-until":
    skip = True
    for k_reg in get_mesas.d_regiones.keys():
      prov = get_mesas.from_reg_get_provs( get_mesas.d_regiones[k_reg] )
      for k_prov in prov.keys():
        dist = get_mesas.from_prov_get_districts( prov[k_prov] )
        for k_dist in dist.keys():
          centros = get_mesas.from_district_get_centros( dist[k_dist] )
          for k_centro in centros.keys():
            if skip:
              print k_centro,':',k_dist
              if str(k_centro) == sys.argv[2]: #str to convert 'unicode' to 'str'
                skip = False
              else:
                pass
            else:
              mesas = get_mesas.from_centro_get_mesas( get_mesas.d_regiones[k_reg], prov[k_prov], dist[k_dist], centros[k_centro] )
              url_actas = get_mesas.from_mesas_get_actas( mesas, get_mesas.str_2da_vuelta)
              for url in url_actas:
                r_acta = exp.search(url)
                try:
                  html_acta = urllib2.urlopen(url)
                except urllib2.HTTPError, e:
                  f_log = open('error.log','a')
                  f_log.write(''.join( [ str(r_acta),',',centros[k_centro],',',dist[k_dist],',',prov[k_prov],'\n']))
                  f_log.close()
                data = ParserDB.parse_acta(html_acta)
                ParserDB.insert_data_SVP(r_acta.group(2),data,cursor)
                conn.commit()
    sys.exit(0) 


for k_reg in get_mesas.d_regiones.keys():
  prov = get_mesas.from_reg_get_provs( get_mesas.d_regiones[k_reg] )
  for k_prov in prov.keys():
    dist = get_mesas.from_prov_get_districts( prov[k_prov] )
    for k_dist in dist.keys():
      centros = get_mesas.from_district_get_centros( dist[k_dist] )
      for k_centro in centros.keys():
        mesas = get_mesas.from_centro_get_mesas( get_mesas.d_regiones[k_reg], prov[k_prov], dist[k_dist], centros[k_centro] )
        url_actas = get_mesas.from_mesas_get_actas( mesas, get_mesas.str_2da_vuelta)
        for url in url_actas:
          r_acta = exp.search(url)
          try:
            html_acta = urllib2.urlopen(url)
          except urllib2.HTTPError, e:
            f_log = open('error.log','a')
            f_log.write(''.join( [ str(r_acta),',',centros[k_centro],',',dist[k_dist],',',prov[k_prov],'\n']))
            f_log.close()
          data = ParserDB.parse_acta(html_acta)
          ParserDB.insert_data_SVP(r_acta.group(2),data,cursor)
          conn.commit()
    

cursor.close()
conn.close()
"""

if __name__ == "__main__":
  main(options)
