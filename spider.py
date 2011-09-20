
import Parser,get_mesas

print get_mesas.d_regiones

for k_reg in get_mesas.d_regiones.keys():
  prov = get_mesas.from_reg_get_provs( get_mesas.d_regiones[k_reg] )
  for k_prov in prov.keys():
    dist = get_mesas.from_prov_get_districts( prov[k_prov] )
    for k_dist in dist.keys():
      centros = get_mesas.from_district_get_centros( )
      for k_centro in centros.keys():
	mesas = get_mesas.from_centro_get_mesas( get_mesas.d_regions[k_reg], prov[k_prov], dist[k_dist], centros[k_centro] )
	url_actas = get_mesas.from_mesas_get_actas( mesas, get_mesas.str_1ra_vuelta)
    
  print dist