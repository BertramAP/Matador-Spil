import pyglet
from random import randint, sample
from time import sleep

class Roller(pyglet.event.EventDispatcher):
    def __init__(self):
        super().__init__()
        self.register_event_type("rolled")

        self.tbatch = pyglet.graphics.Batch()
        self.bbatch = pyglet.graphics.Batch()

        self.pressed_button = False

        self.button = pyglet.shapes.Rectangle(300, 200, 100, 50, (255,0,0), batch=self.bbatch)
        self.label = pyglet.text.Label("Rul", anchor_x="center",font_size=30, x=350, y= 210, batch=self.tbatch)

        dice_pic = pyglet.image.load("resources/dice2.png")
        self.all_dice = [dice_pic.get_region(i*96,0,96,96) for i in range(6)]
        self.dice = sample(self.all_dice, 2)

        self.clock = pyglet.clock.get_default()

    def initialise(self):
        self.clock.schedule_interval(self.dice_changer, 0.1)

    def end(self):
        pass

    def throw_success(self, dt, res) -> None:
        self.dispatch_event("rolled", res)

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
            self.button.color = (200,0,0)
        else: self.pressed_button = False
        
    def on_mouse_release(self, x, y, button, modifiers):
        self.button.color = (255,0,0)
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250 and self.pressed_button:
            self.clock.unschedule(self.dice_changer)
            one = randint(1,6)
            two = randint(1,6)
            self.dice = [self.all_dice[one-1], self.all_dice[two-1]]
            
            self.clock.schedule_once(self.throw_success, 2, res=one+two)

