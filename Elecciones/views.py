# coding=utf8
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from ONPEcrawler import ONPEcrawler
import Elecciones.models as m

def index(request):
    return render(request,'index.html')

def seed(request):
    
    crawler = ONPEcrawler(url = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/" )
    crawler.seed_tree()

    return HttpResponse('Success')

def crawl(request):
    
    crawler = ONPEcrawler(url = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/" )
    crawler.make_tree()

    return HttpResponse('Success')


def test(request):
    crawler = ONPEcrawler(url = "http://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2011/1ravuelta/onpe/congreso/" )
    (f, soup) = crawler.test()
    print soup

    return HttpResponse('Success')

def visualize_tree(request):
    return render(request,'visualize_tree.html',{'locales':m.UbiGeo.objects.filter(tipo='local'),
                                                 'departamentos':m.UbiGeo.objects.filter(tipo='departamento')})

def clean_db(request):

    for item in m.UbiGeo.objects.all():
        item.delete()

    return HttpResponse('Success')
