class Conversions:


    def m2f(m):
        return m*3.28084
    #Nautical Miles to km
    def nmtokm(nm):
        return nm*1.852
    #Kilometres to Nautical Miles
    def kmtonm(km):
        return km/1.852
    #Km/h to m/s
    def kmhtoms(kmh):
        return (kmh*1000)/3600
    #lb to Newton
    def lbtoN(lb):
        return lb*4.448