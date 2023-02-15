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
    
    def set_card(self, tile, card):
        self.spaces[tile].card = card
    
    def update_ownership(self, property, pid):
        self.spaces[property].card.owner = pid
        self.ownership_indicators[property].color = Player.Player.get_color(pid)
    
    def update_rent(self, tile):
        if type(self.spaces[tile].card) == Cards.street:
            indices=[]
            card=self.spaces[tile].card
            all_owned=True

            for index, space in enumerate(self.spaces):
                if space.card.color == card.color:
                    indices.append(index)
                    if space.card.owner != card.owner:
                        all_owned = False
            
            if all_owned:
                for index in indices:
                    self.spaces.upgradable = True
        
        elif type(self.spaces[tile].card) in (Cards.shippingPort, Cards.Corparation):
            indices=[]
            card=self.spaces[tile].card
            owned = 0

            for index, space in enumerate(self.spaces):
                if space.card.color == card.color and space.card.owner == card.owner:
                    indices.append(index)
                    owned += 1
            
            for index in indices:
                self.spaces[index].card.owned = owned

def get_player_coords(pid: int, r: int, i: int) -> tuple[int, int]:
    pos = Cards.get_coord(i)

    x = pos[0] + r
    y = pos[1] + r

    if pid in (1, 3):
        x += 2*r
    if pid in (2,3):
        y += 2*r
    return (x, y)