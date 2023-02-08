import pyglet
import Cards

class Board:
    def __init__(self) -> None:
        self.top_batch = pyglet.graphics.Batch()
        self.bot_batch = pyglet.graphics.Batch()
        
        self.background = pyglet.shapes.Rectangle(64,64,576,576,color=(24,99,18),batch=self.bot_batch)
        self.spaces: list[Cards.Space] = Cards.generate_spaces(self.bot_batch, self.top_batch)

    def draw(self):
        self.bot_batch.draw()
        self.top_batch.draw()

def generate_spaces(bot_batch, top_batch):
    lst = [0]*40

    lst[0] = Cards.Space((0,0),"START", 10, (234,169,28), bot_batch, top_batch)

    for i in range(1, 40):
       lst[i] = Cards.Space(get_coord(i), str(i), 10, (255,255,255), bot_batch, top_batch)

    return lst

def get_coord(i: int):
    if i < 11:
        return (0, 64*i)
    if i < 20:
        i -= 10
        return (i*64, 640)
    if i < 30:
        i -= 20
        return (640, 640 - i*64)
    i -= 30
    return (640 - i*64, 0)

def get_player_coords(pid: int, r: int, i: int) -> tuple[int, int]:
    pos = get_coord(i)

    x = pos[0] + r
    y = pos[1] + r

    if pid in (1, 3):
        x += 2*r
    if pid in (2,3):
        y += 2*r
    return (x, y)