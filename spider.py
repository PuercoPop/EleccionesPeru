
import psycopg2
import ParserDB,get_mesas
import re

print get_mesas.d_regiones
conn = pyscopg2.connect("dbname=eleccionesperu2011 user=pirata")
cursor = conn.cursor()
exp = re.compile('^(.*)cnume_acta=(\d+)$')

for k_reg in get_mesas.d_regiones.keys():
  prov = get_mesas.from_reg_get_provs( get_mesas.d_regiones[k_reg] )
  for k_prov in prov.keys():
    dist = get_mesas.from_prov_get_districts( prov[k_prov] )
    for k_dist in dist.keys():
      centros = get_mesas.from_district_get_centros( )
      for k_centro in centros.keys():
        mesas = get_mesas.from_centro_get_mesas( get_mesas.d_regions[k_reg], prov[k_prov], dist[k_dist], centros[k_centro] )
        url_actas = get_mesas.from_mesas_get_actas( mesas, get_mesas.str_2da_vuelta)
        for url in url_actas:
          html_acta = urllib2.urlopen(url)
          data = ParserDB.parse_acta(html_acta)
          r_acta = exp.search(url)
          ParserDB.insert_data_SVP(r_acta.group(2),data,cursor)
    

cursor.close()
conn.close()
