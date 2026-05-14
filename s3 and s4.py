# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Metres to Feet
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

"""Class II Raymer Weight Estimation"""

def raymer(Wto):

    #Raymer Variables List
    kdw = 1 #Delta Wing Parameter, 0.768 for a delta wing, 1 otherwise
    kvs = 1 #1.19 For variable sweep wing, 1 otherwise
    Nz = 11.25  #1.5*ultimate load factor
    Nl = 3  # Ultimate landing loading factor Ngear x 1.5 
    Sw = 544.44 # Trapezoidal wing areas
    tc_naca6716 = 0.16
    lambdaa = 0.898
    Scsw = 40.72 #Control Surface main wing area 
    Fw = 3 #Fuselage width at horizontal tail intersection ft 
    Bh = 18.37  #Hortizontal Tail span
    Sht = 89.45 #Hortizontal tail area
    Krht = 1    #1.047 for rollinh tail, 1 otherwise
    Ht = 0  #0 for a conventional tail, 1 for a t tail
    Hv = 8.2    #Vertical tiail height about fuselage   
    Svt = 83.96 #Vertial Tail area
    M = 0.58    #Mach number at cruise
    Lt = 14.72-(6.7-1.5)    #Tail length
    Sr = 23.47  #Rudder area
    Avt = 1.08  #Aspect Rtaio for the vertical tail
    Kcb = 1 #2.25 for ross beam, 1 otherwise
    Ktpg = 0.826    #0.826 for tripod, 1 otherwise 
    Wl = 0.85*Wto   #Landing design gross weight 0.85*Wdg
    Nc = 1  #Number of Crew
    Lm = 70.87 #Length of main landing gear inch
    Ln = 74.80 #Nose gear length inch
    Nnw = 1 #Number of nose wheels 
    Nen = 2 #Number of engines
    Wen = 1440 #engine weight lb
    T = 9065*2  #Total engine thrust lb
    Vt = 1642 #total fuel volume gal
    Vi = Vt#integral tanks volume, gal
    Vp = Vt #self sealing tankls volume, gal
    Scs = Scsw + 15.98 #Total control surfaces area
    Ns =  3  #Number of flight control systems
    Nci = 1 #1 if single pilot, 1.2 if pilot plus backseater, 2 if pilot and copassenger
    Kvsh = 1        #1.425 for variable sweep wing, 1 ogtherwise
    Nu = 10 #number of hydraulic utility functions (5-15)
    Kmc = 1.45  #1.45 if mission completion required after failure, 1 otherwise
    Rkva = 130 #system rating kv (110-160)
    La = 1.5*53.35 #electrical routing distance from generators to avionics to cockpit in ft
    Ngen = Nen  #Number of generators
    Wuav = 1200 #Uninstalled aviatonics mas (800-1400lb)
    L = m2f(16.26)
    D = m2f(2.1)
    W = m2f(1.3)
    Nt = 4  #Number of generators
    SFC = 0.371 #Specific fuel consumption

    #Raymer Calculations
    W_wing = 0.0103*kdw*kvs*(Wto*Nz)**0.5*Sw**0.785*tc_naca6716**-0.4*(1+lambdaa)**0.05*np.cos(0)**-1*Scsw**0.04
    W_horizontal_tail = 3.316*(1+(Fw/Bh))**-2*(Wto*Nz/1000)**0.26*Sht**0.806
    W_vertical_tail = 0.452*Krht*(1+Ht/Hv)**0.5*(Wto*Nz)**0.488*Svt**0.718*M**0.341*Lt**-1*(1+Sr/Svt)**0.348*Avt**0.223*(1+lambdaa)**0.25*(np.cos(0))**-0.323
    W_fuselage = 0.499*kdw*Wto**0.35*Nz**0.25*L*0.5*D**0.849*W**0.685
    W_main_landing_gear = Kcb*Ktpg*(Wl*Nl)**0.25*Lm**0.973
    W_nose_landing_gear = (Wl/Nl)**0.290*Ln**0.5*Nnw**0.525
    W_engine = 0.01*Wen**0.717*Nen*Nz
    W_fuel_system = 7.45*Vt**0.47*(1+Vi/Vt)**-0.095*(1+Vp/Vt)*Nt**0.066*Nen**0.052*(T*SFC/1000)**0.249
    W_flight_controls = 36.28*M**0.003*Scs**0.489*Ns**0.484*Nc**0.127
    W_instruments = 8 + 36.37*Nen**0.676*Nt**0.237 + 26.4*(1+Nci)**1.356
    W_hydraulics = 37.23*Kvsh*Nu**0.664
    W_electrical = 172.2*Kmc*Rkva**0.152*Nc**0.1*La**0.1*Ngen**0.091
    W_avionics = 2.117*Wuav**0.933
    W_engines = 2*Wen

    Weights = {"Wing":W_wing, "Horizontal Tail":W_horizontal_tail, "Vertical Tail":W_vertical_tail, 
            "Fuselage":W_fuselage, "Main Landing Gear":W_main_landing_gear, "Nose Landing Gear":W_nose_landing_gear,
            "Engine Weight": W_engines, "Engine Section":W_engine, "Fuel System":W_fuel_system, 
            "Flight Controls":W_flight_controls, "Instruments":W_instruments, "Hydraulics":W_hydraulics, 
            "Electrical":W_electrical, "Avionics":W_avionics}

    #Design Weight Calculation

    for name, value in Weights.items():
        print(f"{name}: {value:.2f} lb")
    print(" ")

    oew =  sum(Weights.values())
    return oew
    

