#!usr/bin/env python
__author__ = "Xiaoguang Zhang"
__email__ = "xzhang@westwoodrobotics.net"
__copyright__ = "Copyright 2020 Westwood Robotics"
__date__ = "Jan 8, 2020"
__version__ = "0.0.1"
__status__ = "Prototype"

class ESC(object):

    def __init__(self, name, freq, duty_max, duty_min):
        self.name = name
        self.freq = freq
        self.duty_max = duty_max
        self.duty_min = duty_min