import pyglet

class Player:
    def __init__(self, id: int, pos: tuple[int, int], r: int, color: tuple[int, int, int], money: int,):
        self.circle = pyglet.shapes.Circle(pos[0], pos[1], r, color=color)
        self.money = money

    def draw(self):
        self.circle.draw()

    def set_pos(self, pos: tuple[int, int]):
        self.circle.x, self.circle.y = pos

    @staticmethod
    def get_color(pid):
        colors = [(255,0,0), (0,0,255), (0,255,0), (244,179,38)]
        return colors[pid]

