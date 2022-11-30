import pyglet

class Board:
    def __init__(self, batch: pyglet.graphics.Batch) -> None:
        self.background = pyglet.shapes.Rectangle(64,64,576,576,color=(24,99,18),batch=batch)
        self.spaces: list[Space] = [Space(0,0,"START", (234,169,28), batch)]

class Space:
    def __init__(self, x: int, y: int, event: str, bgc: tuple[int], batch: pyglet.graphics.Batch) -> None:
        self.x: int = x
        self.y: int = y
        
        self.event: str = event

        self.background = pyglet.shapes.Rectangle(self.x+4,self.y+4,56,56,color=bgc,batch=batch)

        document = pyglet.text.decode_text(event)
        self.label = pyglet.text.layout.TextLayout(document,56,56,wrap_lines=True,batch=batch)
        self.label.x = self.x+32
        self.label.y = self.y+32
        self.label.anchor_x = "center"
        self.label.anchor_y = "center"