import pyglet

class Board:
    def __init__(self) -> None:
        self.top_batch = pyglet.graphics.Batch()
        self.bot_batch = pyglet.graphics.Batch()
        
        self.background = pyglet.shapes.Rectangle(64,64,576,576,color=(24,99,18),batch=self.bot_batch)
        self.spaces: list[Space] = generate_spaces(self.bot_batch, self.top_batch)

    def draw(self):
        self.bot_batch.draw()
        self.top_batch.draw()


class Space:
    def __init__(self, x: int, y: int, event: str, font_size: int, bgc: tuple[int], batch1: pyglet.graphics.Batch, batch2: pyglet.graphics.Batch) -> None:
        self.x: int = x
        self.y: int = y
        self.event: str = event

        self.background = pyglet.shapes.Rectangle(self.x+4,self.y+4,56,56,color=bgc,batch=batch1)

        document = pyglet.text.decode_text(event)
        document.set_style(0,len(document.text), dict(font_size=font_size))
        self.label = pyglet.text.layout.TextLayout(document,56,56,wrap_lines=True,batch=batch2)
        self.label.x = x+32
        self.label.y = y+32
        self.label.anchor_x = "center"
        self.label.anchor_y = "center"

def generate_spaces(bot_batch, top_batch):
    lst = [0]*40

    lst[0] = (Space(0,0,"START", 10, (234,169,28), bot_batch, top_batch))

    #for i in range(1, 39)
    #   lst[i] = <genereret space>

    return lst

def get_coord(i: int):