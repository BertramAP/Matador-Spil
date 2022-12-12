import random

community_chest = ["Kør hen til Start", "Du får 200kr fra aktie salg", "Du arver 500", "Du skal betale din søns hospital regning på 700kr"
                   "Tag 300kr for hver spiller", "Du har betalt for meget i skat, du modtager 150kr fra skatteministeriet", "modtag 200 kr for dine service",
                   "Du er kommet til skade, derfor skal du betale lægen 100kr", "Gå i føngsæet (spring start feldtet over)", "Bank fejl i din fordel, indsaml 1500kr", 
                   "Din juleopsparelse stiger i værdi, indsaml 400kr", "Din livsforsikring stiger, indsaml 300kr", "Fængels frikort", "Betal skole skat på 800kr"
                   "Du er kommet på en anden plads i en skønhedskonkurrence, indsaml 150kr", "Du skal betale for vejarbejde på din grunde, 150kr pr hus, 700kr pr hotel"]
chance = ["Du er blevet valgt som formand for bordet, betal hver spiller 200kr", "Din bolig værdi stiger, indsaml 900kr", "Fængsels frikort", 
          "Banken udbetaler dig et udbytte på 400kr", "Betal din resterende top skat på 300kr", "Rejs til en tog station, og indsaml 200kr hvis du passerer start"
          "Rejs til start brikken (indsaml 200kr)", "Rejs til Frederiksberg Alle (indsaml 200kr hvis du passerer start)", "Gå tre fælter tilbage", 
          "Rejs til Rådhuspladsen", "Rejs til nærmeste togstation. Hvis stationen er ejet, så skal du betale ejeren dobbelt "]

class Mysterycard:
    def __init__(self) -> None:
        self.cardType = random.randint
    