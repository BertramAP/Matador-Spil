import pyglet
from random import randint

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
        self.dice = [pyglet.sprite.Sprite(dice_pic.get_region(i*96,0,96,96),x=244,y=290, batch=self.bbatch) for i in range(6)]

    def initialise(self):
        #TODO: scedule dice_drawer funktionen her til TBA gange i sekundet

    def end(self):
        #TODO: unschedule dice_drawer funktionen her

    def dice_drawer():
        #TODO: blit to tilfældige terninger ind over rul knappen

    def draw(self):
        self.bbatch.draw()
        self.tbatch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250:
            self.pressed_button = True
            self.button.color = (200,0,0)
        else: self.pressed_button = False
        
    def on_mouse_release(self, x, y, button, modifiers):
        self.button.color = (255,0,0)
        if button == 1 and 300 <= x <= 400 and 200 <= y <= 250 and self.pressed_button:
            self.dispatch_event("rolled", randint(1,6) + randint(1,6))
            

