from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        self.tuote = Tuote
        self.ostos = Ostos
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaramaara = 0
        for ostos in self.ostoskori:
            tavaramaara += ostos.lukumaara()
        return tavaramaara
        #self.tavaroita_korissa = len(self.ostoskori)
        #return self.tavaroita_korissa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        ostoskorin_hinta = 0
        for self.ostos in self.ostoskori:      
            ostoskorin_hinta += self.ostos.hinta()
        return ostoskorin_hinta
        #for self.ostos in self.ostoskori:      
        #    ostoskorin_hinta += self.ostos.hinta()
        #return ostoskorin_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if len(self.ostoskori) > 0:
            for ostos in self.ostoskori:
                if ostos.tuotteen_nimi() == lisattava.nimi():
                    ostos.muuta_lukumaaraa(1)
                    return
            lisattava_ostosolio = self.ostos(lisattava)
            self.ostoskori.append(lisattava_ostosolio)
        else:
            lisattava_ostosolio = self.ostos(lisattava)
            self.ostoskori.append(lisattava_ostosolio)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
