#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:26:30 2019
@author: songqsh
"""

import numpy as np
import matplotlib.pyplot as plt

'''=========
option class init
=========='''
class VanillaOption:
    def __init__(
        self,
        otype = 1, # 1: 'call'
                  # -1: 'put'
        strike = 110.,
        maturity = 1.,
        market_price = 10.):
      self.otype = otype
      self.strike = strike
      self.maturity = maturity
      self.market_price = market_price #this will be used for calibration
      
        
    def payoff(self, s): #s: excercise price
      otype = self.otype
      k = self.strike
      return np.max([0, (s - k)*otype])
  

if __name__ == '__main__':
    #create option instance, maturity is just arbitrarily given
    option1 = VanillaOption(otype = 1, strike = 40, maturity= 1., market_price=38.) 
    ss = np.arange(20,61) #exercise price
    
    payoff = [option1.payoff(s) for s in ss] #compute payoff
    plt.plot(ss, payoff)
    plt.xlabel('exercise price')
    plt.ylabel('payoff')
    plt.title('40-strike call');
   
