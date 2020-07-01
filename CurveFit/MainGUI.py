import tkinter as tk
import tkinter.font
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

__version__ = '1.0.0'

class GUI:
    
    def __init__(self, root, geometry=''):
        self.root = root
        if not geometry:
            w = root.winfo_screenwidth()
            h = root.winfo_screenheight()
            geometry=f"{int(w*0.85)}x{int(h*0.8)}"
        self.root.geometry(geometry)
        self.root.title('CurveFit')
        self.root.iconbitmap(r"curvefit_logo_icon.ico")
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.big_font = tk.font.Font(size=12, weight='bold')
        self.norm_font = tk.font.Font(size=10)
        
        self.generate_frames()
        
        self.generate_file()
        self.generate_formula()
        self.generate_limit()  # under tabel_frame
        #self.generate_tabel()  # initiated under app.py
        self.generate_mini_figure()
        self.generate_status()
        self.generate_control()
        self.generate_figure()
        
        self.grid()
        
        
    
    def generate_frames(self):
        self.rfram = tk.Frame(self.root) 
        self.rfram.grid(column=0, row=0, sticky="NSEW", padx=20, pady=20)
        
        self.file_frame = tk.LabelFrame(self.rfram, text='Files')
        self.tabel_frame = tk.LabelFrame(self.rfram, text="Table")
        self.mini_figure_frame = tk.LabelFrame(self.rfram, text='Mini Figure')
        self.formula_frame = tk.LabelFrame(self.rfram, text="Formula")
        self.status_frame = tk.LabelFrame(self.rfram, text='Status')
        self.control_frame = tk.LabelFrame(self.rfram, text="Control")
        self.figure_frame = tk.LabelFrame(self.rfram, text='Figure')
        
    def grid(self):
        self.file_frame.grid(column=0, row=0, columnspan=2, rowspan=1, ipadx=20, ipady=10, padx=10, pady=5, sticky='NWES')
        self.formula_frame.grid(column=3, row=0, columnspan=4, rowspan=1, ipadx=10, ipady=10, padx=20, pady=5,sticky='NWES')
        self.tabel_frame.grid(column=0, row=1, columnspan=2, rowspan=3, ipadx=20, ipady=10, padx=10, pady=5, sticky='NWES')
        self.mini_figure_frame.grid(column=0, row=4, columnspan=2, rowspan=3, ipadx=5, ipady=5, padx=10, pady=5, sticky='NWES')
        self.status_frame.grid(column=5, row=6, columnspan=3, rowspan=2, ipadx=2, ipady=2, padx=10, pady=5, sticky='NWES')
        self.control_frame.grid(column=3, row=6, columnspan=2, rowspan=1, ipadx=20, ipady=15, padx=10, pady=5, sticky='NWES')
        self.figure_frame.grid(column=2, row=1, columnspan=6, rowspan=5, ipadx=20, ipady=15, padx=10, pady=5, sticky='NWES')
        self.figure_frame.columnconfigure(1, weight=1)
        
        for i in range(10) :
            self.rfram.columnconfigure(i, weight=1)
            self.rfram.rowconfigure(i, weight=1)
        
    def generate_file(self):
        self.b_load_files = tk.Button(self.file_frame, text='Load Data', width=8, height=2, font=self.big_font)
        self.b_load_files.grid(column=0, row=0, padx=20, pady=10, sticky='NWES')
        
        self.b_ok = tk.Button(self.file_frame, text='OK', width=8, height=2, font=self.big_font)
        self.b_ok.grid(column=1, row=0, padx=20, pady=10, sticky='NWES')

        for i in range(2) :
            self.file_frame.columnconfigure(i, weight=1)
            self.file_frame.rowconfigure(i, weight=1)
        
    def select_files(self):
        self.filenames = filedialog.askopenfilenames(title='Select all Data Files', filetypes=(('txt Files', '*.txt'),('CSV files','.csv')))
        
        
    def generate_formula(self):
        self.formula_text = tk.Entry(self.formula_frame, width=50, bg='white', font=self.big_font)
        self.formula_text.grid(column=0, row=0, columnspan=5, ipady=12)
        self.formula_text.insert(0, 'A*x + b')
        
        self.b_fo_exp = tk.Button(self.formula_frame, text="Exp / Decay", width=10, height=1, font=self.norm_font,)
        self.b_fo_gaussian = tk.Button(self.formula_frame, text="Gaussian", width=10, height=1, font=self.norm_font)
        self.b_fo_wave = tk.Button(self.formula_frame, text="Wave", width=9, height=1, font=self.norm_font)
        self.b_fo_poly = tk.Button(self.formula_frame, text="Polynomials", width=10, height=1, font=self.norm_font)
        self.b_fo_custom = tk.Button(self.formula_frame, text="Custom", width=10, height=1, font=self.norm_font)
        
        self.b_fo_exp.grid(column=0, row=1, padx=4, pady=10)
        self.b_fo_gaussian.grid(column=1, row=1, padx=4, pady=10)
        self.b_fo_wave.grid(column=2, row=1, padx=4, pady=10)
        self.b_fo_poly.grid(column=3, row=1, padx=4, pady=10)
        self.b_fo_custom.grid(column=4, row=1, padx=4, pady=10)
        
        for i in range(5) :
            self.formula_frame.columnconfigure(i, weight=1)
            self.formula_frame.rowconfigure(i, weight=1)
 
    
    def generate_limit(self): # Under tabel_frame
        tk.Label(self.tabel_frame, text='Range', font=self.big_font).grid(column=0,row=0, padx=15, pady=2)
        self.e_from = tk.Entry(self.tabel_frame, width=8)
        self.e_to = tk.Entry(self.tabel_frame, width=8)
        
        self.e_from.grid(column=1,row=0, padx=5, pady=2)
        self.e_to.grid(column=2,row=0, padx=5, pady=2)
        
        
        
    def generate_tabel(self, const_list=[]):
        tk.Label(self.tabel_frame, text = 'Const', font=self.big_font).grid(column=0, row=1, pady=2)
        tk.Label(self.tabel_frame, text = 'Fit', font=self.big_font).grid(column=1, row=1, pady=2)
        tk.Label(self.tabel_frame, text = 'Guess', font=self.big_font).grid(column=2, row=1, pady=2)
        self.tabel_elements = {}
        for i, const in enumerate(const_list):
            l_const = tk.Label(self.tabel_frame, text = const)
            
            const_fit = tk.Label(self.tabel_frame, text='nan')
            const_guess = tk.Entry(self.tabel_frame, width=7)
            
            l_const.grid(column=0, row=i+2, pady=2)
            const_fit.grid(column=1, row=i+2, pady=2)
            const_guess.grid(column=2, row=i+2, pady=2)
            
            self.tabel_elements[const] = [const_fit, const_guess, l_const]
            
        for i in range(8) :
            self.tabel_frame.columnconfigure(i, weight=1)
            self.tabel_frame.rowconfigure(i, weight=1)
    
    def generate_mini_figure(self):
        self.mini_fig = Figure(dpi=70, figsize=[4,4])
        self.mini_axes = self.mini_fig.add_subplot(111)
        self.mini_canvas = FigureCanvasTkAgg(self.mini_fig, master=self.mini_figure_frame)  # A tk.DrawingArea.
        self.mini_canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.mini_canvas.draw()
        
    def generate_status(self):
        self.l_status = tk.Label(self.status_frame, text='Messege', wraplength=300)
        self.l_status.grid(column=0, row=0, sticky='NW')
        
        self.progress_bar = ttk.Progressbar(self.status_frame, length=250)
        self.progress_bar.grid(column=0, row=1, sticky='NWES')
        
        for i in range(1) :
            self.status_frame.columnconfigure(i, weight=1)
            self.status_frame.rowconfigure(i, weight=1)
        
    def generate_control(self):
        self.b_fit = tk.Button(self.control_frame, text='Fit', width=12, height=2, font=self.big_font)
        self.b_fit.grid(column=1, row=0, columnspan=2, sticky='NWES', padx=5)
        
        self.b_back = tk.Button(self.control_frame, text='<<', width=7, height=2, font=self.big_font)
        self.b_back.grid(column=0, row=0, columnspan=1, sticky='NWES', padx=5)
        
        self.b_next = tk.Button(self.control_frame, text='>>', width=7, height=2, font=self.big_font)
        self.b_next.grid(column=4, row=0, sticky='NWES', padx=5)
        
        self.b_del = tk.Button(self.control_frame, text='Delete', fg='red', width=7, height=2, font=self.big_font)
        self.b_del.grid(column=3, row=0, sticky='NWES', padx=5)
        
        for i in range(3) :
            self.control_frame.columnconfigure(i, weight=1)
            self.control_frame.rowconfigure(i, weight=1)
        
    def generate_figure(self):
        self.fig = Figure(dpi=120)
        self.axes = self.fig.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.figure_frame)  # A tk.DrawingArea.
        toolbar = NavigationToolbar2Tk(self.canvas, self.figure_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        toolbar.pack(expand=False, side='bottom')
        self.canvas.draw()
                
            
        




if __name__ == '__main__':
    root = tk.Tk()
    Curve_fit_GUI = GUI(root)
    root.mainloop()    
