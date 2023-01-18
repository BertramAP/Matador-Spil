import pyglet
import Player
import Board
import Roller

class Game(pyglet.event.EventDispatcher):
    def __init__(self, window: pyglet.window.Window, nplayers, ndollars) -> None:
        super().__init__()
        self.register_event_type("rolled")
        
        self.board = Board.Board()

        self.screens = [Roller.Roller()]
        self.active_screen = 0
        self.screens[self.active_screen].push_handlers(self)

        self.players = [Player.Player(i, Board.get_player_coords(i,16,0), 16, Player.Player.get_color(i), ndollars) for i in range(nplayers)]
        self.active_player: int = 0
        self.nplayers: int = nplayers

        self.window = window
        self.window.set_handler("on_draw", self.on_draw)
        self.window.push_handlers(self.screens[self.active_screen])
        
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

        for player in self.players:
            player.draw()

    def rolled(self, val):
        self.players[self.active_player].move_by(val)
        self.active_player = (self.active_player+1)%self.nplayers
    
if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game(window, 4, 500)

    pyglet.app.run()
    