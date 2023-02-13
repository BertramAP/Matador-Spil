import pyglet
import Cards
import Player

class Board:
    def __init__(self) -> None:
        self.top_batch = pyglet.graphics.Batch()
        self.bot_batch = pyglet.graphics.Batch()
        
        self.background = pyglet.shapes.Rectangle(64,64,576,576,color=(24,99,18),batch=self.bot_batch)
        self.spaces: list[Cards.Space] = Cards.generate_spaces(self.bot_batch, self.top_batch)
        self.ownership_indicators: list = [pyglet.shapes.Circle(space.x+7, space.y+7, 3, color=space.card.RGB, batch=self.top_batch) if hasattr(space.card, "owner") else None for space in self.spaces]

    def draw(self):
        self.bot_batch.draw()
        self.top_batch.draw()

    def get_card(self, tile: int):
        return self.spaces[tile].card
    
    def update_ownership(self, property, pid):
        self.spaces[property].card.owner = pid
        self.ownership_indicators[property].color = Player.Player.get_color(pid)

def get_player_coords(pid: int, r: int, i: int) -> tuple[int, int]:
    pos = Cards.get_coord(i)

    x = pos[0] + r
    y = pos[1] + r

    if pid in (1, 3):
        x += 2*r
    if pid in (2,3):
        y += 2*r
    return (x, y)