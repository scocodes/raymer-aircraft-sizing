import numpy as np
import matplotlib.pyplot as plt


class MissionAnalysis:
    
    def __init__(self, Wto, raymer_equations, data_import, raymer_variables, conversions):
        self.Wto = Wto
        self.reqs = raymer_equations
        self.data = data_import
        self.revs = raymer_variables
        self.convs = conversions

    """ Mission Analysis and Fuel Burn Iteration """

    #Breuget Range and Endurance Equation 
    def breuget(self, cl ,index):
        "Cruise Cl Calculation"
        L_over_D = self.data.cl_interpolate(cl)
        
        if index == 0:
            cruise_range = self.convs.nmtokm(250) #km
            v_cruise = 623  #km/h
            weight_fract = np.exp(-cruise_range*self.revs.SFC/(v_cruise*(L_over_D)))
            # print(f"Cruise Fraction: {weight_fract}")
        else:
            loiter_time = 1
            weight_fract = np.exp(-loiter_time*self.revs.SFC/L_over_D)
            # print(f"Loiter Fraction: {weight_fract}")

        return weight_fract


    #Fuel Burn from Mass Fractions Calculations
    def fuel_burn (self, Wto, Wf):

        S_wing = 47.01 # Wing area in m^2
        rho_5000_ft = 1.0555 #kg/m^3

        fuel_fractions = {"Engine Warm up":0.990,
                        "Taxi":0.990,
                        "Take-Off":0.995,
                        "Climb":0.96,
                        "Descent":0.990,
                        "Landing, Taxi and Shutdown":0.995}
        
        q_cruise = 0.5*rho_5000_ft*self.convs.kmhtoms(623)**2
        q_loiter = 0.5*rho_5000_ft*self.convs.kmhtoms(450)**2

        cl_cruise = (self.convs.lbtoN(Wto)-(0.4*self.convs.lbtoN(Wf)))/(q_cruise*S_wing)
        cl_loiter = (self.convs.lbtoN(Wto)-(0.4*self.convs.lbtoN(Wf)))/(q_loiter*S_wing)

        Mff = 1

        for fraction in fuel_fractions.values():
            Mff *= fraction
        Mff *= (self.breuget(cl_cruise, 0))**2 * (self.breuget(cl_loiter, 1))

        weight_fuel = (1-Mff)*Wto

        #Fuel reserve margin 
        weight_fuel = 1.1*weight_fuel

        return weight_fuel
        
    #Reference Values from Literature
    MTOW_0 = 50000
    Wf_0 = 10700
    Wp_0 = 14341

    #Main Iteration Engine to Converge on Correct Weights
    def iteration(self, MTOW_l, Wf_l, Wp_l):
        
        total_iterations = 0

        #Convergence Plot Lists

        fuel_list = []
        oew_list = []
        mtow_list = []

        oew_0 = self.reqs.Weight_Calculation(MTOW_l)
        Wf_0 = self.fuel_burn(MTOW_l, Wf_l)
        Total_Weights_0 = oew_0 + Wf_0+ Wp_l
            
        while True:

            total_iterations += 1
            target = 0.01

            new_oew = self.reqs.Weight_Calculation(Total_Weights_0)
            new_fuel = self.fuel_burn(Total_Weights_0, Wf_0)
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




