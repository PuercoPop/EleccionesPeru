# -*- coding: utf-8 -*-

from urllib import urlencode
from  urllib2 import Request, urlopen
from BeautifulSoup import BeautifulSoup
import Elecciones.models as m

from django.core.management import setup_environ 
import settings 
setup_environ(settings)

class ONPEcrawler():
    def __init__(self, url):
        #http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/rep_acta_cong.php
        self.url = url
        self.departamentos = { 'Lima':'140000' }
        """
        self.departamentos = {'Amazonas':'010000',
                              'Ancash':'020000',
                              'Apurimac':'030000',
                              'Arequipa':'040000',
                              'Ayacucho':'050000', 
                              'Cajamarca':'060000',
                              'Callao':'240000',
                              'Cusco':'070000',
                              'Huancavelica':'080000',
                              'Huanuco':'090000',
                              'Ica':'100000',
                              'Junin':'110000',
                              'La Libertad':'120000',
                              'Lambayeque':'130000',
                              'Lima':'140000',
                              'Loreto':'150000',
                              'Madre de Dios':'160000',
                              'Moquegua':'170000',
                              'Pasco':'180000',
                              'Piura':'190000',
                              'Puno':'200000',
                              'San Martin':'210000',
                              'Tacna':'220000',
                              'Tumbes':'230000',
                              'Ucayali':'250000'}
                              """

    def seed_tree(self):
        for departamento in self.departamentos:
        #Save into models
            depar = m.UbiGeo.objects.get_or_create(nombre=departamento, tipo='departamento', post_code=self.departamentos[departamento])

    def make_tree(self):
        for departamento in m.UbiGeo.objects.filter(tipo='departamento'):
            req = Request( self.url + 'extras/provincias.php',
                           urlencode( {'elegido': departamento.post_code } ))
            f = urlopen( req )
            soup = BeautifulSoup( f.read(),
                                  convertEntities=BeautifulSoup.HTML_ENTITIES)
            f.close()
            for item in soup.findAll('option'):
                if item.string is not None:
                    #item.string = name ie. u'Amazonas'
                    #item['value'] = post_code ie. 19291
                    (prov,created) = m.UbiGeo.objects.get_or_create(nombre=item.string, tipo='provincia', parent=departamento, post_code=item['value'])

            #Ahora hacer query a los Ubigeo que tengan el departamento de parent
            for provincia in m.UbiGeo.objects.filter( parent=departamento ):
                req = Request( self.url + 'extras/distritos.php',
                               urlencode( {'elegido': provincia.post_code }))
                f = urlopen( req )
                soup = BeautifulSoup( f.read(),
                                      convertEntities=BeautifulSoup.HTML_ENTITIES)
                f.close()
                for item in soup.findAll('option'):
                    if item.string is not None:
                        (dist,created) = m.UbiGeo.objects.get_or_create(nombre=item.string, tipo='distrito', parent=provincia, post_code=item['value'] )
                        
                for distrito in m.UbiGeo.objects.filter( parent=provincia ):
                    req = Request( self.url + 'extras/locales.php',
                                   urlencode( {'elegido': distrito.post_code}))
                    f=urlopen(req)
                    soup = BeautifulSoup( f.read(),
                                          convertEntities=BeautifulSoup.HTML_ENTITIES)
                    f.close()
                    for item in soup.findAll('option'):
                        if item.string is not None:
                            (local,created) = m.UbiGeo.objects.get_or_create(nombre=item.string, tipo='local', parent=distrito, post_code=item['value'])

                    for local in m.UbiGeo.objects.filter( parent=distrito ):
                        post_data = dict()
                        post_data['tipo_consulta1'] = 'UBIGEO'
                        post_data['cnume_acta'] = ''
                        post_data['ambito1'] = 'P'
                        post_data['dpto'] = local.parent.parent.parent.post_code
                        post_data['prov'] = local.parent.parent.post_code
                        post_data['dist'] = local.parent.post_code
                        post_data['local'] = local.post_code
                        post_data['estado'] = 'T'
                        post_data['continente'] = ''
                        post_data['pais'] = ''
                        post_data['ciudad'] = ''
                        post_data['embajada'] = ''
                        post_data['estado2'] = 'T'

                        req = Request( self.url + 'extras/buscar_ubigeo_actas.php',
                                       urlencode( post_data ))
                        f = urlopen( req )
                        soup = soup.BeautifulSoup( f.read(),
                                            convertEntities=BeautifulSoup.HTML_ENTITIES)
                        f.close()

                        ### SE GUARDA EL ACTA

                        for tr in soup.findAll('tr'):
                            if tr.findAll('td'):
                                if len( tr.findAll('td')) == 1:
                                    print "No se encontrarcon actas con los siguientes para", post_data
                                    pass
                                else:
                                    acta = m.Info_Electoral( num_mesa=tr.findAll('td')[1].string,
                                                      estado=tr.findAll('td')[3].string,
                                                      local=local,
                                                      distrito=distrito, 
                                                      provincia=provincia,
                                                      departamento=departamento)
                                    acta.save()
                                    print "Bajando Acta Num: ", tr.findAll('td')[4].find('a')['href']


    def search_tree(departamento=None, provincia=None, distrito=None, local=None, num_mesa=None ):
        pass

    def test(self):

        local = m.UbiGeo.objects.filter( tipo='local' )[0]

        post_data = dict()
        post_data['tipo_consulta1'] = 'UBIGEO'
        post_data['cnume_acta'] = ''
        post_data['ambito1'] = 'P'
        post_data['dpto'] = str(local.parent.parent.parent.post_code)
        post_data['prov'] = str(local.parent.parent.post_code)
        post_data['dist'] = str(local.parent.post_code)
        post_data['local'] = str(local.post_code)
        post_data['estado'] = 'T'
        post_data['continente'] = ''
        post_data['pais'] = ''
        post_data['ciudad'] = ''
        post_data['embajada'] = ''
        post_data['estado2'] = 'T'
        
        print post_data
        print local
        print self.url + 'extras/buscar_ubigeo_actas.php'

        req = Request( self.url + 'extras/buscar_ubigeo_actas.php',
                                       urlencode( post_data ))
        f = urlopen( req )
        soup = BeautifulSoup( f.read(),
                            convertEntities=BeautifulSoup.HTML_ENTITIES)

        return (f, soup)

if __name__ == '__main__':
    #Congreso :"http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/"
    #Ejemplo Acta URL: http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/rep_mesas_det_cong.php?cnume_acta=240245
    crawler = ONPEcrawler(url = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/" )
    crawler.seed_tree()
    #crawler.make_tree()
            

