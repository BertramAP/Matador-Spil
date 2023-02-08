import pyglet
from Cards import street, start, Chance, parkingSpace

class Board:
    def __init__(self) -> None:
        self.top_batch = pyglet.graphics.Batch()
        self.bot_batch = pyglet.graphics.Batch()
        
        self.background = pyglet.shapes.Rectangle(64,64,576,576,color=(24,99,18),batch=self.bot_batch)
        self.spaces: list[Space] = generate_spaces(self.bot_batch, self.top_batch)

    def draw(self):
        self.bot_batch.draw()
        self.top_batch.draw()
chance = Chance()

parkingplace = parkingSpace()
Spaces = [[start()], [street("Rødovrevej", [0, 0, 255], 1200, [50, 250, 750, 2250, 4000, 6000]), street("Hvidovrevej", [0, 0, 255], 1200, [50, 250, 750, 2250, 4000, 6000])], [chance], [payTaxSpace(True)], [shippingPort("Scandlines, Helsingør-Helsingborg")],
          [street("Roskildevej", [255, 100, 127], 2000, [100, 600,  1800, 5400, 8000, 11000]), street("Valby langgade", [255, 100, 127], 2000, [100, 600,  1800, 5400, 8000, 11000]), street("Allegade", [255, 100, 127], 2400, [150, 800,  2000, 6000, 9000, 12000])], [chance], [prison(False)],
          [street("Frederiksberg Alle", [0, 255, 0], 2800, [200, 1000, 3000, 9000, 12500, 15000]), street("Bulowsvej", [0, 255, 0], 2800, [200, 1000, 3000, 9000, 12500, 15000]), street("G.L. Kongevej", [0, 255, 0], 3200, [250, 1250, 3750, 10000, 14000, 18000])], [Corparation("Tuborg")], [shippingPort("Mols-Linien")],
          [street("Bernstorttsvej", [128, 128, 128], 3600, [300, 1400, 4000, 11000, 15000, 19000]), street("Hellerupvej", [128, 128, 128], 3600, [300, 1400, 4000, 11000, 15000, 19000]), street("Strandvejen", [128, 128, 128], 4000, [350, 1600, 4400, 12000, 16000, 20000])], [chance], [parkingplace],
          [street("Trianglen", [255, 51, 51], 4400, [350, 1800, 5000, 14000, 17500, 21000]), street("Østerbrogade", [255, 51, 51], 4400, [350, 1800, 5000, 14000, 17500, 21000]), street("Grønningen", [255, 51, 51], 4800, [400, 2000, 6000, 15000, 18500, 22000])], [chance], [shippingPort("Scandlines Gedse-Rostock")]
          [street("Bredgade", [0, 0, 0], 5200, [450, 2200, 6600, 16000, 19500, 23000]), street("Kgs. Nytorv", [0, 0, 0], 5200, [450, 2200, 6600, 16000, 19500, 23000]), street("Østergade", [0, 0, 0], 5600, [500, 2400, 7200, 17000, 20500, 24000])], [Corparation("Coca-Cola")], [prison(True)],
          [street("Amagertorv", [255, 234, 0], 6000, [550, 2600, 7800, 18000, 22000, 25000]), street("Vimmelskaftet ", [255, 234, 0], 6000, [550, 2600, 7800, 18000, 22000, 25000]), street("Nygade",[255, 234, 0], 6400, [600, 3000, 9000, 20000, 24000, 28000])], [chance], [shippingPort("Scandlines, Rødby-Puttgarden")],
          [Chance],[street("Frederiksberggade", [255, 234, 0], 7000, [700, 3500, 10000, 22000, 26000, 30000]), street("Rådhuspladsen", [255, 234, 0], 8000, [1000, 4000, 12000, 28000, 34000, 40000])],[payTaxSpace(False)]]
newSpaces = []
for i in range(len(Spaces)):
    if (len(Spaces[i]) > 1):
        for x in range(len(Spaces[i])):
            if (x == 1):
                b = i + 1
                newSpaces.append(Spaces[b][0])
                newSpaces.append(Spaces[i][x])
            else:
                newSpaces.append(Spaces[i][x])
            i+=1
    newSpaces.append(Spaces[i][0])

class Space:
    def __init__(self, pos: tuple[int, int], event: str, font_size: int, bgc: tuple[int], batch1: pyglet.graphics.Batch, batch2: pyglet.graphics.Batch) -> None:
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.event: str = event

        self.background = pyglet.shapes.Rectangle(self.x+4,self.y+4,56,56,color=bgc,batch=batch1)

        document = pyglet.text.decode_text(event)
        document.set_style(0,len(document.text), dict(font_size=font_size))
        self.label = pyglet.text.layout.TextLayout(document,56,56,wrap_lines=True,batch=batch2)
        self.label.x = self.x+32
        self.label.y = self.y+32
        self.label.anchor_x = "center"
        self.label.anchor_y = "center"

def generate_spaces(bot_batch, top_batch):
    lst = [0]*40

    lst[0] = Space((0,0),"START", 10, (234,169,28), bot_batch, top_batch)

    for i in range(1, 40):
       lst[i] = Space(get_coord(i), str(i), 10, (255,255,255), bot_batch, top_batch)

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