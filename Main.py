import pyglet
import Player
import Board
import Screens

import random

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
        self.players = [Player.Player(i, Board.get_player_coords(i,16,0), 16, Player.Player.get_color(i), ndollars, self.pbatch) for i in range(nplayers)]
        self.active_player: int = 0
        self.nplayers: int = nplayers

        self.docs = [pyglet.text.decode_text(str(player.money)+"kr.") for player in self.players]
        self.layouts = [pyglet.text.layout.TextLayout(doc, 576/nplayers, 50, batch=self.pbatch) for doc in self.docs]

        for i in range(nplayers):
            self.layouts[i].x = 64+i*576/nplayers
            self.layouts[i].y = 64

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
        self.pbatch.draw()

    def next_player(self) -> None:
        self.active_player = (self.active_player+1)%self.nplayers
        self.init_screen(0)

    def rolled(self, val):
        self.players[self.active_player].move_by(val)
        self.players[self.active_player].make_payment(val)
        self.next_player()

    def update_bank(self, pid):
        self.docs[pid].text = str(self.players[self.active_player].money)

if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game(window, 4, 30_000)

    pyglet.app.run()
    