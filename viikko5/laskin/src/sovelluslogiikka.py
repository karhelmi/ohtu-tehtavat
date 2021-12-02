class Sovelluslogiikka:
    def __init__(self, tulos=0): #, edellinen_arvo=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def save_last_result(self, arvo):
        self.edellinen_arvo = self.tulos - arvo

    def aseta_arvo(self):
        self.tulos = self.edellinen_arvo

class Summa:
    def __init__(self, io, arvo):
        self.io = io
        self._lue_syote = arvo

    def suorita(self):
        self.io.plus(int(self._lue_syote()))
        self.io.save_last_result(int(self._lue_syote()))

class Erotus:
    def __init__(self, io, arvo):
        self.io = io
        self._lue_syote = arvo

    def suorita(self):
        self.io.miinus(int(self._lue_syote()))
        self.io.save_last_result(-int(self._lue_syote()))

class Nollaus:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        self.io.nollaa()

class Kumoa:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        self.io.aseta_arvo()