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

class MysteryHandler(pyglet.event.EventDispatcher):
    def __init__(self):
        self.mystery_pile = [("Kør hen til Start", {"event": "MYSTERY_GO_TO", "tile": 0, "start": True}), ("Du får 2000kr fra aktie salg", {"event": "MYSTERY_GIFT", "amount": 2000}), ("Du arver 6000kr", {"event": "MYSTERY_GIFT", "amount": 6000}), ("Du skal betale din søns hospital regning på 4200kr", {"event": "MYSTERY_BILL", "amount": 4200}), ("Tag 1500kr for hver spiller", {"event": "MYSTERY_STEAL", "amount": 1500}), ("Du har betalt for meget i skat, du modtager 2000kr fra skatteministeriet", {"event": "MYSTERY_GIFT", "amount": 2000}), ("modtag 1000kr for dine services", {"event": "MYSTERY_GIFT", "amount": 1000}), ("Du er kommet til skade, derfor skal du betale lægen 700kr", {"event": "MYSTERY_BILL", "amount": 700}), ("Gå i direkte i fængsel (spring start feldtet over)", {"event": "MYSTERY_GO_TO", "tile": 30, "start": False}), ("Bank fejl i din fordel, indsaml 1500kr", {"event": "MYSTERY_GIFT", "amount": 1500}), ("Din juleopsparelse stiger i værdi, indsaml 2000kr", {"event": "MYSTERY_GIFT", "amount": 2000}), ("Din livsforsikring stiger, indsaml 1200kr", {"event": "MYSTERY_GIFT", "amount": 1200}), ("Fængels frikort", {"event": "MYSTERY_GOOJFC"}), ("Betal skole skat på 2500kr", {"event": "MYSTERY_BILL", "amount": 2500}), ("Du er kommet på en anden plads i en skønhedskonkurrence, indsaml 3500kr", {"event": "MYSTERY_GIFT", "amount": 3500}), ("Du skal betale for vejarbejde på dine grunde, 200kr pr hus, 700kr pr hotel", {"event": "MYSTERY_HH_BILL", "house": 200, "hotel": 700}), ("Du er blevet valgt som formand for bestyrelsen, betal hver spiller 500kr", {"event": "MYSTERY_GIVE", "amount": 500}), ("Din bolig værdi stiger, indsaml 4500kr", {"event": "MYSTERY_GIFT", "amount": 4500}), ("Fængsels frikort", {"event": "MYSTERY_GOOJFC"}), ("Banken udbetaler dig et udbytte på 1800kr", {"event": "MYSTERY_GIFT", "event": 1800}), ("Betal din resterende top skat på 1200kr", {"event": "MYSTERY_BILL", "amount": 1200}), ("Rejs til en vilkårlig skibshavn, og indsaml 4000kr hvis du passerer start", {"event": "MYSTERY_GO_TO_PORT", "which": "random"})("Rejs til start brikken (indsaml 4000kr)", {"event": "MYSTERY_GO_TO", "tile": 0, "start": True}), ("Rejs til Frederiksberg Alle (indsaml 4000kr hvis du passerer start)", {"event": "MYSTERY_GO_TO", "tile": 11, "start": True}), ("Gå tre fælter tilbage", {"event": "MYSTERY_SHIFT", "shift": -3}), ("Rejs til Rådhuspladsen", {"event": "MYSTERY_GO_TO", "tile": 39, "start": True}), ("Rejs til nærmeste skibshavn. Hvis havnen er ejet, så skal du betale ejeren dobbelt", {"event": "MYSTERY_GO_TO_PORT", "which": "closest"}), ("Rejs til det nermæste virksomhed, hvis virksomheden allerede er ejet, så slå terningen og betal ejeren 100 gange det der blev slået", {"event": "MYSTERY_GO_TO_CORPORATION"}), ("Rejs til Grønningen", {"event": "MYSTERY_GO_TO", "tile": 24, "start": True}), ("Gå i direkte i fængsel (spring start feldtet over)", {"event": "MYSTERY_GO_TO", "tile": 30}), ("Dine ejendomme skal reperares. For hvert hus du ejer betal 200kr, og for hvert hotel du ejer betal 800kr", {"event": "MYSTERY_HH_BILL", "house": 200, "hotel": 800})]

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
        self.upgradable = False
        if (self.intPrice < 2500):
            self.upgradeCost = 1000
        elif (self.intPrice < 4200):
            self.upgradeCost = 2000
        elif (self.intPrice < 5800):
            self.upgradeCost = 3000
        else:
            self.upgradeCost = 4000

    def incrementRent(self):
            if not (len(self.rents) < self.rentIndex+1):
                self.rentIndex+=1

    def get_rent(self, _):
        if self.upgradable and self.rentIndex == 0:
            return self.rents[self.rentIndex]*2
        else:
            print(self.name, self.upgradable, self.rentIndex)
            return self.rents[self.rentIndex]

    def drawCard(self, x, y, width, height):
        self.cardlabels = []
        self.cardlabels.append(pyglet.shapes.Rectangle(x, y, width, height, (255, 255, 255)))
        self.cardlabels.append(pyglet.shapes.Rectangle(x, y+9/10*height, width, height/10, self.RGB)) #højden af headeren kan altid ændres
        self.cardlabels.append(pyglet.text.Label(self.name, anchor_x="center", anchor_y="center",font_size=15, color=(0,0,0,255), x=width/2+x, y=y+height*9/10+height/20))
        self.cardlabels.append(pyglet.text.Label(f"Leje af grunde >> {self.rents[0]}kr\n>> med 1 hus >> {self.rents[1]}kr\n>> 2 huse >> {self.rents[2]}kr\n>> 3 huse >> {self.rents[3]}kr\n>> 4 huse >> {self.rents[4]}kr\n>> hotel >> {self.rents[5]}kr", multiline=True, width=width, height=height, anchor_x="left", anchor_y="top",font_size=10, color=(0,0,0,255), x=x, y=9/10*height+y))
        self.cardlabels.append(pyglet.text.Label(f"Hvert hus koster {self.upgradeCost}kr\net hotel koster {self.upgradeCost}kr + 4 huse",anchor_x="left", anchor_y="top",multiline=True, width=width, height=height,font_size=10, color=(0,0,0,255), x=x, y=y+(height)*1.5/3))
        self.cardlabels.append(pyglet.text.Label(f"{self.name} koster \n{self.price} at købe", anchor_x="left", anchor_y="bottom", font_size=10, color=(0,0,0,255), x=x, y=y, width=width, height=height/3,multiline=True))
        return self.cardlabels

