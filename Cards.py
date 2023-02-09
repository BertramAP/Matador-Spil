import random
import pyglet

class Space:
    def __init__(self, card, pos: tuple[int, int], name: str, font_size: int, bgc: tuple[int], batch1: pyglet.graphics.Batch, batch2: pyglet.graphics.Batch) -> None:
        self.card = card
        
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.name: str = name

        self.background = pyglet.shapes.Rectangle(self.x+4,self.y+4,56,56,color=bgc,batch=batch1)

        document = pyglet.text.decode_text(name)
        document.set_style(0,len(document.text), dict(font_size=font_size, font_name="Monospace", bold=True))
        self.label = pyglet.text.layout.TextLayout(document, 56, 56, multiline=True, batch=batch2)
        self.label.x = self.x + 4
        self.label.y = self.y + 4


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
    def __init__(self): #get player
        self.name = "START"
        self.RGB = (255, 0, 0)
        self.price = ""
        #Add 4000kr to players balance

class street:
    def __init__(self, Name, RGB, price, rents):
        self.name = Name
        self.RGB = RGB
        self.owner = -1
        self.intPrice = price
        self.price = str(price) + "kr"
        self.rents = rents
        self.rentIndex = 0
        self.rent = rents[self.rentIndex]
        if (self.intPrice < 2500):
            self.upgradeCost = 1000
        elif (self.intPrice < 4200):
            self.upgradeCost = 2000
        elif (self.intPrice < 5800):
            self.upgradeCost = 3000
        else:
            self.upgradeCost = 4000
        
        def checkAmountOwned(self, streetCards):
            if (self.RGB == (173, 216, 230)) or (self.RGB == (114, 47, 55)):
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
        self.name = "???"
        self.cards = []
        self.price = ""
        self.RGB = (234,169,28)
        for i in range(40): 
            self.cards.append(Mysterycard())
        self.index = 0
    def pullCard(self):
        #Use card event
        self.index+=1

class payTaxSpace:
    def __init__(self, Indkomstskat):
        self.name = "Betal skat"
        self.RGB = (50, 205, 50)
        self.price = ""
        self.Indkomstskat = Indkomstskat

    def payTax(self):
        if self.Indkomstskat:
            text = "Betal din indkomst skat på 10% eller betal 4000kr"
            #Set text, og lad spilleren vælge
        if not self.Indkomstskat:
            text = "Ekstra ordinær statskat, betal 2000kr"    


class shippingPort:
    def __init__(self, Name) -> None:
        self.name = Name          
        self.owner = -1
        self.rent = 500 #500kr pr skibs port ejet
        self.intPrice = 4000
        self.price = "4000kr"
        self.RGB = [0, 0, 200]

    def udpateRent(self, player):
        pass #Check amount of shipping ports players owned, time that with 500 for new rent.



class Corparation:
    def __init__(self, Name):
        self.name = Name          
        self.owner = -1
        self.intPrice = 3000
        self.price = "3000kr"
        self.rent = 100
        self.RGB = (133, 1, 2)
        # skal betale 100 gange det terningen vise
    
    def updateRent(self, player):
        pass #Check if player owns both corparations, if player does set rent to 200

    def calcRent(self, roll):
        return self.rent * roll
        

class prison:
    def __init__(self, visit):
        self.name = "Fængsel"
        self.price = ""
        self.visit = visit
        self.RGB = (47,79,79)

    def putPlayerInPrison(self, Player, visit):
        #Frøs spilleren i 2 ture
        pass

#simpel parkerings plads hvor der sker intet
class parkingSpace:
    def __init__(self):
        self.name = "Gratis parkering"
        self.price = ""
        self.RGB = (255, 255, 255)

class streetCard(street):
    def __init__(self):
        super.__init__()
        self.eventType

def get_coord(i: int):
    if i < 11:
        return (0, 64*i)
    if i < 20:
        i -= 10
        return (i*64, 640)
    if i < 30:
        i -= 20
        return (640, 640 - i*64)
    i -= 30
    return (640 - i*64, 0)

def generate_spaces(bot_batch, top_batch):
    chance = Chance()
    parkingplace = parkingSpace()
    SPACES = [start(), street('Rødovre\nvej',  [173, 216, 230], 1200, [50, 250, 750, 2250, 4000, 6000]), Chance(), street('Hvidovre\nvej', [173, 216, 230], 1200, [50, 250, 750, 2250, 4000, 6000]), 
              payTaxSpace(True), shippingPort('Scandlines, Helsingør-Helsingborg'),street('Roskilde\nvej', [255, 100, 127], 2000, [100, 600, 1800, 5400, 8000, 11000]),
              Chance(),street('Valby langgade', [255, 100, 127], 2000, [100, 600, 1800, 5400, 8000, 11000]), street('Allegade', [255, 100, 127], 2400, [150, 800, 2000, 6000, 9000, 12000]),
              prison(True), street('Frederiks\nberg Alle', [79, 121, 66], 2800, [200, 1000, 3000, 9000, 12500, 15000]), Corparation('Tuborg'), street('Bulows\nvej', [79, 121, 66], 2800, [200, 1000, 3000, 9000, 12500, 15000]),
              street('G.L. Kongevej', [79, 121, 66], 3200, [250, 1250, 3750, 10000, 14000, 18000]), shippingPort('Mols-\nLinien'),street('Bernstoff\nssvej', [128, 128, 128], 3600, [300, 1400, 4000, 11000, 15000, 19000]),
              Chance(), street('Hellerup\nvej', [128, 128, 128], 3600, [300, 1400, 4000, 11000, 15000, 19000]), street('Strand\nvejen', [128, 128, 128], 4000, [350, 1600, 4400, 12000, 16000, 20000]),
              parkingSpace(), street('Trianglen', [255, 51, 51], 4400, [350, 1800, 5000, 14000, 17500, 21000]), Chance(), street('Østerbro\ngade', [255, 51, 51], 4400, [350, 1800, 5000, 14000, 17500, 21000]),
              street('Grønning\nen', [255, 51, 51], 4800, [400, 2000, 6000, 15000, 18500, 22000]), shippingPort('Scandlines Gedse-Rostock'), street('Bredgade', [255, 255, 255], 5200, [450, 2200, 6600, 16000, 19500, 23000]),
              street('Kgs. Nytorv', [255, 255, 255], 5200, [450, 2200, 6600, 16000, 19500, 23000]),Corparation('Coca-\nCola'),street('Øster\ngade', [255, 255, 255], 5600, [500, 2400, 7200, 17000, 20500, 24000]),
              prison(False), street('Amager\ntorv', [255, 234, 0], 6000, [550, 2600, 7800, 18000, 22000, 25000]), street('Vimmel\nskaftet ', [255, 234, 0], 6000, [550, 2600, 7800, 18000, 22000, 25000]), Chance(),
              street('Nygade', [255, 234, 0], 6400, [600, 3000, 9000, 20000, 24000, 28000]), shippingPort('Scandlines, Rødby-Puttgarden'), Chance(), street('Frederiks\nberggade', [114, 47, 55], 7000, [700, 3500, 10000, 22000, 26000, 30000]),
              payTaxSpace(False), street('Rådhus\npladsen', [114, 47, 55], 8000, [1000, 4000, 12000, 28000, 34000, 40000])]

    lst = [0]*40

    #lst[0] = Space((0,0),"START", 10, (234,169,28), bot_batch, top_batch)

    for i in range(40):
       lst[i] = Space(SPACES[i], get_coord(i), SPACES[i].name, 9, SPACES[i].RGB, bot_batch, top_batch)

    return lst