#-*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup

with open( 'test_cases/tmp_resultados.html', 'r') as f:
    soup = BeautifulSoup( f.read() )
    for item in soup.findAll('a'):
        print item.attrs[0][1]
        #print item

with open( 'test_cases/tmp_resultados.html', 'r') as f:
    soup = BeautifulSoup( f.read() )
    #print len(soup.findAll('tr'))

    #el número de tr que tengan elementos td (para exceptuar el tr)
    print len( [ i for i in soup.findAll('tr') if (len(i.findAll('td') ) > 0 )] )
    for tr in soup.findAll('tr'):
        if tr.findAll('td'):
            print 'numero de mesa : ', tr.findAll('td')[1].string
            print 'estado del acta : ', tr.findAll('td')[3].string
            #print 'url : ', tr.findAll('td')[4].find('a').attrs[0][1]
            print 'url : ', tr.findAll('td')[4].find('a')['href']

    
