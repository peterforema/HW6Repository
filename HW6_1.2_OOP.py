#region imports
# Importing classes from HW6_1_OOP.py
from scipy.optimize import fsolve
from HW6_1_OOP import ResistorNetwork, Resistor, VoltageSource, Loop
#endregion

#region Functions
class ResistorNetwork2(ResistorNetwork):
    def __init__(self):
        super().__init__()

    def AnalyzeCircuit(self):
        i0 = [0.1, 0.1, 0.1]  # Initial guess for the currents in the circuit
        i = fsolve(self.GetKirchoffVals, i0)
        print("I1 = {:0.1f}".format(i[0]))
        print("I2 = {:0.1f}".format(i[1]))
        print("I3 = {:0.1f}".format(i[2]))
        return i

    def GetKirchoffVals(self, i):
        self.GetResistorByName('ad').Current = i[0]
        self.GetResistorByName('bc').Current = i[0]
        self.GetResistorByName('cd').Current = i[2]
        self.GetResistorByName('ce').Current = i[1]
        Node_c_Current = sum([i[0], i[1], -i[2]])

        KVL = self.GetLoopVoltageDrops()
        KVL.append(Node_c_Current)
        return KVL

# Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
    """
    Net = ResistorNetwork2()  # Instantiate a resistor network object of the derived class
    Net.BuildNetworkFromFile("ResistorNetwork_2.txt")  # Call the function from Net that builds the resistor network from a text file
    IVals = Net.AnalyzeCircuit()
#endregion

#region function calls
if __name__ == "__main__":
    main()
#endregion


#stem code from Prof Smay's GIThub