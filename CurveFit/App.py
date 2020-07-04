import os
import tkinter as tk
from tkinter import filedialog
import sympy as sp
import pandas as pd
import warnings

from curvefit import Curve_fit
from MainGUI import GUI

__version__='1.0.1'  # Local verion (App.py)
version = "1.0.2"    # Global Version (CurveFit project)


class App(Curve_fit, GUI):
    
    def __init__(self, root):
        # Creat the GUI
        GUI.__init__(self, root)
        
        self.connect()
        
        
        self.app_started = False
        
        warnings.filterwarnings("error")
    
    def connect(self,):
        self.b_load_files['command'] = self.press_load_data
        #self.b_ok['command'] = self.press_ok
        self.b_fit['command'] = self.press_fit
        self.b_next['command'] = self.press_next
        self.b_back['command'] = self.press_back
        self.b_del['command'] = self.press_del
        
        self.b_fo_exp['command'] = lambda: self.insert_formula('exp')
        self.b_fo_gaussian['command'] = lambda: self.insert_formula('gaussian')
        self.b_fo_wave['command'] = lambda: self.insert_formula('wave')
        self.b_fo_poly['command'] = lambda: self.insert_formula('poly')
        self.b_fo_custom['command'] = lambda: self.insert_formula('custom')
        
        
    def press_load_data(self):
        self.select_files()
        self.start_app()
        
    def start_app(self,):
        self.clear_app()
        self.initate_fittings()
        self.app_started = True
        
    def clear_app(self):
        self.axes.cla()
        self.mini_axes.cla()
        self.b_ok['text'] = 'Ok'
        self.b_ok['fg'] = 'green'
        self.b_ok['command'] = self.press_ok
            
        if self.app_started:
            for lg, e, lc in self.tabel_elements.values():
                lc.grid_forget()
                lg.grid_forget()
                e.grid_forget()

    def initate_fittings(self):
        self.fittings = [Curve_fit(path = p, id=ID+1) for ID, p in enumerate(self.filenames)]
        for fit in self.fittings:
            fit.show(self.axes)
        self.fittings_size = len(self.fittings)
        self.fitting_index = -1 # so it starts from zero, 1 + (-1) = 0
        self.canvas.draw()
        self.mini_canvas.draw()

        
    def press_ok(self): 
        self.switch_to_restart()
        self.first_fit_guess()
        
        self.select_fitting(d=1)        
        self.plot()
            
    def switch_to_restart(self):
        self.b_ok['text'] = 'Restart'
        self.b_ok['fg'] = 'red'
        self.b_ok['command'] = self.start_app        
        
    
    def first_fit_guess(self,):
        self.formula = self.formula_text.get().replace('X','x').replace('^', '**')
        self.parameters = [str(s) for s in sp.simplify(self.formula).free_symbols if str(s)!='x']
        self.parameters_guess = {par : 1 for par in self.parameters}
        
        self.generate_tabel(self.parameters)
        
        self.fitted_parameters_dict = {'parameters': self.parameters}
        for self.fitting in self.fittings:
            try:
                self.fitting.fit(expr=self.formula, p0=self.parameters_guess)
                self.add_to_fitted_parameters_dict()
            except:
                continue
            
        self.update_status(msg='CurveFit is Trying to Fit All!')
        
    
    def add_to_fitted_parameters_dict(self):
        if not str(self.fitting.name_value).replace('.','').isdigit():
            self.fitting.name_value = str(self.fitting.id)
        
        self.fitted_parameters_dict[self.fitting.name_value] = self.fitting.pfit
        self.mini_plot()
            
            
    def select_fitting(self, d): # To select fitting from fitting
        self.fittings_size = len(self.fittings)

        if (d == 1 and self.fitting_index == self.fittings_size - 1): # Last fitting
            self.fitting_index = 0 # start again
        elif d == -1 and self.fitting_index == 0: # going back from first fitting
            self.fitting_index = self.fittings_size - 1 # Go to the last fitting
        else:
            self.fitting_index += d
        self.fitting = self.fittings[self.fitting_index]
        
        self.update_status()
            

    def press_fit(self, d=0):
        self.get_data_from_tabel()
        
        from_ = self.e_from.get()
        to = self.e_to.get()
        if from_.replace('.','').isdigit() and to.replace('.','').isdigit():
            self.fitting.limit(float(from_), float(to))
        try:
            self.fitting.fit(expr=self.formula, p0=self.parameters_guess, var='x')
            self.add_to_fitted_parameters_dict()
        except Exception as e:
            print(f'Error! {e}')
            self.error_msg=e
            
        self.show_fit_at_tabel()
        self.plot()
        
        self.update_status()
        
    def get_data_from_tabel(self, ):
        for const in self.parameters_guess:
            guess = self.tabel_elements[const][1].get()
            if guess:
                guess = float(guess)
            else:
                last_fit = self.tabel_elements[const][0]['text']
                if last_fit.replace('.','').isdigit():
                    guess = float(last_fit)
                else:
                    guess = 1
            self.parameters_guess[const] = guess
        
    def show_fit_at_tabel(self,):
        for i, const in enumerate(self.parameters):
            try:
                self.tabel_elements[const][0]['text'] = str(round(self.fitting.pfit[i],3))
            except:
                self.tabel_elements[const][0]['text'] = "Guess again!"
    
    def press_next(self):
        self.select_fitting(d=1)        
        self.plot()
        
        
    def press_back(self,):
        self.select_fitting(d=-1)        
        self.plot()
        
    def plot(self):
        self.axes.cla()
        if self.fitting.fitted == True:
            self.fitting.plot(self.axes)
            self.show_fit_at_tabel()
        else:
            self.fitting.show(self.axes)
        self.axes.set_title(self.fitting.name)
        self.canvas.draw()
        
    def mini_plot(self):
        self.mini_axes.cla()
        self.generate_tabel_fit()
        
        for par in self.tabel_fit:
            if par != 'File' and par[0].isupper():
                self.mini_axes.plot(self.tabel_fit['File'], self.tabel_fit[par], label=par)
        self.mini_axes.legend(loc=0)
        self.mini_canvas.draw()
    
    def press_del(self):
        try:
            self.fittings.remove(self.fitting)
            self.fittings_size = len(self.fittings)
        except:
            self.update_status(msg='All Files were deleted! Load them Again')
        
        if self.fittings_size == 0:
            self.clear_app()
            self.update_status(msg='All Files were deleted!')
            self.canvas.draw()
            self.switch_to_restart()
            del self.fitting
        else:
            self.select_fitting(d=-1)
            self.plot()
            self.mini_plot()
        
    def press_save(self):
        self.save_path = filedialog.askdirectory(title='Select Folder to save your Results at')
        print(self.save_path)
        if self.save_path:
            self.save_table()
            self.save_fit_data()
            self.update_status(msg='The Fitting is Saved at: {}'.format(self.save_path))
        else:
            self.update_status(msg='The Fitting is NOT saved!')
        
            
    def save_table(self,):
        self.generate_tabel_fit()
        self.export_tabel_to_csv()
    
    def save_fit_data(self):
        for fit in self.fittings:
            fit.fitted_data(save=True, path=os.path.join(self.save_path, fit.name+'.txt')) 
    
    def save_figs(self):
        pass
    
    def generate_tabel_fit(self):
        self.tabel_fit = {par:[] for par in self.parameters}
        self.tabel_fit['File'] = []
        for fit in self.fittings:
            if fit.fitted:
                self.tabel_fit['File'].append(fit.name_value)
                for i, par in enumerate(self.parameters):
                    self.tabel_fit[par].append(fit.pfit[i])
    
    def export_tabel_to_csv(self):
        df = pd.DataFrame(self.tabel_fit)
        df = df[['File', *self.parameters]]
        
        df.to_csv(os.path.join(self.save_path, 'Results.csv'))
        
    
    def update_status(self, msg=''):
        if msg:
            self.msg = msg
        else:
            self.msg =f"File index number: {self.fitting_index + 1}\nError: {self.error_msg}" 
        
        self.l_status['text'] = self.msg
        #self.l_status.grid(column=0, row=0, sticky='NW')
        
        if self.fittings_size:
            self.calculate_progress()
        else:
            self.progress_bar['value'] = 0
        
    def calculate_progress(self):
        progress = 0
        for fit in self.fittings:
            if fit.fitted:
                progress += 1
        progress_value = progress * 100 / self.fittings_size
        self.progress_bar['value'] = progress_value
        self.error_msg='None'
        if progress_value == 100:
            self.b_ok['text'] = 'Save'
            self.b_ok['fg'] = 'green'
            self.b_ok['command'] = self.press_save
        
    
    def insert_formula(self, fo):
        fo_dict = {
            "poly": "A*x**3 + B*x**2 + c*x + d",
            "wave": "a*sin(W1*x) + b*cos(W2*x) + c",
            "exp": "a*exp(G*x) + bg",
            "gaussian": "a*exp(-( (x-b)/C )**2) + d",
            "custom": ""
            }
        
        self.formula_text.delete(0, 'end')
        self.formula_text.insert(0, fo_dict[fo])
        
    
    
        
        
    
    
    
    
    
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
