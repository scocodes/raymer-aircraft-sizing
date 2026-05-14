import numpy as np
class RaymerEquations:
    def __init__(self, raymer_variables):
        self.rvs = raymer_variables
    
    #Raymer Calculations
        self.W_wing = 0.0103*self.rvs.kdw*self.rvs.kvs*(self.rvs.Wto*self.rvs.Nz)**0.5*self.rvs.Sw**0.785*self.rvs.tc_naca6716**-0.4*(1+self.rvs.lambdaa)**0.05*np.cos(0)**-1*self.rvs.Scsw**0.04
        self.W_horizontal_tail = 3.316*(1+(self.rvs.Fw/self.rvs.Bh))**-2*(self.rvs.Wto*self.rvs.Nz/1000)**0.26*self.rvs.Sht**0.806
        self.W_vertical_tail = 0.452*self.rvs.Krht*(1+self.rvs.Ht/self.rvs.Hv)**0.5*(self.rvs.Wto*self.rvs.Nz)**0.488*self.rvs.Svt**0.718*self.rvs.M**0.341*self.rvs.Lt**-1*(1+self.rvs.Sr/self.rvs.Svt)**0.348*self.rvs.Avt**0.223*(1+self.rvs.lambdaa)**0.25*(np.cos(0))**-0.323
        self.W_fuselage = 0.499*self.rvs.kdw*self.rvs.Wto**0.35*self.rvs.Nz**0.25*self.rvs.L*0.5*self.rvs.D**0.849*self.rvs.W**0.685
        self.W_main_landing_gear = self.rvs.Kcb*self.rvs.Ktpg*(self.rvs.Wl*self.rvs.Nl)**0.25*self.rvs.Lm**0.973
        self.W_nose_landing_gear = (self.rvs.Wl/self.rvs.Nl)**0.290*self.rvs.Ln**0.5*self.rvs.Nnw**0.525
        self.W_engine = 0.01*self.rvs.Wen**0.717*self.rvs.Nen*self.rvs.Nz
        self.W_fuel_system = 7.45*self.rvs.Vt**0.47*(1+self.rvs.Vi/self.rvs.Vt)**-0.095*(1+self.rvs.Vp/self.rvs.Vt)*self.rvs.Nt**0.066*self.rvs.Nen**0.052*(self.rvs.T*self.rvs.SFC/1000)**0.249
        self.W_flight_controls = 36.28*self.rvs.M**0.003*self.rvs.Scs**0.489*self.rvs.Ns**0.484*self.rvs.Nc**0.127
        self.W_instruments = 8 + 36.37*self.rvs.Nen**0.676*self.rvs.Nt**0.237 + 26.4*(1+self.rvs.Nci)**1.356
        self.W_hydraulics = 37.23*self.rvs.Kvsh*self.rvs.Nu**0.664
        self.W_electrical = 172.2*self.rvs.Kmc*self.rvs.Rkva**0.152*self.rvs.Nc**0.1*self.rvs.La**0.1*self.rvs.Ngen**0.091
        self.W_avionics = 2.117*self.rvs.Wuav**0.933
        self.W_engines = 2*self.rvs.Wen