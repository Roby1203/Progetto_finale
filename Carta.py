import random

class Carta:
    ListaSemi = ["Fiori", "Quadri", "Cuori", "Picche"]
    ListaRanghi = ["impossibile", "Asso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Regina", "Re"]

    def __init__(self, Seme=0, Rango=0):
        self.Seme = Seme
        self.Rango = Rango

    def __str__(self):
        return (self.ListaRanghi[self.Rango] + " " + "di" + " " + self.ListaSemi[self.Seme])
        
    def __cmp__(self, Altro):
#controlla il seme
        if self.Seme != Altro.Seme:
            return -1
        #if self.Seme < Altro.Seme: return -1
        else:
#se i semi sono uguali controlla il rango
            if self.Rango != Altro.Rango:
                return -1
            else:
                return 0
        #if self.Rango < Altro.Rango: return -1
#se anche i ranghi sono uguali le carte sono uguali
    
class Mazzo:
    def __init__ (self):
        self.Carte = []
        for Seme in range(4):
            for Rango in range(1, 14):
                self.Carte.append(Carta(Seme, Rango))
    def __str__(self):
        s = ""
        for i in range(len(self.Carte)):
            s = s + " "*i + str(self.Carte[i]) + "\n"

        return s
                 
    def Mescola(self):
        NumCarte = len(self.Carte)
        for i in range(NumCarte):
            j = random.randrange (i, NumCarte)

            self.Carte[i], self.Carte[j] = self.Carte[j], self.Carte[i]

    def RimuoviCarta(self, Carta):
        if Carta in self.Carte:
            self.Carte.remove(Carta)
            return 1
        else:
            return 0
    def PrimaCarta (self):
        return self.Carte.pop()
    def EVuoto (self):
        return (len(self.Carte) == 0)
    def Distribuisci(self, ListaMani, NumCarte):
        NumMani = len(ListaMani)                
        for i in range (NumCarte):                 
           if self.EVuoto(): break                 

           Carta = self.PrimaCarta()
                                                   
           Mano = ListaMani [i % NumMani]           
                                                
           Mano.AggiungeCarta(Carta)            
class Mano(Mazzo):
    def __init__(self, Nome=""):
        self.Carte = []
        self.Nome = Nome

    def AggiungeCarta(self, Carta):
        self.Carte.append(Carta)

    def __str__(self):
        s = "La mano di " + self.Nome
        if self.EVuoto():
            s = s + " e' vuota\n"

        else:
            s = s + " contiene queste carte: \n"
        return s + Mazzo.__str__(self)
#Mazzo1 = Mazzo()
#Mazzo1.Mescola()
#Mano1 = Mano("rtrff")
#Mazzo1.Distribuisci([Mano1],5)
#print Mano1
class GiocoDiCarte:
    def __init__(self):
       self.Mazzo = Mazzo()
       self.Mazzo.Mescola()
class ManoOldMaid(Mano):

    def RimuoveCoppie(self):
        Conteggio = 0
        CarteOriginali = self.Carte[:]
        for CartaOrig in CarteOriginali:
            
            CartaDaCercare = Carta(3-CartaOrig.Seme, CartaOrig.Rango)
            
            
            if CartaDaCercare in self.Carte:
            
                self.Carte.remove(CartaOrig)
                self.Carte.remove(CartaDaCercare)

                print "Mano di %s : %s elimina %s" % (self.Nome, CartaOrig, CartaDaCercare)
                Conteggio = Conteggio + 1
                return Conteggio
#Partita = GiocoDiCarte()
#Mano1 = ManoOldMaid("Franco")
#Partita.Mazzo.Distribuisci([Mano1],13)
#print Mano1
#Mano1.RimuoveCoppie()
#print Mano1


#Mano2 = ManoOldMaid("Fabio")
#Partita.Mazzo.Distribuisci([Mano2],13)
#print Mano2
#Mano2.RimuoveCoppie()
#print Mano2


#Mano3 = ManoOldMaid("Mario")
#Partita.Mazzo.Distribuisci([Mano3],13)
#print Mano3
#Mano3.RimuoveCoppie()
#print Mano3

#Mano4 = ManoOldMaid("Giando")
#Partita.Mazzo.Distribuisci([Mano4],13)
#print Mano4
#Mano4.RimuoveCoppie()
#print Mano4







class GiocoOldMaid(GiocoDiCarte):
   def Partita(self, Nomi):
       self.Mazzo.RimuoviCarta(Carta(0,12))
       
       self.Mani = []
       for Nome in Nomi:
           self.Mani.append(ManoOldMaid(Nome))
           self.Mazzo.Distribuisci(self.Mani)
           print "LE CARTE SONO STATE DISTRIBUITE"
           self.StampaMani()
           NumCoppie = self.RimuoveTutteLeCoppie()
           print"COPPIE SCARTATE, INIZIA LA PARTITA"
           self.StampaMani()
           Turno = 0
           NumMani = len(self.Mani)
           while NumCoppie < 25:
               NumCoppie = NumCoppie + self.GiocaUnTurno(Turno)
               Turno = (Turno + 1) % NumMani
               print "LA PARTITA E' FINITA"
               self.StampaMani()
               def RimuoveTutteLeCoppie(self):
                   Conteggio = 0
                   for Mano in self.Mani:
                       Conteggio = Conteggio + Mano.RimuoveCoppie()
                       return Conteggio
                   def GiocaUnTurno(self, Giocatore):
                       if self.Mani[Giocatore].EVuoto():
                           return 0
                       Vicino = self.TrovaVicino(Giocatore)
                       CartaScelta = self.Mani[Vicino].PrimaCarta()
                       self.Mani[Giocatore].AggiungeCarta(CartaScelta)
                       print "Mano di", self.Mani[Giocatore].Nome,": scelta", CartaScelta
                       Conteggio = self.Mani[Giocatore].RimuoveCoppie()
                       self.Mani[Giocatore].MischiaMazzo()
                       return Conteggio
                   def TrovaVicino(self, Giocatore):
                       NumMani = len(self.Mani)
                       for Prossimo in range (1,NumMani):
                           Vicino = (Giocatore + Prossimo) % NumMani
                           if not self.Mani[Vicino].EVuoto():
                               return Vicino
                           self.StampaMani()


Partita = GiocoDiCarte()
Mano1 = ManoOldMaid("Franco")
Partita.Mazzo.Distribuisci([Mano1],13)
print Mano1
Mano1.RimuoveCoppie()
print Mano1


Mano2 = ManoOldMaid("Fabio")
Partita.Mazzo.Distribuisci([Mano2],13)
print Mano2
Mano2.RimuoveCoppie()
print Mano2


Mano3 = ManoOldMaid("Mario")
Partita.Mazzo.Distribuisci([Mano3],13)
print Mano3
Mano3.RimuoveCoppie()
print Mano3

Mano4 = ManoOldMaid("Giando")
Partita.Mazzo.Distribuisci([Mano4],13)
print Mano4
Mano4.RimuoveCoppie()
print Mano4





 



