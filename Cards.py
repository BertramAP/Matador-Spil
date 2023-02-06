import random

community_chest = ["Kør hen til Start", "Du får 2000kr fra aktie salg", "Du arver 6000kr", "Du skal betale din søns hospital regning på 4200kr"
                   "Tag 1500kr for hver spiller", "Du har betalt for meget i skat, du modtager 2000kr fra skatteministeriet", "modtag 1000kr for dine service",
                   "Du er kommet til skade, derfor skal du betale lægen 700kr", "Gå i dirkete i fængsel (spring start feldtet over)", "Bank fejl i din fordel, indsaml 1500kr",
                   "Din juleopsparelse stiger i værdi, indsaml 2000kr", "Din livsforsikring stiger, indsaml 1200kr", "Fængels frikort", "Betal skole skat på 2500kr"
                   "Du er kommet på en anden plads i en skønhedskonkurrence, indsaml 3500kr", "Du skal betale for vejarbejde på din grunde, 200kr pr hus, 700kr pr hotel"]
chance = ["Du er blevet valgt som formand for bordet, betal hver spiller 500kr", "Din bolig værdi stiger, indsaml 4500kr", "Fængsels frikort",
          "Banken udbetaler dig et udbytte på 1800kr", "Betal din resterende top skat på 1200kr", "Rejs til en vilkårlig skibshavn, og indsaml 4000kr hvis du passerer start"
          "Rejs til start brikken (indsaml 4000kr)", "Rejs til Frederiksberg Alle (indsaml 4000kr hvis du passerer start)", "Gå tre fælter tilbage",
          "Rejs til Rådhuspladsen", "Rejs til nærmeste skibshavn. Hvis havnen er ejet, så skal du betale ejeren dobbelt", 
          "Rejs til det nermæste virksomhed, hvis virksomheden allerede er ejet, så slå terningen og betal ejeren 100 gange det der blev slået", "Rejs til Grønningen",
          "Gå i dirkete i fængsel (spring start feldtet over)", "Din ejendomme skal reperares. For hvert hus du ejer betal 200kr, og for hvert hotel du ejer betal 800kr"]

class Mysterycard:
    def __init__(self) -> None:
        self.cardType = random.randint(0, 1)
        if self.cardType == 0:
            self.card = random.randint(0, len(community_chest))
            self.cardText = community_chest[self.card]
        else:
            self.card = random.randint(0, len(community_chest))
            self.cardText = chance[self.card]
    
    def mysteryEvent(self):
        self.card
class start:
    def _innit(self): #get player
        pass #Add 4000kr to players balance
class street:
    def __init__(self, Name, RGB, price):
        self.name = Name
        self.RGB = RGB
        self.owned = False
        self.price = price
        self.rent = self.price/10 #skal ganges med 2 hvis alle i gader i samme gruppe ejes
        if (self.price < 2500):
            self.upgradeCost = 1000

class Chance:
    def __init__(self):
        self.cards = []
        for i in range(40): 
            self.cards.append(Mysterycard())
        self.index = 0
    def pullCard(self):
        #Use card event
        self.index+=1

def payTax(Indkomstskat):
    if Indkomstskat:
        text = "Betal din indkomst skat på 10% eller betal 4000kr"
        #Set text, og lad spilleren vælge
    if not Indkomstskat:
        text = "Ekstra ordinær statskat, betal 2000kr"
class shippingPort:
    def __init__(self, Name) -> None:
        self.name = Name          
        self.owned = False
        self.rent = 500 #500kr pr skibs port ejet
        self.price = 4000

class Corparation:
    def __init__(self, Name):
        self.name = Name          
        self.owned = False
        self.price = 3000
        # skal betale 100 gange det terningen vise

class prison:
    def __init__(self, visit):
        self.visit = visit

    def putPlayerInPrison(self, Player, visit):
        #Frøs spilleren i 2 ture
class parkingSpcae:
    def __init__(self):
        pass #simpel parkerings plads hvor der sker intet


chance = Chance()

parkingplace = parkingSpcae()
Spaces = [[start()], [street("Rødovrevej", [0, 0, 255], 1200), street("Hvidovrevej", [0, 0, 255], 1200)], [chance], [payTax(True)], [shippingPort("Scandlines, Helsingør-Helsingborg")],
          [street("Roskildevej", [255, 100, 127], 2000), street("Valby langgade", [255, 100, 127], 2000), street("Allegade", [255, 100, 127], 2400)], [chance], [prison(False)],
          [street("Frederiksberg Alle", [0, 255, 0], 2800), street("Bulowsvej", [0, 255, 0], 2800), street("G.L. Kongevej", [0, 255, 0], 3200)], [Corparation("Tuborg")], [shippingPort("Mols-Linien")],
          [street("Bernstorttsvej", [128, 128, 128], 3600), street("Hellerupvej", [128, 128, 128], 3600), street("Strandvejen", [128, 128, 128], 4000)], [chance], [parkingplace],
          [street("Trianglen", [255, 51, 51], 4400), street("Østerbrogade", [255, 51, 51], 4400), street("Grønningen", [255, 51, 51], 4800)], [chance], [shippingPort("Scandlines Gedse-Rostock")]
          [street("Bredgade", [0, 0, 0], 5200), street("Kgs. Nytorv", [0, 0, 0], 5200), street("Østergade", [0, 0, 0], 5600)], [Corparation("Coca-Cola")], [prison(True)],
          [street("Amagertorv", [255, 234, 0], 6000), street("Vimmelskaftet ", [255, 234, 0], 6000), street("Nygade",[255, 234, 0]), 6400], [chance], [shippingPort("Scandlines, Rødby-Puttgarden")],
          [Chance],[street("Frederiksberggade", [255, 234, 0], 7000), street("Rådhuspladsen", [255, 234, 0], 8000)],[payTax(False)]]

class streetCard(street):
    def __init__(self):
        super.__init__()
        self.eventType