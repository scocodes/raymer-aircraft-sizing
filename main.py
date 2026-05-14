from src.mission_analysis import MissionAnalysis
from src.conversions import Conversions
from src.data_import import Data
from src.raymer_equations import RaymerEquations
from src.raymer_variables import RaymerVariables

def main(mtow, mf, pl):
    conv = Conversions()
    data = Data()
    RVar = RaymerVariables(conv, mtow)
    REqs = RaymerEquations(RVar)
    missions = MissionAnalysis(mtow, REqs, data, RVar, conv)
    missions.iteration(mtow, mf, pl)


main(50000, 10700, 14341) 
