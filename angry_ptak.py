from ptak import Ptak

class AngryPtak(Ptak):
    # třída reprezentuje poddruh ptáka se schopností vzteku
    #vztek angry-ptáka
    vztek = 50

    # vyprovokuje angry-ptáka, čímyž zvýší jeho vztek v závislosti na hladu
    def provokuj(self, mira):
        if self.hlad > 0:   # hladový angry pták se necha vyprovokovat 2x snáze
            self.vztek += mira * 2
        else:
            self.vztek += mira

    def __str__(self):
        return "Jsem angry-pták s váhou {} a hladem {}, míra mého vzteku je {}.".format(self.vaha, self.hlad, self.vztek)

