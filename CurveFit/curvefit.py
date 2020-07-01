"""
CurveFit 
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import sympy as sp
import re

#local import
import cftools as cft
version = '1.0.0'




class Curve_fit:
    
    
    def __init__ (self, x0 = None, y0 = None, name = None , path = None, id=None):
        self.name = name
        self.path = path
        self.x0 = x0; self.y0 = y0
        if type(x0) == list: self.x0 = np.array(x0)
        if type(y0) == list: self.y0 = np.array(y0)
        if type(x0) == type(None) or type(y0) == type(None):
            try:
                self.x0,self.y0 = np.loadtxt(self.path).T
            except:
                self.x0,self.y0 = np.array(re.findall(r'(\d*\.?\d*)[\t,]+(\d*\.?\d*)', cft.read(self.path)),dtype=float).T
        if not self.name and self.path: 
            self.name = cft.path_info(self.path)[1].strip() #File Name
            self.name_value = cft.get_the_var_value_from_the_file_name(self.name)
        
        #Copy
        self.x, self.y = self.x0.copy(), self.y0.copy()

        #Initailizations
        self.fitted = False  
        
        # ID is used with Curve_fit_systemGUI
        self.id = id
    
    def fit(self, expr:str, p0:dict, var:str = 'x'):
        self.expr = expr
        self.p0 = p0
        self.var = var
        self.fun = sp.sympify(self.expr)
        self.fun = sp.lambdify([self.var] + list(self.p0.keys()), self.fun)        
        self.pfit, self.pcov = optimize.curve_fit(self.fun, self.x, self.y, list(self.p0.values()))
        self.perr = np.sqrt(np.diag(self.pcov))

        self.fitted = True
        
        
        
        
    def limit(self,a,b):
        self.x, self.y = cft.chose_range_xy(self.x0,self.y0, a, b)
    
    
    def plot(self, axes = None):
        assert self.pfit.any()

        if axes == None:
            fig = plt.figure()
            axes = fig.add_subplot(111)

        self.xf = np.linspace(self.x[0], self.x[-1], self.x.size * 2)
        self.yf = self.fun(self.xf, *list(self.pfit))
        
        axes.plot(self.x,self.y, '.k', label = 'Data')
        axes.plot(self.xf, self.yf, '-', label = 'Fited Data')
        
        axes.legend()
        #plt.show()
        
    
    def show(self, axes = None):
        if axes == None:
            fig = plt.figure()
            axes = fig.add_subplot(111)

        axes.plot(self.x,self.y)
        #plt.show()
    
    def fitted_data(self, save = False, path = None):
        try: 
            fitted_d = np.array([self.xf, self.yf]).T
        except AttributeError:
            self.xf = np.linspace(self.x[0], self.x[-1], self.x.size * 2)
            self.yf = self.fun(self.xf, *list(self.pfit))
            fitted_d = np.array([self.xf, self.yf]).T
            
        if save:
            np.savetxt(path, fitted_d)
        
        