class Chance:
    def __init__(self):
        self.name = "???"
        self.price = ""
        self.RGB = (234,169,28)

class payTaxSpace:
    def __init__(self, Indkomstskat):
        self.name = "Betal skat"
        self.RGB = (50, 205, 50)
        self.price = ""
        self.Indkomstskat = Indkomstskat

    def payTax(self, money):
        if self.Indkomstskat:
            if money >= 40_000: payment = 4_000
            else: payment = 0.1*money
            text = f"Betal din indkomst skat på {payment}kr"
        if not self.Indkomstskat:
            text = "Ekstra ordinær statskat, betal 2000kr"
            payment = 2_000
        return (int(payment), text)


class shippingPort:
    def __init__(self, Name) -> None:
        self.name = Name          
        self.owner = -1
        self.owned = 1 #500kr pr skibs port ejet
        self.rents = [500,1000,2000,4000]
        self.rent = self.rents[0]
        self.intPrice = 4000
        self.price = "4000kr"
        self.RGB = [0, 0, 200]

    def get_rent(self, _):
        self.rent = self.rents[self.owned-1]
        return self.rent

    def drawCard(self, x, y, width, height):
        self.cardlabels = []
        self.cardlabels.append(pyglet.shapes.Rectangle(x, y, width, height, (255, 255, 255)))
        self.cardlabels.append(pyglet.shapes.Rectangle(x, y+height*9/10, width, height/10, self.RGB)) #højden af headeren kan altid ændres
        self.cardlabels.append(pyglet.text.Label(self.name, anchor_x="center", anchor_y="center",font_size=15, x=width/2+x, y=y+height*9.5/10))
        self.cardlabels.append(pyglet.text.Label(f"Leje >> {self.rent}kr\nHvis 2 skipsporte ejes >> {self.rent*2}kr\nHvis 3 skipsporte ejes >> {self.rent*4}kr\nHvis 4 skipsporte ejes >> {self.rent*8}kr", multiline=True, width=width, height=height, anchor_x="left", anchor_y="top",font_size=10, color=(0,0,0,255), x=x, y=9/10*height+y))
        self.cardlabels.append(pyglet.text.Label(f"{self.name} koster \n{self.price} at købe", anchor_x="left", anchor_y="bottom", font_size=10, color=(0,0,0,255), x=x, y=y, width=width, height=height/3,multiline=True))
        return self.cardlabels

class Corparation:
    def __init__(self, Name):
        self.name = Name          
        self.owner = -1
        self.owned = 1
        self.intPrice = 3000
        self.price = "3000kr"
        self.rent = 100
        self.RGB = (133, 1, 2)
        # skal betale 100 gange det terningen vise
    
    def get_rent(self, roll):
        return self.rent * roll * self.owned
    
    def drawCard(self, x, y, width, height):
        self.cardlabels = []
        self.cardlabels.append(pyglet.shapes.Rectangle(x, y, width, height, (255, 255, 255)))
        self.cardlabels.append(pyglet.shapes.Rectangle(x, y+height*9/10, width, height/10, self.RGB)) #højden af headeren kan altid ændres
        self.cardlabels.append(pyglet.text.Label(self.name, anchor_x="center", anchor_y="center",font_size=15, x=width/2+x, y=y+height*9.5/10))
        self.cardlabels.append(pyglet.text.Label(f"Hvis en virksomhed ejes, skal der betales {self.rent} gange så meget som øjnene viser\nHvis både Coca-Cola og Tuborg ejes, betales {self.rent*2} gange så meget som øjnene viser.", anchor_x="left", anchor_y="top",font_size=10, color=(0,0,0,255), multiline=True, width=width, height=height, x=x, y=9/10*height+y))
        self.cardlabels.append(pyglet.text.Label(f"{self.name} koster \n{self.price} at købe", anchor_x="left", anchor_y="bottom", font_size=10, color=(0,0,0,255), x=x, y=y, width=width, height=height/3,multiline=True))
        return self.cardlabels
        

class prison:
    def __init__(self, visit):
        self.name = "Fængsel"
        self.idle_text = "Du er på besøg i fængsel"
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
        self.idle_text = "Her er gratis parkering"
        self.price = ""
        self.RGB = (255, 255, 255)

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