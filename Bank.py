import pyglet

class Bank:
    def __init__(self, players: list, nplayers: int):
        STARTCASH = 30_000
        self.ledger = [STARTCASH]*nplayers
        self.nplayers = nplayers

        self.money_labels = [pyglet.text.Label(str(STARTCASH)+"kr.", x=64+(player.id+0.5)*576/nplayers, y=68, anchor_x="center", font_name="Times New Roman", color=(0,0,0,255), bold=True) for player in players]
        self.background_rect = pyglet.shapes.Rectangle(64,64,576,20,color=(0,0,0))
        self.label_rects = [pyglet.shapes.Rectangle(64+2+player.id*(576-2)/nplayers,64,(576-2)/nplayers-2,18, color=player.circle.color) for player in players]

    def draw(self):
        self.background_rect.draw()

        for rect in self.label_rects:
            rect.draw()

        for label in self.money_labels:
            label.draw()

    def withdraw(self, pid, amount):
        self.ledger[pid] -= amount
        self.update_labels()

    def deposit(self, pid, amount):
        self.ledger[pid] += amount
        self.update_labels()

    def transfer(self, p1, p2, amount):
        if self.ledger[p1] > amount:
            self.withdraw(p1, amount)
            if p2 != -1: self.deposit(p2, amount)
            return True
        return False

    def update_labels(self):
        for i, label in enumerate(self.money_labels):
            label.text = str(self.ledger[i])+"kr."

    def get_ledger(self):
        return self.ledger
    
    def get_holdings(self, pid):
        return self.ledger[pid]
    
    def freeze_account(self, pid):
        self.ledger[pid] = 0
        self.label_rects[pid].color = (128,128,128)
        self.update_labels()