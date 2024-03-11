import numpy as np
from scipy.interpolate import griddata

class steam1:
    """
    The steam class is used to find thermodynamic properties of steam along an isobar.
    The Gibbs phase rule tells us we need two independent properties in order to find
    all the other thermodynamic properties. Hence, the constructor requires pressure of
    the isobar and one other property.
    """
    def __init__(self, pressure, T=None, x=None, v=None, h=None, s=None, name=None):
        """
        Constructor for steam
        :param pressure: pressure in kPa
        :param T: Temperature in degrees C
        :param x: quality of steam x=1 is saturated vapor, x=0 is saturated liquid
        :param v: specific volume in m^3/kg
        :param h: specific enthalpy in kJ/kg
        :param s: specific entropy in kJ/(kg*K)
        :param name: a convenient identifier
        """
        #assign arguments to class properties
        self.p = pressure #pressure - kPa
        self.T = T #Temperature - degrees C
        self.x = x #quality
        self.v = v #specific volume - m^3/kg
        self.h = h #specific enthalpy - kj/kg
        self.s = s #entropy - kj/(kg*K)
        self.name = name #a useful identifier
        self.region = None #'superheated' or 'saturated' or 'two-phase'
        if T is None and x is None and v is None and h is None and s is None:
            return
        else:
            self.calc()

    def calc(self):
        '''
        The Rankine cycle operates between two isobars (i.e., p_high (Turbine inlet state 1) & p_low (Turbine exit state 2)
        So, given a pressure, we need to determine if the other given property puts
        us in the saturated or superheated region.
        :return: nothing returned, just set the properties
        '''
        # implementation of the calc() method
        pass  # You need to implement this method according to your requirements

    def print(self):
        """
        This prints a nicely formatted report of the steam properties.
        :return: nothing, just prints to screen
        """
        print('Name:', self.name)
        if self.x < 0.0:
            print('Region: compressed liquid')
        else:
            print('Region:', self.region)
        print('p = {:.2f} kPa'.format(self.p))
        if self.x is not None and self.x >= 0.0:
            print('T = {:.1f} degrees C'.format(self.T))
        print('h = {:.2f} kJ/kg'.format(self.h))
        if self.x is not None and self.x >= 0.0:
            print('s = {:.4f} kJ/(kg K)'.format(self.s))
            if self.region == 'Saturated':
                print('v = {:.6f} m^3/kg'.format(self.v))
            if self.region == 'Saturated':
                print('x = {:.4f}'.format(self.x))
        print()
