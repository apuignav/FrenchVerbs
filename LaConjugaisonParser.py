#!/usr/bin/env python
# @file   LaConjugaisonParser.py
# @author Albert Puig (albert.puig@epfl.ch)
# @date   27.11.2012

from BeautifulSoup import BeautifulSoup
import urllib
import re
import unicodedata

tempsFinder = re.compile("verbe width[0-9][0-9]")
tagFinder = re.compile(r'<.*?>')
baseUrl = 'http://www.la-conjugaison.fr/imprimer/conjugaison.php?verbe=%s&f=&vp='

def eliminaTildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def loadWeb(myUrl):
 req = urllib.urlopen(myUrl)
 content = req.read()
 encoding=req.headers['content-type'].split('charset=')[-1]
 return unicode(content, encoding)

def parseVerb(text):
  tree = {}
  soup = BeautifulSoup(text)
  groups = soup.findAll('table' ,{'cellspacing':"0",'cellpadding':"0",'class':"tab_groupe"})
  for group in groups:
    groupTitle = unicode(group.find('div', {'class':"groupe center"}).renderContents(), 'utf-8')
    if not groupTitle in tree:
      tree[groupTitle] = {}
    for temps in group.findAll("td", {'class':tempsFinder}):
      tempsTitle = unicode(temps.find('div',{'class':'temps'}).renderContents(), 'utf-8')
      if not tempsTitle in tree[groupTitle]:
        tree[groupTitle][tempsTitle] = []
      for conj in temps.findAll('tr', {'class':"conj"}):
        tree[groupTitle][tempsTitle].append(tagFinder.sub('', conj.renderContents().replace('&nbsp;','').strip(' ')))
  return tree

def getConjugation(verb):
    return parseVerb(loadWeb(baseUrl % str(eliminaTildes(verb))))

# EOF

