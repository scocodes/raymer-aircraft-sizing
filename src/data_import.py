import pandas as pd
import numpy as np

class Data:
    def __init__(self):
        self.df = pd.read_excel("data/optimum clld.xlsx")
        self.df = self.df.sort_values(by="cl")
        self.section2_cl = self.df["cl"]
        self.section2_ld = self.df["ld"]

    def cl_ld_values(self):
        cls = [0.2, 0.3, 0.4, 0.5, 0.6]
        for c in cls:
            L_over_D = np.interp(c, self.section2_cl, self.section2_ld)
            print(f"{L_over_D:.1f}")

    def cl_interpolate(self, cl):
        return np.interp(cl, self.section2_cl, self.section2_ld)

