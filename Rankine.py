from Steam import steam1

class rankinee:
    """
    The Rankine class analyzes Rankine power cycles.
    """
    def __init__(self, p_low=8, p_high=8000, T1=None, x1=None, name=None):
        '''
        Constructor for Rankine power cycle
        :param p_low: low pressure isobar for the cycle in kPa
        :param p_high: high pressure isobar for the cycle in kPa
        :param T1: temperature for State 1 (turbine inlet) in degrees C
        :param x1: quality of steam at State 1
        :param name: a convenient name for the cycle
        '''
        self.p_low = p_low
        self.p_high = p_high
        self.T1 = T1
        self.x1 = x1
        self.name = name
        self.efficiency = None
        self.turbine_work = 0
        self.pump_work = 0
        self.heat_added = 0
        self.state1 = None
        self.state2 = None
        self.state3 = None
        self.state4 = None

    def calc_efficiency(self):
        # Calculate the states
        self.state1 = steam(self.p_high, T=self.T1, x=self.x1, name='Turbine Inlet')
        self.state2 = steam(self.p_low, s=self.state1.s, name='Turbine Exit')
        self.state3 = steam(self.p_low, x=0, name='Pump Inlet')  # Calculate v for state3
        self.state4 = steam(self.p_high, h=self.state3.h + self.state3.v * (self.p_high - self.p_low), name='Pump Exit')

        # Calculate work and heat added
        self.turbine_work = self.state1.h - self.state2.h
        self.pump_work = self.state4.h - self.state3.h
        self.heat_added = self.state1.h - self.state4.h

        # Calculate efficiency
        self.efficiency = 100.0 * (self.turbine_work - self.pump_work) / self.heat_added
        return self.efficiency

    def print_summary(self):
        """
        Prints a summary of the Rankine cycle.
        """
        if self.efficiency is None:
            self.calc_efficiency()
        print('Cycle Summary for:', self.name)
        print('\tEfficiency: {:.3f}%'.format(self.efficiency))
        print('\tTurbine Work: {:.3f} kJ/kg'.format(self.turbine_work))
        print('\tPump Work: {:.3f} kJ/kg'.format(self.pump_work))
        print('\tHeat Added: {:.3f} kJ/kg'.format(self.heat_added))
        self.state1.print()
        self.state2.print()
        self.state3.print()
        self.state4.print()
