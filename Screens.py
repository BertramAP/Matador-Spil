import pyglet
from random import randint, sample

class Roller(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("rolled")

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
        self.button.color = self.color
        self.pcolor = (self.color[0]*0.8, self.color[1]*0.8, self.color[2]*0.8)

    def throw_success(self, dt, res) -> None:
        print(self.dispatch_event("rolled", res))

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
            
            self.clock.schedule_once(self.throw_success, 2, res=one+two)

class Idle(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("next_player")

        self.tbatch = pyglet.graphics.Batch()
        self.bbatch = pyglet.graphics.Batch()

        self.button = pyglet.shapes.Rectangle(270, 200, 160, 50, (255,0,0), batch=self.bbatch)
        self.text = [pyglet.text.Label("Forstået", anchor_x="center",font_size=30, x=350, y= 210, batch=self.tbatch),
                     pyglet.text.Label("TBA", anchor_x="center",font_size=20,x=350,y=500,batch=self.tbatch)
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
        self.register_event_type("check_balance")
        self.register_event_type("balance_checked")
        self.register_event_type("next_player")

        self.question = pyglet.text.Label("Vil du købe følgende\ngrund?", font_size=20, x=500, y=500, color=(0,0,0,255), anchor_x="center", multiline=True, width=300, height=50)

    def initialise(self, kwargs):
        self.card = kwargs["card"]
        self.card_drawables = self.card.drawCard(100,100,150,300)
        self.player = kwargs["pid"]

    def draw(self):
        self.question.draw()
        
        for obj in self.card_drawables:
            obj.draw()

class Auction(pyglet.event.EventDispatcher):
    def __init__(self, players) -> None:
        super().__init__()
        self.register_event_type("acquire_property")
        self.register_event_type("check_balance")
        self.register_event_type("balance_checked")

        self.participants = players
        self.folded = []
        self.card = None

        self.windowSize = 576 #Størrelsen af vinduet
        self.box1 = pyglet.shapes.Rectangle(0, self.windowSize-40, 70, 40, (255, 255, 255))
        self.text1 = pyglet.text.Label("Bidders:", anchor_x="center", anchor_y="center", font_size=30, x=35, y=self.windowSize-20)
        self.playerShapes = []
        self.playerText = []
        for players in range(len(self.participants)):
            self.playerShapes.append(pyglet.shapes.Rectangle(((players)/len(self.participants)*(self.windowSize-70))+70, self.windowSize-40, 1/len(self.participants), 40, self.participants[players].circle.color))
            self.playerText.append(pyglet.text.Label(f"player{players+1}", anchor_x="center", anchor_y="center", x=(((players)/len(self.participants)*(self.windowSize-70))+70)+1/(1/len(self.participants)), y=self.windowSize-20))

    def initialise(self, kwargs):
        self.folded.append(kwargs["initiator"])
        self.card = kwargs

    def draw(self):
        self.box1.draw()
        self.text1.draw()
        for i in range(len(self.playerShapes)):
            self.playerShapes[i].draw()
            self.playerText[i].draw()
        #her tegnes alle figurene osv der udgør skærmen