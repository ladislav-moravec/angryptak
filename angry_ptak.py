from ptak import Ptak

class AngryPtak(Ptak):

    vztek = 50

    def provokuj(self, mira):
        if self.hlad > 0:
            self.vztek += mira * 2
        else:
            self.vztek += mira

    def __str__(self):
        return "Jsem angry-pták s váhou {} a hladem {}, míra mého vzteku je {}.".format(self.vaha, self.hlad, self.vztek)

