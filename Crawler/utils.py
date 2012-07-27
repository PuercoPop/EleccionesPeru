# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import constants


def compose_url(place_type):
    if place_type == 'region':
        suffix = 'extras/provincias.php'
    elif place_type == 'provincia':
        suffix = 'extras/distritos.php'
    elif place_type == 'distrito':
        suffix = 'extras/locales.php'
    elif place_type == 'centro de votacion':
        suffix = 'extras/buscar_ubigeo_actas.php'
    elif place_type == 'mesa':
        suffix = 'rep_acta_cong.php'
    else:
        return None

    return constants.url_prefix + suffix


def parse_region_response(data=None):
    """
    Usage:
    with open('example_response.html', 'r') as f_data:
        data = f_data.read()
    result:
    [(Cañete, 1403000),...]
    """

    if data is None:
        return None

    result = []
    soup = BeautifulSoup(data)
    for item in soup.find_all('option'):
        if item.string is not None:
            result.append((u'%s' % item.string, u'%s' % item['value']))

    return result

if __name__ == "__main__":
    print parse_region_response()
