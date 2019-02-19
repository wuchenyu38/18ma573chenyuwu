
import numpy as np
import scipy.stats as ss
import math
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
      maturity = self.maturity
      return np.max([0, (s - k)*otype])

'''============
Gbm class inherited from sde_1d
============='''

class Gbm:
    def __init__(self,
                 init_state = 100.,
                 drift_ratio = .0475,
                 vol_ratio = .2
                ):
        self.init_state = init_state
        self.drift_ratio = drift_ratio
        self.vol_ratio = vol_ratio
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
Gbm.bsm_price = bsm_price



def bsm_geometric_asian_price(self,otype,strike,maturity,num_step):
  sigma = self.vol_ratio
  S0 = self.init_state
  r=self.drift_ratio
  miu=r-(1/2)*(sigma**2)
  miu2=miu/2
  sigma2=((sigma**2)*(2*num_step+1))/(6*(num_step+1))
  r2=miu2+(1/2)*(sigma2)
  gbm1=Gbm(init_state=S0,
               drift_ratio=r2,
               vol_ratio = math.sqrt(sigma2))
  option1=VanillaOption(
      otype = otype,       
      strike = strike,                
      maturity = maturity,
      )
  option1.market_price=(math.e**((r2-r)*maturity))*bsm_price(gbm1,option1)
  return (math.e**((r2-r)*maturity))*bsm_price(gbm1,option1)
Gbm.bsm_geometric_asian_price=bsm_geometric_asian_price


def BM_gen(T1,T2,n):
  t=np.linspace(T1,T2,num=n+1)
  W=np.zeros(n+1)
  for i in range(n):
    W[i+1]=W[i]+1./np.sqrt(n)*np.random.normal()
  return t,W

def bsm_arithmetic_asian_exact_sample(self,otype,strike,maturity,num_step,num_path):
    sigma = self.vol_ratio
    s0 = self.init_state
    r=self.drift_ratio
    A=0
    MC_A=[]
    for i in range(num_path):
        t,W=BM_gen(0.,maturity,num_step)
        A=(1/num_step)*(sum(s0*np.exp((r-(1/2)*sigma**2)*maturity+sigma*W))-s0)
        option1=VanillaOption(maturity=maturity,otype=otype,strike=strike)
        MC_A.append(VanillaOption.payoff(option1,A))
    Asion_price=np.exp(-r*maturity)*sum(MC_A)/num_path
    return Asion_price
Gbm.bsm_arithmetic_asian_exact_sample = bsm_arithmetic_asian_exact_sample


