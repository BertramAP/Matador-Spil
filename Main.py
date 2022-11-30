import pyglet
from Player import Player
from Board import Board

class Game(pyglet.event.EventDispatcher):
    def __init__(self) -> None:
        super().__init__()

        self.batch = pyglet.graphics.Batch()        

        self.board = Board(self.batch)

    def on_draw(self):
        self.batch.draw()
    
if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game()
    window.push_handlers(game)

    pyglet.app.run()
    