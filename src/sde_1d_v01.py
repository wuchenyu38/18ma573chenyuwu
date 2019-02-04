
# coding: utf-8

# # Euler on 1d SDE
# ## General 1d SDE

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from contract_v01 import VanillaOption
# In[2]:


'''=========
sde class init
=========='''

class Sde_1d:
    def __init__(self,
                init_state = 0.,
                drift = lambda x: 0,
                vol = lambda x: 1.
                ):
        self.init_state = init_state
        self.drift = drift
        self.vol = vol
        


# In[3]:


'''================
euler_1d_difference 
input:
    xh_i:  current state
    dt: time diff
    dw: bm increase
output:
    xh_i_diff: increase for euler solution
=================='''

def euler_1d_diff(self, xh_i, dt, dw):
    #set SDE param
    mu = self.drift
    sigma = self.vol
    
    return mu(xh_i)*dt + sigma(xh_i)*dw

Sde_1d.euler_diff = euler_1d_diff




'''============
Gbm class inherited from sde_1d
============='''

class Gbm_1d(Sde_1d):
    def __init__(self,
                 init_state = 100.,
                 drift_ratio = .0475,
                 vol_ratio = .2
                ):
        self.init_state = init_state
        
        self.drift_ratio = drift_ratio
        self.vol_ratio = vol_ratio
        
        self.drift = lambda x: drift_ratio*x
        self.vol = lambda x: vol_ratio*x


'''========
Black-Scholes-Merton formula. 
=========='''

def bsm_price(self, vanilla_option):
    s0 = self.init_state
    sigma = self.vol_ratio
    r = self.drift_ratio
    
    otype = vanilla_option.otype
    k = vanilla_option.strike
    maturity = vanilla_option.maturity
    
    d1 = (np.log(s0 / k) + (r + 0.5 * sigma ** 2) 
          * maturity) / (sigma * np.sqrt(maturity))
    d2 = d1 - sigma * np.sqrt(maturity)
    
    return (otype * s0 * ss.norm.cdf(otype * d1) #line break needs parenthesis
            - otype * np.exp(-r * maturity) * k * ss.norm.cdf(otype * d2))

Gbm_1d.bsm_price = bsm_price        









# In[5]:

if __name__ == '__main__':       
    '''============
    test:
        plot Gbm paths
    =============='''
    gbm1 = Gbm_1d(init_state=10., drift_ratio=.03, vol_ratio=.25)
    grid = np.linspace(0,1,100)
    
    plt.figure()
    plt.title('test Gbm_1d.euler')
    plt.xlabel('time')
    plt.ylabel('state')
    for i in range(5):
        xh = gbm1.euler(grid)
        plt.plot(grid, xh)
        
        
            
    '''===============
    Test bsm_price
    ================='''
    gbm1 = Gbm_1d(init_state=100., drift_ratio=.0475, vol_ratio=.2)
    option1 = VanillaOption(otype = 1, strike = 110., maturity= 1., market_price=15.) 
    
    print('>>>>>>>>>>call value is ' + str(gbm1.bsm_price(option1)))
    option2 = VanillaOption(otype=-1)
    print('>>>>>>>>>>put value is ' + str(gbm1.bsm_price(option2)))    

