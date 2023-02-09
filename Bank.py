import pyglet

class Bank(pyglet.event.EventDispatcher):
    def __init__(self, start_cash: int, nplayers: int):
        self.ledger = [start_cash]*nplayers

    def 