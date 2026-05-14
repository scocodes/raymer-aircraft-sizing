class RaymerVariables:

    def __init__(self, conversions, Wto):
        self.conversions = conversions
        self.Wto = Wto

        #Raymer Variables List
        self.kdw = 1 #Delta Wing Parameter, 0.768 for a delta wing, 1 otherwise
        self.kvs = 1 #1.19 For variable sweep wing, 1 otherwise
        self.Nz = 11.25  #1.5*ultimate load factor
        self.Nl = 3  # Ultimate landing loading factor Ngear x 1.5 
        self.Sw = 544.44 # Trapezoidal wing areas
        self.tc_naca6716 = 0.16
        self.lambdaa = 0.898
        self.Scsw = 40.72 #Control Surface main wing area 
        self.Fw = 3 #Fuselage width at horizontal tail intersection ft 
        self.Bh = 18.37  #Hortizontal Tail span
        self.Sht = 89.45 #Hortizontal tail area
        self.Krht = 1    #1.047 for rollinh tail, 1 otherwise
        self.Ht = 0  #0 for a conventional tail, 1 for a t tail
        self.Hv = 8.2    #Vertical tiail height about fuselage   
        self.Svt = 83.96 #Vertial Tail area
        self.M = 0.58    #Mach number at cruise
        self.Lt = 14.72-(6.7-1.5)    #Tail length
        self.Sr = 23.47  #Rudder area
        self.Avt = 1.08  #Aspect Rtaio for the vertical tail
        self.Kcb = 1 #2.25 for ross beam, 1 otherwise
        self.Ktpg = 0.826    #0.826 for tripod, 1 otherwise 
        self.Wl = 0.85*Wto   #Landing design gross weight 0.85*Wdg
        self.Nc = 1  #Number of Crew
        self.Lm = 70.87 #Length of main landing gear inch
        self.Ln = 74.80 #Nose gear length inch
        self.Nnw = 1 #Number of nose wheels 
        self.Nen = 2 #Number of engines
        self.Wen = 1440 #engine weight lb
        self.T = 9065*2  #Total engine thrust lb
        self.Vt = 1642 #total fuel volume gal
        self.Vi = self.Vt#integral tanks volume, gal
        self.Vp = self.Vt #self sealing tankls volume, gal
        self.Scs = self.Scsw + 15.98 #Total control surfaces area
        self.Ns =  3  #Number of flight control systems
        self.Nci = 1 #1 if single pilot, 1.2 if pilot plus backseater, 2 if pilot and copassenger
        self.Kvsh = 1        #1.425 for variable sweep wing, 1 ogtherwise
        self.Nu = 10 #number of hydraulic utility functions (5-15)
        self.Kmc = 1.45  #1.45 if mission completion required after failure, 1 otherwise
        self.Rkva = 130 #system rating kv (110-160)
        self.La = 1.5*53.35 #electrical routing distance from generators to avionics to cockpit in ft
        self.Ngen = self.Nen  #Number of generators
        self.Wuav = 1200 #Uninstalled aviatonics mas (800-1400lb)
        self.L = self.conversions.m2f(16.26)
        self.D = self.conversions.m2f(2.1)
        self.W = self.conversions.m2f(1.3)
        self.Nt = 4  #Number of generators
        self.SFC = 0.371 #Specific fuel consumption
