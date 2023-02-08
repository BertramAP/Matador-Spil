import pyglet
import Player
import Board
import Screens

import random

import os

class Game(pyglet.event.EventDispatcher):
    def __init__(self, window: pyglet.window.Window, nplayers, ndollars) -> None:
        super().__init__()
        self.register_event_type("rolled")
        self.register_event_type("update_bank")
        
        self.board = Board.Board()

        self.screens = [Screens.Roller(), ]
        self.active_screen = 0
        self.screens[self.active_screen].push_handlers(self)

        self.pbatch = pyglet.graphics.Batch()

        self.players = [Player.Player(i, Board.get_player_coords(i,16,0), 16, Player.Player.get_color(i), ndollars) for i in range(nplayers)]
        self.active_player: int = 0
        self.nplayers: int = nplayers

        self.money_labels = [pyglet.text.Label(str(player.money)+"kr.", x=64+(player.id+0.5)*576/nplayers, y=68, anchor_x="center", font_name="Times New Roman", color=(0,0,0,255), bold=True) for player in self.players]
        self.background_rect = pyglet.shapes.Rectangle(64,64,576,20,color=(0,0,0))
        self.label_rects = [pyglet.shapes.Rectangle(64+2+player.id*(576-2)/nplayers,64,(576-2)/nplayers-2,18, color=player.circle.color) for player in self.players]

        self.window = window
        self.window.set_handler("on_draw", self.on_draw)
        self.window.push_handlers(self.screens[self.active_screen])

        for player in self.players:
            player.push_handlers(self)

        self.init_screen(0)

    def init_screen(self, tindex: int) -> None:
        self.screens[self.active_screen].end()
        self.window.pop_handlers()

        self.window.push_handlers(self.screens[tindex])
        self.screens[tindex].initialise()
        
        self.active_screen = tindex

    def on_draw(self):
        self.window.clear()

        self.board.draw()
        self.screens[self.active_screen].draw()
        self.draw_player_stuff()

    def draw_player_stuff(self):
        for player in self.players:
            player.circle.draw()

        self.background_rect.draw()

        for rect in self.label_rects:
            rect.draw()

        for label in self.money_labels:
            label.draw()

    def next_player(self) -> None:
        self.active_player = (self.active_player+1)%self.nplayers
        self.init_screen(0)

    def rolled(self, val):
        self.players[self.active_player].move_by(val)
        self.players[self.active_player].make_payment(val)
        self.next_player()

    def update_bank(self, pid):
        self.money_labels[pid].text = str(self.players[self.active_player].money)+"kr."

if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game(window, 3, 30_000)

    pyglet.app.run()
    