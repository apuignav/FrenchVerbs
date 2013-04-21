#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8

import random

import PickleFile
from Verbs import loadVerbs

baseFile = 'verbs.fr'
personneList = ['je', 'tu', 'il', 'nous', 'vous', 'ils']

mode = [ (u'Indicatif', u'Présent'),
         (u'Indicatif', u'Imparfait'),
         (u'Indicatif', u'Passé composé'),
         (u'Indicatif', u'Futur simple'),
         (u'Conditionnel', u'Présent'),
        ]

if __name__ == '__main__':
  fullTree = PickleFile.load(baseFile)
  if not fullTree:
    fullTree = {}
  loadVerbs(fullTree)
  PickleFile.write(baseFile, fullTree)
  print "=" * 80
  print "Bienvenue au test de Français".center(80)
  #print
  #print (u"Tu étudies %s" % ((u' et ' .join(temps)))).encode("utf-8").center(80)
  #print "du".center(80)
  #print (u"%s" % ((u' et '.join(group)))).encode("utf-8").center(80)
  print "=" * 80
  ntot = 0
  nb = 0
  try:
    while True:
      personneNum = int(random.uniform(0,len(personneList)))
      verbNum = int(random.uniform(0,len(fullTree.keys())))
      gr, tmps = mode[int(random.uniform(0,len(mode)))]
      verb = fullTree.keys()[verbNum]
      try:
        if not fullTree[verb][gr].get(tmps, None):
          continue
      except:
        continue
      tempPrint = "[%s - %s]" % (gr, tmps)
      if gr == u'Conditionnel':
      	tempPrint = "[%s]" % (gr)
      answ = raw_input("%s: " % (u"%40s %s (%s)" % (tempPrint, personneList[personneNum], verb)).encode("utf-8"))
      if not answ:
        raise KeyboardInterrupt()
      if fullTree[verb][gr][tmps][personneNum] == answ:
        print " Très bien!"
        nb = nb+1
      else:
        print (u" Faux! %s" % unicode(fullTree[verb][gr][tmps][personneNum],'utf-8')).encode("utf-8")
      ntot = ntot+1
  except KeyboardInterrupt:
    print
    print "=" * 80
    print ("C'est fini! Ton résultat est %s/%s (%.2f)." % (nb, ntot, 10.0*nb/ntot if ntot else 0)).center(80)
    print "=" * 80

# EOF

