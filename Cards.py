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
            self.card = random.randint(0, len(community_chest)-1)
            self.cardText = community_chest[self.card]
        else:
            self.card = random.randint(0, len(community_chest)-1)
            self.cardText = chance[self.card]
    
    def mysteryEvent(self):
        self.card
class start:
    def _innit(self): #get player
        pass #Add 4000kr to players balance
class street:
    def __init__(self, Name, RGB, price, rents):
        self.name = Name
        self.RGB = RGB
        self.owned = False
        self.price = price
        self.rents = rents
        self.rentIndex = 0
        self.rent = rents[self.rentIndex]
        if (self.price < 2500):
            self.upgradeCost = 1000
        elif (self.price < 4200):
            self.upgradeCost = 2000
        elif (self.price < 5800):
            self.upgradeCost = 3000
        else:
            self.upgradeCost = 4000
        
        def checkAmountOwned(self, streetCards):
            if (self.RGB == [0, 0, 255]) or (self.RGB == [255, 234, 0]):
                for i in range(len(streetCards)):
                    streetCards[i].rent = streetCards[i].rent*2
            elif (len(streetCards) == 3):
                for i in range(len(streetCards)):
                    streetCards[i].rent = streetCards[i].rent*2


        def updateRent(self):
            if not (len(self.rents) < self.rentIndex+1):
                self.rentIndex+=1
                self.rent = rents[self.rentIndex]
            else:
                pass # already max upgraded


class Chance:
    def __init__(self):
        self.cards = []
        for i in range(40): 
            self.cards.append(Mysterycard())
        self.index = 0
    def pullCard(self):
        #Use card event
        self.index+=1

class payTaxSpace:
    def __init__(self, Indkomstskat):
        self.Name = "Betal skat"
        self.Indkomstskat = Indkomstskat

    def payTax(self,):
        if self.Indkomstskat:
            text = "Betal din indkomst skat på 10% eller betal 4000kr"
            #Set text, og lad spilleren vælge
        if not self.Indkomstskat:
            text = "Ekstra ordinær statskat, betal 2000kr"    



class shippingPort:
    def __init__(self, Name) -> None:
        self.name = Name          
        self.owned = False
        self.rent = 500 #500kr pr skibs port ejet
        self.price = 4000

    def udpateRent(self, player):
        pass #Check amount of shipping ports players owned, time that with 500 for new rent.



class Corparation:
    def __init__(self, Name):
        self.name = Name          
        self.owned = False
        self.price = 3000
        self.rent = 100
        # skal betale 100 gange det terningen vise
    
    def updateRent(self, player):
        pass #Check if player owns both corparations, if player does set rent to 200

    def calcRent(self, roll):
        return self.rent * roll
        

class prison:
    def __init__(self, visit):
        self.visit = visit

    def putPlayerInPrison(self, Player, visit):
        #Frøs spilleren i 2 ture
        pass

class parkingSpcae:
    def __init__(self):
        pass #simpel parkerings plads hvor der sker intet


chance = Chance()

parkingplace = parkingSpcae()
Spaces = [[start()], [street("Rødovrevej", [0, 0, 255], 1200, [50, 250, 750, 2250, 4000, 6000]), street("Hvidovrevej", [0, 0, 255], 1200, [50, 250, 750, 2250, 4000, 6000])], [chance], [payTaxSpace(True)], [shippingPort("Scandlines, Helsingør-Helsingborg")],
          [street("Roskildevej", [255, 100, 127], 2000, [100, 600,  1800, 5400, 8000, 11000]), street("Valby langgade", [255, 100, 127], 2000, [100, 600,  1800, 5400, 8000, 11000]), street("Allegade", [255, 100, 127], 2400, [150, 800,  2000, 6000, 9000, 12000])], [chance], [prison(False)],
          [street("Frederiksberg Alle", [0, 255, 0], 2800, [200, 1000, 3000, 9000, 12500, 15000]), street("Bulowsvej", [0, 255, 0], 2800, [200, 1000, 3000, 9000, 12500, 15000]), street("G.L. Kongevej", [0, 255, 0], 3200, [250, 1250, 3750, 10000, 14000, 18000])], [Corparation("Tuborg")], [shippingPort("Mols-Linien")],
          [street("Bernstorttsvej", [128, 128, 128], 3600, [300, 1400, 4000, 11000, 15000, 19000]), street("Hellerupvej", [128, 128, 128], 3600, [300, 1400, 4000, 11000, 15000, 19000]), street("Strandvejen", [128, 128, 128], 4000, [350, 1600, 4400, 12000, 16000, 20000])], [chance], [parkingplace],
          [street("Trianglen", [255, 51, 51], 4400, [350, 1800, 5000, 14000, 17500, 21000]), street("Østerbrogade", [255, 51, 51], 4400, [350, 1800, 5000, 14000, 17500, 21000]), street("Grønningen", [255, 51, 51], 4800, [400, 2000, 6000, 15000, 18500, 22000])], [chance], [shippingPort("Scandlines Gedse-Rostock")]
          [street("Bredgade", [0, 0, 0], 5200, [450, 2200, 6600, 16000, 19500, 23000]), street("Kgs. Nytorv", [0, 0, 0], 5200, [450, 2200, 6600, 16000, 19500, 23000]), street("Østergade", [0, 0, 0], 5600, [500, 2400, 7200, 17000, 20500, 24000])], [Corparation("Coca-Cola")], [prison(True)],
          [street("Amagertorv", [255, 234, 0], 6000, [550, 2600, 7800, 18000, 22000, 25000]), street("Vimmelskaftet ", [255, 234, 0], 6000, [550, 2600, 7800, 18000, 22000, 25000]), street("Nygade",[255, 234, 0], 6400, [600, 3000, 9000, 20000, 24000, 28000])], [chance], [shippingPort("Scandlines, Rødby-Puttgarden")],
          [Chance],[street("Frederiksberggade", [255, 234, 0], 7000, [700, 3500, 10000, 22000, 26000, 30000]), street("Rådhuspladsen", [255, 234, 0], 8000, [1000, 4000, 12000, 28000, 34000, 40000])],[payTaxSpace(False)]]

class streetCard(street):
    def __init__(self):
        super.__init__()
        self.eventType