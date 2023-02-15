string = ["Kør hen til Start", "Du får 2000kr fra aktie salg", "Du arver 6000kr", "Du skal betale din søns hospital regning på 4200kr"
                           "Tag 1500kr for hver spiller", "Du har betalt for meget i skat, du modtager 2000kr fra skatteministeriet", "modtag 1000kr for dine service",
                           "Du er kommet til skade, derfor skal du betale lægen 700kr", "Gå i dirkete i fængsel (spring start feldtet over)", "Bank fejl i din fordel, indsaml 1500kr",
                           "Din juleopsparelse stiger i værdi, indsaml 2000kr", "Din livsforsikring stiger, indsaml 1200kr", "Fængels frikort", "Betal skole skat på 2500kr"
                           "Du er kommet på en anden plads i en skønhedskonkurrence, indsaml 3500kr", "Du skal betale for vejarbejde på din grunde, 200kr pr hus, 700kr pr hotel","Du er blevet valgt som formand for bordet, betal hver spiller 500kr", "Din bolig værdi stiger, indsaml 4500kr", "Fængsels frikort",
                           "Banken udbetaler dig et udbytte på 1800kr", "Betal din resterende top skat på 1200kr", "Rejs til en vilkårlig skibshavn, og indsaml 4000kr hvis du passerer start"
                           "Rejs til start brikken (indsaml 4000kr)", "Rejs til Frederiksberg Alle (indsaml 4000kr hvis du passerer start)", "Gå tre fælter tilbage",
                           "Rejs til Rådhuspladsen", "Rejs til nærmeste skibshavn. Hvis havnen er ejet, så skal du betale ejeren dobbelt", 
                           "Rejs til det nermæste virksomhed, hvis virksomheden allerede er ejet, så slå terningen og betal ejeren 100 gange det der blev slået", "Rejs til Grønningen",
                           "Gå i dirkete i fængsel (spring start feldtet over)", "Din ejendomme skal reperares. For hvert hus du ejer betal 200kr, og for hvert hotel du ejer betal 800kr"]

for i in range(len(string)):
    string[i] = "(\""+string[i]+"\", {\"event\": \"MYSTERY_\"}), "

print("[" + "".join(string) + ")")