#!/usr/bin/env python
# -*- coding: utf8 -*-

from random import choice

gracze = ['Asia', 'Pawel', 'Monika', 'Rafal']


red = ['lis', 'kon'] + 2*['swinka'] + 2*['owca'] + 6*['krolik']
green = ['wilk', 'krowka', 'swinka'] + 3*['owca'] + 6*['krolik']
zasoby_gracza = {}


def init():
    global zasoby_gracza
    for g in gracze:
        zasoby_gracza[g] = {
            'krolik': 0,
            'owca':0,
            'swinka':0,
            'krowka':0,
            'kon':0,
            'maly pies':0,
            'duzy pies':0,
        }


def wymiana_zwierzat(zasoby):
    done = True
    while done:
        if zasoby['maly pies'] < 2 or zasoby['duzy pies'] < 2:
            for zwierze, ilosc in zasoby.items():
                if zwierze == 'owca' and ilosc > 1 and zasoby['maly pies'] < 2:
                    zasoby[zwierze] -= 2
                    zasoby['maly pies'] += 1
                elif zwierze == 'krowka' and ilosc > 0:
                    zasoby[zwierze] -= 1
                    zasoby['duzy pies'] += 1
                elif zwierze == 'krolik' and ilosc > 5:
                    zasoby[zwierze] -= 6
                    zasoby['owca'] += 1
                elif zwierze == 'owca' and ilosc > 1:
                    zasoby[zwierze] -= 2
                    zasoby['swinka'] += 1
                elif zwierze == 'swinka' and ilosc > 2:
                    zasoby[zwierze] -= 3
                    zasoby['krowka'] += 1
                elif zwierze == 'krowka' and ilosc > 1:
                    zasoby[zwierze] -= 2
                    zasoby['kon'] += 1
                else:
                    done = False
        else:
            for zwierze, ilosc in zasoby.items():
                if zwierze == 'krolik' and ilosc > 10:
                    zasoby[zwierze] -= 6
                    zasoby['owca'] += 1
                elif zwierze == 'owca' and ilosc > 4:
                    zasoby[zwierze] -= 2
                    zasoby['swinka'] += 1
                elif zwierze == 'swinka' and ilosc > 4:
                    zasoby[zwierze] -= 3
                    zasoby['krowka'] += 1
                elif zwierze == 'krowka' and ilosc > 4:
                    zasoby[zwierze] -= 2
                    zasoby['kon'] += 1
                else:
                    done = False

def tura(wygrany=''):
    for gracz in gracze:
        if not wygrany:
            # Okreslam zasoby aktualnego gracza
            zasoby = zasoby_gracza[gracz]

            # Gracz rzuca koscmi
            rd = choice(red)
            gd = choice(green)
            #print 'Gracz {0} wyrzucil {1} oraz {2}'.format(gracz, rd, gd)

            # Gdy wypadly dwa takie same zwierzeta
            if rd == gd:
                zasoby[rd] += (zasoby[rd]+2) / 2

            else:
                # Gdy wypadł lis
                if rd == 'lis':
                    # Lis pozera tylko malego psa
                    if zasoby['maly pies'] > 0:
                        zasoby['maly pies'] -= 1
                    # Lis pozera wszystkie kroliki
                    else:
                        zasoby['krolik'] = 0
                else:
                    zasoby[rd] += (zasoby[rd]+1) / 2  

                # Gdy wypadł wilk
                if gd == 'wilk':
                    # Wilk pozera tylko duzego psa
                    if zasoby['duzy pies'] > 0:
                        zasoby['duzy pies'] -= 1
                    # Wilk pozera wszystkie zwierzeta poza malym psem i koniem
                    else:
                        for zwierze in zasoby:
                            if zasoby[zwierze] > 0:
                                if zwierze != 'maly pies' and zwierze != 'kon':
                                    zasoby[zwierze] = 0
                else:
                    zasoby[gd] += (zasoby[gd]+1) / 2

            # Wymiana zwierzat
            wymiana_zwierzat(zasoby)

            # Podsumowanie zasobów
            farma = 0
            for zwierze, ilosc in zasoby.items():
                if ilosc > 0:
                    farma += 1
                #print '{0:9} -> {1}'.format(zwierze, ilosc)

            # Warunek koncowy
            if farma > 6:
                return gracz


def rozgrywka():
    counter = 0
    while True:
        #print '\n##### Tura {0} #####'.format(counter)

        wygrany = tura()
        if wygrany:
            #print '\nWygrany ', wygrany
            return wygrany
        counter += 1

wygrane = {}
for gracz in gracze:
    wygrane[gracz] = 0


def statystyka(n):
    for i in range(n):
        init()
        wygrany = rozgrywka()
        wygrane[wygrany] += 1
    print wygrane


if __name__ == "__main__":
    statystyka(10000)



