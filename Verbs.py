#!/usr/bin/env python
# vim: set fileencoding=utf-8
# @file   Verbs.py
# @author Albert Puig (albert.puig@epfl.ch)
# @date   27.11.2012

verbList = list(set([ u'avoir',
                      u'faire',
                      u'épeler',
                      u'sortir',
                      u'être',
                      u'habiller',
                      u'aller',
                      u'prendre',
                      u'acheter',
                      u'répéter',
                      u'payer',
                      u'appeler',
                      u'envoyer',
                      u'appuyer',
                      u'tutoyer',
                      u'employer',
                      u'compléter',
                      u'espérer',
                      u'lever',
                      u'peser',
                      u'jeter',
                      u'projeter',
                      u'choisir',
                      u'partir',
                      u'lire',
                      u'mettre',
                      u'attendre',
                      u'finir',
                      u'réussir',
                      u'grandir',
                      u'réfléchir',
                      u'accomplir',
                      u'rougir',
                      u'atterrir',
                      u'dormir',
                      u'venir',
                      u'tenir',
                      u'introduire',
                      u'conduire',
                      u'réduire',
                      u'produire',
                      u'instruire',
                      u'vivre',
                      u'répondre',
                      u'descendre',
                      u'perdre',
                      u'connaître',
                      u'paraître',
                      u'prendre',
                      u'venir',
                      u'pouvoir',
                      u'recevoir',
                      u'apprendre',
                      u'comprendre',
                      u'surprendre',
                      u'revenir',
                      u'prévenir',
                      u'obtenir',
                      u'vouloir',
                      u'apercevoir',
                      u'décevoir',
                      u'devoir',
                      u'compléter',
                      u'travailler',
                      u'parler',
                      u'chercher',
                      u'étudier',
                      u'aimer',
                      u'voyager',
                      u'entrer',
                      u'écouter',
                      u'arriver',
                      u'fermer',
                      u'écrire',
                      u'arrêter',
                      u'tomber',
                      u'jouer',
                      u'rêver',
                      u'naître',
                      u'mourir',
                      u'entret',
                      u'sortir',
                      u'arriver',
                      u'partir',
                      u'monter',
                      u'descendre',
                      u'rester',
                      u'tomber',
                      u'passer',
                      u'retourner',
                      u'falloir',
                      u'rencontrer',
                      u'souhaiter',
                      u'croire',
                      u'dire',
                      u'plaindre',
                      u'occuper',
                      u'taiser',
                      u'remplir',
                      u'éteindre',
                      u'allumer',
                      u'déplacer',
                      u'injurier',
                      u'voler',
                      u'ajouter',
                      u'savoir',
                     ]))

def loadVerbs(tree):
    for verb in verbList:
        if not verb in tree:
            from LaConjugaisonParser import getConjugation, eliminaTildes
            print "Téléchargeant %s..." % eliminaTildes(verb).encode('utf-8')
            conj = getConjugation(verb)
            tree[verb] = conj

# EOF
