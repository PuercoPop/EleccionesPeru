# -*- coding: utf-8 -*-

from urllib import urlencode
from  urllib2 import Request, urlopen
from BeautifulSoup import BeautifulSoup
import pickle
import json

class ONPEcrawler():
    def __init__(self, url):
        #http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/rep_acta_cong.php
        self.url = url
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

    def fetch_tree(self):
        tree = {'name':'Peru', 'type':'Nacional', 'post_code':None, 'child':[]}
        for departamento in self.departamentos:
            tree['child'].append( { 'name':departamento ,
                                    'type': 'Departamento',
                                    'post_code':self.departamentos[departamento],
                                    'child':[] } ) 

        for departamento in tree['child']:
            req = Request( self.url + 'extras/provincias.php',
                           urlencode( {'elegido':departamento['post_code'] } ))
            f = urlopen( req )
            soup = BeautifulSoup( f.read() )
            f.close()
            for item in soup.findAll('option'):
                if item.string is not None:
                    #item.string = name ie. u'Amazonas'
                    #item['value'] = post_code ie. 19291
                    departamento['child'].append( { 'name': item.string,
                                                    'type':'Provincia',
                                                    'post_code': item['value'],
                                                    'child':[] })

            for provincia in departamento['child']:
                req = Request( self.url + 'extras/distritos.php',
                               urlencode({ 'elegido':provincia['post_code'] }) )
                f = urlopen( req )
                soup = BeautifulSoup( f.read() )
                f.close()
                for item in soup.findAll('option'):
                    if item.string is not None:
                        provincia['child'].append({ 'name':item.string,
                                                    'type':'Distrito',
                                                    'post_code': item['value'],
                                                    'child':[] })
                for distrito in provincia['child']:
                    req = Request( self.url + 'extras/locales.php',
                                   urlencode({ 'elegido':distrito['post_code'] }) )
                    f = urlopen( req )
                    soup = BeautifulSoup( f.read() )
                    f.close()
                    for item in soup.findAll('option'):
                        if item.string is not None:
                            distrito['child'].append({ 'name':item.string,
                                                       'type':'local',
                                                       'post_code':item['value'],
                                                       'child':[] })
                    for local in distrito['child']:
                        post_data= {}
                        post_data['tipo_consulta1'] = 'UBIGEO'
                        post_data['cnume_acta'] = ''
                        post_data['ambito1'] = 'P'
                        post_data['dpto'] = departamento['name']
                        post_data['prov'] = provincia['name']
                        post_data['dist'] = distrito['name']
                        post_data['local'] = local['name']
                        post_data['estado'] = 'T'
                        post_data['continente'] = ''
                        post_data['pais'] = ''
                        post_data['ciudad'] = ''
                        post_data['embajada'] = ''
                        post_data['estado2'] = 'T'
                        
                        req = Request( self.url + 'extras/buscar_ubigeo_actas.php',
                                       urlencode(post_data) )
                        f = urlopen( req )
                        soup = BeautifulSoup( f.read() )
                        f.close()
                        local['numero_de_mesas'] = len( [ i for i in soup.findAll('tr') if (len(i.findAll('td') ) > 0 )] )
                        
                        for tr in soup.findAll('tr'):
                            if tr.findAll('td'):
                                if len( tr.findAll('td')) == 1:
                                    #No se encontraron actas para este local
                                    pass
                                else:
                                    local['child'].append({ 'num_mesa': tr.findAll('td')[1].string,
                                                            'estado' : tr.findAll('td')[3].string ,
                                                            'url': tr.findAll('td')[4].find('a')['href'] })
                    
        return tree
    def save_tree(self, tree, path ):
        with open( path, 'w') as f:
             pickle.dump( tree, f )
    def load_tree(self, path ):
        with open(path, 'r') as f:
            tree = pickle.load( f )
        return tree

    def recur_helper(self, tree, f_html):
        f_html.write('<table>')
        for leaf in tree:
            f_html.write('<tr>')
            if leaf == 'child':
                f_html.write('<td>')
                for node in tree['child']:
                    self.recur_helper( node, f_html )
                f_html.write('</td>')
            else:
                f_html.write("<th>%s</th>" % (leaf,))
                f_html.write("<td>%s</th>" % (tree[leaf],) ) 
                
            f_html.write('</tr>')
        f_html.write('</table>')

    def tree_2_html(self, tree , f_html):
        #header
        f_html.write('<!DOCTYPE html>\n<head><meta encoding="utf-8">')
        f_html.write('<link rel="stylesheet" type="text/css" href="table.css"></head>' )
        f_html.write('<body>')
        #do_stuff
        """
        f_html.write('<table>')
        for leaf in tree:
            f_html.write('<tr>')
            if leaf == 'child':
                f_html.write('pass')
            else:
                f_html.write("<th>%s</th>" % (leaf,))
                f_html.write("<td>%s</th>" % (tree[leaf],) ) 
            f_html.write('</tr>')
        f_html.write('</table>')
        """
        self.recur_helper( tree, f_html )
        #tail
        f_html.write('</body>')



if __name__ == '__main__':
    #Congreso :"http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/"
    #Ejemplo Acta URL: http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/rep_mesas_det_cong.php?cnume_acta=240245
    crawler = ONPEcrawler(url = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/" )
    #tree = crawler.fetch_tree()
    #crawler.save_tree( tree, 'tree.dump' )
    tree = crawler.load_tree( 'tree.dump')
    with open('tree.html','w') as f:
        crawler.tree_2_html(tree , f)
        

