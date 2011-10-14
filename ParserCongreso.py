from BeautifulSoup import BeautifulSoup
import re

exp1 = re.compile(r"<td class=\"borde_celda\" align=\"left\"><span class=\"arial_contenido\">(.*)</span></td>")
exp = re.compile(r"<td class=\"borde_celda\" align=\"left\">")

f_acta = open('Ejemplo_Acta_Congreso.html','r')

"""for line in f_acta:
  m = exp1.search(line)
  if m is None:
    pass
  else:
    print m.groups()
"""

soup = BeautifulSoup( f_acta.read() )

#for item in soup.findAll('td',attrs={"align":"left","class":"borde_celda"}):
for item in soup.findAll('td',attrs={"class":"borde_celda"}):
  print item