""" Mission Analysis and Fuel Burn Iteration """

#Importing OpenVSP L/D values at given Cl
df = pd.read_excel("optimum clld.xlsx")
df = df.sort_values(by="cl")

section2_cl = df["cl"]
section2_ld = df["ld"]

def cl_ld_values():
    cls = [0.2, 0.3, 0.4, 0.5, 0.6]
    for c in cls:
        L_over_D = np.interp(c, section2_cl, section2_ld)
        print(f"{L_over_D:.1f}")




#Breuget Range and Endurance Equation 
def breuget(cl, index):
    "Cruise Cl Calculation"
    L_over_D = np.interp(cl, section2_cl, section2_ld)
    SFC = 0.371 #Specific fuel consumption (1/hr)
    
    if index == 0:
        cruise_range = nmtokm(250) #km
        v_cruise = 623  #km/h
        weight_fract = np.exp(-cruise_range*SFC/(v_cruise*(L_over_D)))
        # print(f"Cruise Fraction: {weight_fract}")
    else:
        loiter_time = 1
        weight_fract = np.exp(-loiter_time*SFC/L_over_D)
        # print(f"Loiter Fraction: {weight_fract}")

    return weight_fract


#Fuel Burn from Mass Fractions Calculations
def fuel_burn (Wto, Wf):
    S_wing = 47.01 # Wing area in m^2
    rho_5000_ft = 1.0555 #kg/m^3

    fuel_fractions = {"Engine Warm up":0.990,
                      "Taxi":0.990,
                      "Take-Off":0.995,
                      "Climb":0.96,
                      "Descent":0.990,
                      "Landing, Taxi and Shutdown":0.995}
    
    q_cruise = 0.5*rho_5000_ft*kmhtoms(623)**2
    q_loiter = 0.5*rho_5000_ft*kmhtoms(450)**2

    cl_cruise = (lbtoN(Wto)-(0.4*lbtoN(Wf)))/(q_cruise*S_wing)
    cl_loiter = (lbtoN(Wto)-(0.4*lbtoN(Wf)))/(q_loiter*S_wing)

    Mff = 1

    for fraction in fuel_fractions.values():
        Mff *= fraction
    Mff *= (breuget(cl_cruise, 0))**2 * (breuget(cl_loiter, 1))

    weight_fuel = (1-Mff)*Wto

    #Fuel reserve margin 
    weight_fuel = 1.1*weight_fuel

    return weight_fuel
    
#Reference Values from Literature
MTOW_0 = 50000
Wf_0 = 10700
Wp_0 = 14341

#Main Iteration Engine to Converge on Correct Weights
def iteration(MTOW_l, Wf_l, Wp_l):
    
    total_iterations = 0

    #Convergence Plot Lists

    fuel_list = []
    oew_list = []
    mtow_list = []

    oew_0 = raymer(MTOW_l)
    Wf_0 = fuel_burn(MTOW_l, Wf_l)
    Total_Weights_0 = oew_0 + Wf_0+ Wp_l
        
    while True:

        total_iterations += 1
        target = 0.01

        new_oew = raymer(Total_Weights_0)
        new_fuel = fuel_burn(Total_Weights_0, Wf_0)
        new_total_weights = new_oew + new_fuel + Wp_l

        error = np.abs(((new_total_weights-Total_Weights_0)/new_total_weights)*100)
        fuel_error = np.abs(((new_fuel-Wf_0)/new_fuel)*100)
        oew_error = np.abs(((new_oew-oew_0)/new_oew)*100)

        fuel_list.append(fuel_error)
        oew_list.append(oew_error)
        mtow_list.append(error)

        Total_Weights_0 = new_total_weights
        Wf_0 = new_fuel
        oew_0 = new_oew

        
        if error < target:

            print(f"Design Weight: {new_oew:.2f}")
            print(f"Fuel Weight: {new_fuel:.2f}")
            print(f"Total Weight: {new_total_weights:.2f}")

            print(f"Total Iterations to Converge: {total_iterations}")
            print(f"Error Percentage of {error:.2f} %")

            x_axis = []
            for i in range(total_iterations):
                x_axis.append(i+1)
            
            plt.plot(x_axis, fuel_list, label="Fuel Weight")
            plt.plot(x_axis, oew_list, label="OEW Weight")
            plt.plot(x_axis, mtow_list, label="MTOW Weight")

            plt.ylabel("Error (%)")
            plt.xlabel("Number of Iterations")
            plt.legend()
            plt.grid()
            plt.show()

            break


iteration(50000, 10700, 14341) 

