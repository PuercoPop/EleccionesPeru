# -*- coding: utf-8 -*-

import unittest
from utils import parse_region_response, compose_url
import constants


class UtilTest(unittest.TestCase):
    def setUp(self):
        # MAke DB
        pass
    def test_comporse_url(self):
        self.assertEqual(compose_url(place_type='region'),
                         'http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/extras/provincias.php')
        self.assertEqual(compose_url(place_type='provincia'),
                         'http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/extras/distritos.php')
        self.assertEqual(compose_url(place_type='distrito'),
                         'http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/extras/locales.php')
        self.assertEqual(compose_url(place_type='centro de votacion'),
                         'http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/extras/buscar_ubigeo_actas.php')
        self.assertEqual(compose_url(place_type='mesa'),
                         'http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/rep_acta_cong.php')
        self.assertEqual(compose_url(place_type=None), None)


    def test_parse_region_response(self):

        self.assertEqual(parse_region_response(data=None),None)

        with open('example_response.html', 'r') as f_data:
            data = f_data.read()

        self.assertEqual(parse_region_response(data),[(u'LIMA', u'140100'), (u'CAJATAMBO', u'140200'), (u'CANTA', u'140300'), (u'CAÑETE', u'140400'), (u'HUAURA', u'140500'), (u'HUAROCHIRI', u'140600'), (u'YAUYOS', u'140700'), (u'HUARAL', u'140800'), (u'BARRANCA', u'140900'), (u'OYON', u'141000')])

        
        def test_insert_into_db(self):
            pass


if __name__ == "__main__":
    unittest.main()
