import random

community_chest = ["Kør hen til Start", "Du får 200kr fra aktie salg", "Du arver 500", "Du skal betale din søns hospital regning på 700kr"
                   "Tag 300kr for hver spiller", "Du har betalt for meget i skat, du modtager 150kr fra skatteministeriet", "modtag 200 kr for dine service",
                   "Du er kommet til skade, derfor skal du betale lægen 100kr", "Gå i dirkete i fængsel (spring start feldtet over)", "Bank fejl i din fordel, indsaml 1500kr", 
                   "Din juleopsparelse stiger i værdi, indsaml 400kr", "Din livsforsikring stiger, indsaml 300kr", "Fængels frikort", "Betal skole skat på 800kr"
                   "Du er kommet på en anden plads i en skønhedskonkurrence, indsaml 150kr", "Du skal betale for vejarbejde på din grunde, 150kr pr hus, 700kr pr hotel"]
chance = ["Du er blevet valgt som formand for bordet, betal hver spiller 200kr", "Din bolig værdi stiger, indsaml 900kr", "Fængsels frikort", 
          "Banken udbetaler dig et udbytte på 400kr", "Betal din resterende top skat på 300kr", "Rejs til en vilkårlig skibshavn, og indsaml 200kr hvis du passerer start"
          "Rejs til start brikken (indsaml 200kr)", "Rejs til Frederiksberg Alle (indsaml 200kr hvis du passerer start)", "Gå tre fælter tilbage", 
          "Rejs til Rådhuspladsen", "Rejs til nærmeste skibshavn. Hvis havnen er ejet, så skal du betale ejeren dobbelt", 
          "Rejs til det nermæste virksomhed, hvis virksomheden allerede er ejet, så slå terningen og betal ejeren 80 gange det der blev slået", "Rejs til Grønningen",
          "Gå i dirkete i fængsel (spring start feldtet over)", "Din ejendomme skal reperares. For hvert hus du ejer betal 150kr, og for hvert hotel du ejer betal 600kr"]

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

class street:
    def __init__(Name, RGB):
        self.name = Name
        self.RGB = RGB
        self.owned = False
        self.price
        self.rent
        self.opgraderingsKost    

class Chance:
    def __init__():
        for i in range(40): 
            self.cards[i] = Mysterycard()
        self.index = 0
    def pullCard(self):
        #Use card event
        self.index+=1

def payTax():
    text = "Betal din indkomst skat på 10% eller betal 200kr"
    #Set text, og lad spilleren vælge

class shippingPort:
    def __init__(self, Name) -> None:
        self.name = Name          
        self.owned = False
        self.rent
        self.price = 400

class Corparation:
    def __init__(Name):
        self.name = Name          
        self.owned = False
        self.rent
        self.price

class prison:
    def __init__(self) -> None:
        pass

    def putPlayerInPrison(self, Player):
        #Frøs spilleren i 2 ture
chance = Chance()
fængsel = prison()
Spaces = [[street("RødovreVej", [0, 0, 255]), street("Hvidovre"), [0, 0, 255]], [chance], [payTax()], [shippingPort("Øresund A/S")], 
          [street("Roskildevej", [255, 100, 127]), street("Valby langgade", [255, 100, 127]), street("Allegade", [255, 100, 127])], [chance], [fængsel], 
          [street("Frederiksberg Alle", [0, 255, 0]), street("Bulowsvej", [0, 255, 0]), street("G.L. Kongevej", [0, 255, 0])], [Corparation("Tuborg")], [shippingPort("D.F.D.S")],
          [street("Bernstorttsvej", [128, 128, 128]), street("Hellerupvej", [128, 128, 128]), street("Strandvejen", [128, 128, 128])] [Corparation("Helle")],
          [street("Trianglen", [255, 51, 51]), street("Østerbrogade", [255, 51, 51]), street("Grønningen", [255, 51, 51])], [chance], [shippingPort("SFL")]]


class streetCard(street):
    def __init__(self):
        super.__init__()
        self.eventType