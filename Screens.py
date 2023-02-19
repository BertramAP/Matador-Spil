import pyglet
from random import randint, sample

class Roller(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("rolled")
        self.register_event_type("handle_prisoner")

        self.tbatch = pyglet.graphics.Batch()
        self.bbatch = pyglet.graphics.Batch()

        self.pressed_button = False
        self.not_rolled = True

        self.button = pyglet.shapes.Rectangle(300, 200, 100, 50, (255,0,0), batch=self.bbatch)
        self.label = pyglet.text.Label("Rul", anchor_x="center",font_size=30, x=350, y= 210, batch=self.tbatch)

        dice_pic = pyglet.image.load("resources/dice2.png")
        self.all_dice = [dice_pic.get_region(i*96,0,96,96) for i in range(6)]
        self.dice = sample(self.all_dice, 2)

        self.clock = pyglet.clock.get_default()

    def initialise(self, kwargs):
        self.clock.schedule_interval(self.dice_changer, 0.1)
        self.not_rolled = True
        self.color = kwargs["color"]
        self.prison_roll = kwargs["prison_roll"]
        self.button.color = self.color
        self.pcolor = (self.color[0]*0.8, self.color[1]*0.8, self.color[2]*0.8)

    def throw_success(self, dt, res) -> None:
        if not self.prison_roll:
            self.dispatch_event("rolled", res[0] + res[1])
        elif res[0] == res[1]:
            self.dispatch_event("handle_prisoner", True, res[0]+res[1])
        else:
            self.dispatch_event("handle_prisoner", False, 0)

    def dice_changer(self, dt):
        self.dice = sample(self.all_dice, 2)

    def draw(self):
        self.bbatch.draw()
        self.tbatch.draw()

        self.dice[0].blit(244, 290, 0)
        self.dice[1].blit(360, 290, 0)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250:
            self.pressed_button = True
            self.button.color = self.pcolor
        else: self.pressed_button = False
        
    def on_mouse_release(self, x, y, button, modifiers):
        self.button.color = self.color
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250 and self.pressed_button and self.not_rolled:
            self.clock.unschedule(self.dice_changer)
            one = randint(1,6)
            two = randint(1,6)
            self.dice = [self.all_dice[one-1], self.all_dice[two-1]]
            self.not_rolled = False
            
            self.clock.schedule_once(self.throw_success, 2, res=(one,two))

class Idle(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("next_player")

        self.tbatch = pyglet.graphics.Batch()
        self.bbatch = pyglet.graphics.Batch()

        self.button = pyglet.shapes.Rectangle(270, 200, 160, 50, (255,0,0), batch=self.bbatch)
        self.text = [pyglet.text.Label("Forstået", anchor_x="center",font_size=30, x=350, y= 210, batch=self.tbatch),
                     pyglet.text.Label("TBA", anchor_x="center",anchor_y="top",font_size=20,x=350,y=500,multiline=True,width=576,height=500,align="center",batch=self.tbatch)
                     ]
        
    def initialise(self, kwargs):
        self.text[1].text = kwargs["text"]

    def draw(self):
        self.button.draw()
        self.text[0].draw()
        self.text[1].draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250:
            self.pressed_button = True
            self.button.color = (200,0,0)
        else: self.pressed_button = False
    
    def on_mouse_release(self, x, y, button, modifiers):
        self.button.color = (255,0,0)
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250 and self.pressed_button:
            self.dispatch_event("next_player")

class BuyProperty(pyglet.event.EventDispatcher):
    def __init__(self) -> None:
        super().__init__()
        self.register_event_type("acquire_property")
        self.register_event_type("auctioned")

        self.question = pyglet.text.Label("Vil du købe følgende\ngrund?", font_size=20, x=500, y=400, color=(0,0,0,255), anchor_x="center", multiline=True, width=300, height=50)

        self.button_pressed = -1
        self.button_1 = pyglet.shapes.Rectangle(400, 300, 75, 40, (0,255,0))
        self.button_2 = pyglet.shapes.Rectangle(480, 300, 75, 40, (255,0,0))

        self.ja_label = pyglet.text.Label("Ja", x=self.button_1.x+self.button_1.height/2, y=self.button_1.y+self.button_1.height/2, anchor_x="center", anchor_y="center", font_size=15, color=(0,0,0,255))
        self.nej_label = pyglet.text.Label("Nej", x=self.button_2.x+self.button_2.height/2, y=self.button_2.y+self.button_2.height/2, anchor_x="center", anchor_y="center", font_size=15, color=(0,0,0,255))

    def initialise(self, kwargs):
        self.data = kwargs
        self.card = kwargs["card"]
        self.card_drawables = self.card.drawCard(100,212,200,280)
        self.player = kwargs["pid"]

    def on_mouse_press(self, x, y, button, modifiers):
        if button != 1: return

        if self.button_1.x <= x <= self.button_1.x+self.button_1.width and self.button_1.y <= y <= self.button_1.y+self.button_1.height:
            self.button_pressed = 1
            self.button_1.color = (0,200,0)
        elif self.button_2.x <= x <= self.button_2.x+self.button_2.width and self.button_2.y <= y <= self.button_2.y+self.button_2.height:
            self.button_pressed = 2
            self.button_2.color = (200,0,0)

    def on_mouse_release(self, x, y, button, modifiers):
        if button != 1: return

        if self.button_pressed == 1 and self.button_1.x <= x <= self.button_1.x+self.button_1.width and self.button_1.y <= y <= self.button_1.y+self.button_1.height and self.data["ledger"][self.data["pid"]] > self.data["card"].intPrice:
            self.dispatch_event("acquire_property", self.data["tile"], self.data["pid"], self.data["card"].intPrice)
        elif self.button_pressed == 2 and self.button_2.x <= x <= self.button_2.x+self.button_2.width and self.button_2.y <= y <= self.button_2.y+self.button_2.height:
            self.dispatch_event("auctioned", self.data)

        self.button_1.color = (0,255,0)
        self.button_2.color = (255,0,0)

    def draw(self):
        self.question.draw()
        
        for obj in self.card_drawables:
            obj.draw()

        self.button_1.draw()
        self.button_2.draw()
        self.ja_label.draw()
        self.nej_label.draw()

class Auction(pyglet.event.EventDispatcher):
    def __init__(self, players) -> None:
        super().__init__()
        self.register_event_type("acquire_property")
    	
        self.participants = players
        self.nplayers = len(players)
        self.active_player = None
        self.highest_bidder = None
        self.highest_bid = 0
        self.ledger = None

        self.folded = []
        self.card = None
        self.startX = 64
        self.startY = 84
        self.dict = {pyglet.window.key._1: 100, pyglet.window.key._2: 500, pyglet.window.key._3: 1000, pyglet.window.key._4: 2000, pyglet.window.key._5: 5000}

        self.windowSize = 576 #Størrelsen af vinduet
        self.yellowBorder = pyglet.shapes.Rectangle(self.startX, self.startY, self.windowSize, 40, color=(255, 234, 0))
        self.text1 = pyglet.text.Label("Bydere:", anchor_x="center", anchor_y="center", font_size=12, x=self.startX+35, y=self.startY+20, width=70, height=40, color=(0, 0, 0, 255))
        self.playerShapes = []
        for players in range(self.nplayers):
            self.playerShapes.append(pyglet.shapes.Rectangle(((players)/self.nplayers*(self.windowSize))+self.startX, self.startY, (self.windowSize)*1/self.nplayers, 40, self.participants[players].circle.color))
            self.playerShapes.append(pyglet.text.Label(f"spiller{players+1}", anchor_x="center", anchor_y="center", x=((((players)/self.nplayers*(self.windowSize)))+(1/2)*(self.windowSize)*1/self.nplayers)+self.startX, y=self.startY+20, color=(0, 0, 0, 255)))
        self.tutorialBox = pyglet.shapes.Rectangle(self.windowSize-200, self.startY+250, 250, 100, (234, 0, 0))
        self.tutorialText = pyglet.text.Label("Tryk på q, for at gå ud af auktionen\nTryk på 1, for at øge bud med 100kr\nTryk på 2, for at øge bud med 500kr\nTryk på 3, for at øge bud med 1000kr\nTryk på 4, for at øge bud med 2000kr\nTryk på 5, for at øge bud med 5000kr\n", multiline=True, anchor_x="left", anchor_y="top", x=self.windowSize-200, y=self.startY+350, font_size=10, width=250, height=200, color=(0, 0, 0, 255))
        self.headertext = pyglet.text.Label("", anchor_x="center", anchor_y="center", bold=True, x=352, y=562, color=(0, 0, 0, 255))

    def initialise(self, kwargs):
        self.data = kwargs
        self.folded = [kwargs["pid"]]
        self.active_player = 0 if 0 != kwargs["pid"] else 1
        self.card = kwargs["card"]
        self.ledger = kwargs["ledger"]
        self.card_drawables = kwargs["card"].drawCard(100,212,200,280)
        self.highest_bidder = self.nplayers-1 if self.nplayers-1 != kwargs["pid"] else self.nplayers-2
        self.highest_bid = 0
        self.headertext.text = ""

        for i in range(self.nplayers):
            if i == kwargs["pid"]:
                self.playerShapes[i*2].color = (128, 128, 128)
            else:
                self.playerShapes[i*2].color = self.participants[i].circle.color


        self.change_rect(self.active_player, 1)
        
    def change_rect(self, player, factor):
        self.playerShapes[2*player].x += 3*factor
        self.playerShapes[2*player].y += 3*factor
        self.playerShapes[2*player].width -= 6*factor
        self.playerShapes[2*player].height -= 6*factor

    def draw(self): #her tegnes alle figurene osv der udgør skærmen
        self.yellowBorder.draw()
        self.text1.draw()
        
        for i in range(len(self.playerShapes)):
            self.playerShapes[i].draw()
        
        self.tutorialBox.draw()
        self.tutorialText.draw()
        self.headertext.draw()
        
        for obj in self.card_drawables:
            obj.draw()

    def rotate_player(self):
        OLD = self.active_player
        self.active_player = (self.active_player+1)%self.nplayers

        while self.active_player in self.folded:
            self.active_player = (self.active_player+1)%self.nplayers

        self.change_rect(OLD, -1)
        self.change_rect(self.active_player, 1)
        

    def on_key_press(self, symbol, modifiers):
        if symbol in self.dict.keys() and self.ledger[self.active_player] > self.highest_bid + self.dict[symbol]: 
            self.highest_bidder = self.active_player
            self.highest_bid += self.dict[symbol]
            self.headertext.text = f"Spiller {self.highest_bidder+1} har det nuværende højeste bud på {self.highest_bid}kr"
            self.rotate_player()
        elif symbol == pyglet.window.key.Q:
            self.folded.append(self.active_player)
            self.playerShapes[2*self.active_player].color = (128,128,128)
            if len(self.folded) == self.nplayers - 1:
                self.dispatch_event("acquire_property", self.data["tile"], self.highest_bidder, self.highest_bid)
                self.change_rect(self.active_player, -1)
            else:
                self.rotate_player()

class UpgradeProperty(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("finalize_upgrade")

        self.headertext = pyglet.text.Label("", anchor_x="center", anchor_y="top", bold=True, x=352, y=612, color=(0, 0, 0, 255), multiline=True, width=400, height=500)
        self.question = pyglet.text.Label("Vil du yderligere opgradere\ndenne grund?", font_size=20, x=550, y=425, color=(0,0,0,255), anchor_x="center", multiline=True, width=300, height=50)

        self.button_1 = pyglet.shapes.Rectangle(400, 300, 75, 40, (0,255,0))
        self.button_2 = pyglet.shapes.Rectangle(480, 300, 75, 40, (255,0,0))

        self.ja_label = pyglet.text.Label("Ja", x=self.button_1.x+self.button_1.height/2, y=self.button_1.y+self.button_1.height/2, anchor_x="center", anchor_y="center", font_size=15, color=(0,0,0,255))
        self.nej_label = pyglet.text.Label("Nej", x=self.button_2.x+self.button_2.height/2, y=self.button_2.y+self.button_2.height/2, anchor_x="center", anchor_y="center", font_size=15, color=(0,0,0,255))

        self.cumulative_cost = 0

    def initialise(self, kwargs):
        self.card = kwargs["card"]
        self.playerCash = kwargs["player_cash"]
        self.tile = kwargs["tile"]
        self.player = kwargs["pid"]
        self.headertext.text = f"Spiller {kwargs['pid']+1} har landet på {self.card.get_name()}, som spilleren allerede ejer.\nDerfor har Spiller {kwargs['pid']} muligheden for at opgraderer {self.card.get_name()}.\nDet vil koste {self.card.upgradeCost}kr at opgradere denne ejendom, som er opgraderet til niveau {self.card.rentIndex}"
        self.cardProperties = self.card.drawCard(100,212,200,280)
        self.cumulative_cost = 0

    def draw(self):
        self.button_1.draw()
        self.ja_label.draw()
        
        self.button_2.draw()
        self.nej_label.draw()
        
        for i in range(len(self.cardProperties)):
            self.cardProperties[i].draw()

        self.headertext.draw()
        self.question.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button != 1: return

        if self.button_1.x <= x <= self.button_1.x+self.button_1.width and self.button_1.y <= y <= self.button_1.y+self.button_1.height:
            self.button_pressed = 1
            self.button_1.color = (0,200,0)
        elif self.button_2.x <= x <= self.button_2.x+self.button_2.width and self.button_2.y <= y <= self.button_2.y+self.button_2.height:
            self.button_pressed = 2
            self.button_2.color = (200,0,0)

    def on_mouse_release(self, x, y, button, modifiers):
        if button != 1: return

        if self.button_pressed == 1 and self.button_1.x <= x <= self.button_1.x+self.button_1.width and self.button_1.y <= y <= self.button_1.y+self.button_1.height and self.playerCash > self.cumulative_cost + self.card.upgradeCost and self.card.rentIndex < len(self.card.rents)-1:
            self.card.incrementRent()
            self.headertext.text = f"Spiller {self.player+1} har landet på {self.card.get_name()}, som spilleren allerede ejer.\nDerfor har Spiller {self.player} muligheden for at opgraderer {self.card.get_name()}.\nDet vil koste {self.card.upgradeCost}kr at opgradere denne ejendom, som er opgraderet til niveau {self.card.rentIndex}"
            self.cumulative_cost += self.card.upgradeCost
        elif self.button_pressed == 2 and self.button_2.x <= x <= self.button_2.x+self.button_2.width and self.button_2.y <= y <= self.button_2.y+self.button_2.height:
            self.dispatch_event("finalize_upgrade", self.tile, self.card, self.cumulative_cost)
        self.button_1.color = (0,255,0)
        self.button_2.color = (255,0,0)

class Prison(pyglet.event.EventDispatcher):
    def __init__(self) -> None:
        super().__init__()
        self.register_event_type("handle_prisoner")

        self.header = pyglet.text.Label("", font_size=20, x=350, y=550, color=(0,0,0,255), anchor_x="center", multiline=True, width=300, height=50)

        self.button_pressed = -1
        self.pay = pyglet.shapes.Rectangle(250, 450, 200, 40, (255,0,0))
        self.roll  = pyglet.shapes.Rectangle(250, 350, 200, 40, (255,0,0))

        self.pay_label = pyglet.text.Label("Betal 1.000kr.", x=self.pay.x+self.pay.width/2, y=self.pay.y+self.pay.height/2, anchor_x="center", anchor_y="center", font_size=15)
        self.roll_label = pyglet.text.Label("Rul", x=self.roll.x+self.roll.width/2, y=self.roll.y+self.roll.height/2, anchor_x="center", anchor_y="center", font_size=15)

    def initialise(self, kwargs):
        self.data = kwargs
        self.cash = kwargs["cash"]
        self.card = kwargs["card"]
        self.player = kwargs["pid"]

    def on_mouse_press(self, x, y, button, modifiers):
        if button != 1: return

        if self.pay.x <= x <= self.pay.x+self.pay.width and self.pay.y <= y <= self.pay.y+self.pay.height:
            self.button_pressed = 1
            self.pay.color = (200,0,0)
        elif self.roll.x <= x <= self.roll.x+self.roll.width and self.roll.y <= y <= self.roll.y+self.roll.height:
            self.button_pressed = 2
            self.roll.color = (200,0,0)

    def on_mouse_release(self, x, y, button, modifiers):
        if button != 1: return

        if self.button_pressed == 1 and self.cash > 1_000 and self.pay.x <= x <= self.pay.x+self.pay.width and self.pay.y <= y <= self.pay.y+self.pay.height:
            self.dispatch_event("handle_prisoner", True, -1)
        elif self.button_pressed == 2 and self.roll.x <= x <= self.roll.x+self.roll.width and self.roll.y <= y <= self.roll.y+self.roll.height:
            self.dispatch_event("handle_prisoner", False, 11)

        self.pay.color = (255,0,0)
        self.roll.color = (255,0,0)

    def draw(self):
        self.header.draw()
        self.roll.draw()
        self.pay.draw()
        self.pay_label.draw()
        self.roll_label.draw()

class Win(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("dummy")

        self.label = pyglet.text.Label("", x=352, y=352, anchor_x="center", anchor_y="center")

    def initialise(self, data):
        self.label.text = f"Spiller {data['pid'] + 1} har vundet"

    def draw(self):
        self.label.draw()