class Conversions:


    def m2f(self, m):
        return m*3.28084
    #Nautical Miles to km
    def nmtokm(self, nm):
        return nm*1.852
    #Kilometres to Nautical Miles
    def kmtonm(self, km):
        return km/1.852
    #Km/h to m/s
    def kmhtoms(self, kmh):
        return (kmh*1000)/3600
    #lb to Newton
    def lbtoN(self, lb):
        return lb*4.448