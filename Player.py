import pyglet

class Player:
    def __init__(self, id: int, pos: tuple[int, int], r: int, color: tuple[int, int, int], money: int,):
        self.id: int = id
        self.circle = pyglet.shapes.Circle(pos[0], pos[1], r, color=color)
        self.money: int = money
        self.tile = 0

    def draw(self):
        self.circle.draw()

    def set_pos(self, pos: tuple[int, int]):
        self.circle.x, self.circle.y = pos

    def move_to(self, i: int):
        self.tile = i
        if i < 11:
            res = (0, 64*i)
        elif i < 20:
            i -= 10
            res = (i*64, 640)
        elif i < 30:
            i -= 20
            res = (640, 640 - i*64)
        elif i < 40:
            i -= 30
            res = (640 - i*64, 0)

        x = res[0] + 16
        y = res[1] + 16

        if self.id in (1, 3):
            x += 2*16
        if self.id in (2,3):
            y += 2*16

        self.set_pos((x,y))

    def move_by(self, spaces: int) -> None:
        self.move_to((self.tile+spaces)%40)

    @staticmethod
    def get_color(pid):
        colors = [(255,0,0), (0,0,255), (0,255,0), (244,179,38)]
        return colors[pid]

