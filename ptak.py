class Ptak():
    #Trida reprezentuje ptaka
    hlad = 100
    #váha v gramech
    vaha = 50

    #sni jidlo, coz snici hlad a zvysi vahu
    def snez(self, gramu):
        self.vaha += gramu
        self.hlad -= gramu
        if self.hlad < 0:
            self.hlad = 0

    # vrati textovou reprezentaci ptaka
    def __str__(self):
        return "Jsem pták s váhou {} a hladem {}.".format(self.vaha, self.hlad)