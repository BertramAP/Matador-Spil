import pyglet
from Player import Player
from Board import Board

class Game(pyglet.event.EventDispatcher):
    def __init__(self) -> None:
        super().__init__()

        self.board = Board()

    def on_draw(self):
        self.board.draw()
        #self.board.spaces[0].label.draw()
    
if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game()
    window.push_handlers(game)

    pyglet.app.run()
    