import pyglet
import Player
import Board

class Game(pyglet.event.EventDispatcher):
    def __init__(self, nplayers, ndollars) -> None:
        super().__init__()

        self.board = Board.Board()
        self.players = [Player.Player(i, Board.get_player_coords(i,16,0), 16, Player.Player.get_color(i), ndollars) for i in range(nplayers)]
        print(len(self.players))

    def on_draw(self):
        self.board.draw()

        for player in self.players:
            player.draw()
    
if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game(4, 500)
    window.push_handlers(game)

    pyglet.app.run()
    