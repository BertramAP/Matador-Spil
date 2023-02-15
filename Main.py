import pyglet
import Player
import Board
import Screens
import Cards
import Bank

import random

import os

class Game(pyglet.event.EventDispatcher):
    def __init__(self, window: pyglet.window.Window, nplayers) -> None:
        super().__init__()
        self.register_event_type("rolled")
        self.register_event_type("next_player")
        self.register_event_type("change_screen")
        self.register_event_type("auctioned")
        self.register_event_type("finalize_upgrade")
        
        self.board = Board.Board()

        self.pbatch = pyglet.graphics.Batch()

        self.players = [Player.Player(i, Board.get_player_coords(i,16,0), 16, Player.Player.get_color(i)) for i in range(nplayers)]
        self.active_player: int = 0
        self.nplayers: int = nplayers

        self.screens = {"Roller": Screens.Roller(), "Idle": Screens.Idle(), "BuyProperty": Screens.BuyProperty(), "Auction": Screens.Auction(self.players), "UpgradeProperty": Screens.UpgradeProperty()}
        self.active_screen = "Roller"
        for key in self.screens.keys():
            self.screens[key].push_handlers(self)

        self.window = window
        self.window.set_handler("on_draw", self.on_draw)
        self.window.push_handlers(self.screens[self.active_screen])

        self.bank = Bank.Bank(self.players, nplayers)

        for player in self.players:
            player.push_handlers(self)

        self.change_screen("Roller", dict(color=self.players[self.active_player].circle.color))

    def change_screen(self, tscreen: str, data: dict) -> None:
        self.window.pop_handlers()
        self.window.push_handlers(self.screens[tscreen])
        self.screens[tscreen].initialise(data)
        self.active_screen = tscreen

    def on_draw(self) -> None:
        self.window.clear()
        self.board.draw()
        self.screens[self.active_screen].draw()
        self.draw_player_stuff()

    def draw_player_stuff(self) -> None:
        for player in self.players:
            player.circle.draw()

        self.bank.draw()

    def next_player(self) -> None:
        self.active_player = (self.active_player+1)%self.nplayers
        self.change_screen("Roller", dict(color=self.players[self.active_player].circle.color))

    def acquire_property(self, tile, pid, price):
        self.bank.withdraw(pid, price)
        self.board.update_ownership(tile, pid)
        self.board.update_rent(tile)
        self.next_player()

    def auctioned(self, data):
        self.change_screen("Auction", data)

    def rolled(self, val) -> None:
        tile = self.players[self.active_player].move_by(val)
        self.go_to(self.active_player, tile, roll=val)

    def finalize_upgrade(self, tile, card, cumulative_cost):
        self.board.set_card(tile, card)
        self.bank.withdraw(card.owner, cumulative_cost)

    def go_to(self, pid, tile, moved=True, roll=0):
        if not moved: self.players[pid].move_to(tile)

        card = self.board.get_card(tile)
        space_type = type(card)

        if space_type in (Cards.street, Cards.shippingPort, Cards.Corparation):
            if card.owner == pid and space_type == Cards.street and card.upgradable == True:
                if card.rentIndex >= len(card.rents)-1:
                    self.change_screen("Idle", dict(text="Du har landet på dit eget fuldt opgraderede kort."))
                else:
                    self.change_screen("UpgradeProperty", dict(tile=tile,  player_cash=self.bank.get_holdings(pid), pid=pid, card=card))
            elif card.owner != -1:
                if self.bank.transfer(self.active_player, card.owner, card.get_rent(roll)):
                    self.change_screen("Idle", dict(text=f"Du har betalt {card.get_rent(roll)} i leje"))
                else:
                    pass#TODO: tilføj skærm til håndtering af bankerot spillere ("du har tabt haha" tekst, pantsætning osv.)
            elif card.owner == -1:
                self.change_screen("BuyProperty", dict(card=card, pid=self.active_player, ledger=self.bank.get_ledger(), tile=tile))

        elif space_type == Cards.parkingSpace or (space_type == Cards.prison and card.visit):
            self.change_screen("Idle", dict(text=card.idle_text))

        elif space_type == Cards.payTaxSpace:
            tax_info = card.payTax(self.bank.get_holdings(self.active_player))
            if self.bank.transfer(self.active_player, -1, tax_info[0]):
                self.change_screen("Idle", dict(text=tax_info[1]))
            else:
                pass#TODO: tilføj skærm til håndtering af bankerot spillere ("du har tabt haha" tekst, pantsætning osv.)

        else: self.change_screen("Idle", dict(text="Du har rullet"))

if __name__ == "__main__":
    SIDELENGTH = 704
    window = pyglet.window.Window(SIDELENGTH, SIDELENGTH)

    game = Game(window, 4)

    pyglet.app.run()