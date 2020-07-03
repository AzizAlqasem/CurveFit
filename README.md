# CurveFit
CurveFit is a Data Analysis software that makes quick and easy fitting using python, the programming langauge. It allows the user to choose a fitting formula, and then get the fitted unknown constants. The Fitting results can be exported and saved in an excel file.


# Quick Tutorial
This Video tutorial takes you through the basic useages of CurveFit:
https://youtu.be/3d7o3ZIqxKY

## How To Use CurveFit
1. Run PeakFit
2. Press Load Data, and select your data from .txt file(s). Your data in a .txt/.csv should be formated as two column of x-axis and y-axis.
3. Write a formula that best describe your data. The constants that you put in your formula are being searched for. The only variable is the letter "x". You can use any math function such as sin, cos, ... etc.
* Note: To watch a constant in the mini-figure, write it in a capital letter in the formula. Eg., "Ax + b". "A" will appear in the minifigure.
4. Press ok to start the fitting.
5. Guess values for your constants to help CurveFit find them quickly. The guess value can be any reasonable number. It helps CurveFit not to look from -inf to +inf !
6. press Fit to do the fitting.
7. Repeat (5) and (6) if the fitting is not accurate enough.
8. Go to the next file and Fit again, untill you finish them all.
9. Press Save to save your Fitting results in excel (.csv) file.
10. If you wish to change your fitting formula, press restart.
11. If you wish to start a new fitting with different data and formula, press Load Data



# Installation:
## Through The Executable File
1. Download the executable file package through:
https://github.com/AzizAlqasem/CurveFit/releases
2. Unzip the file
3. Go to App.exe (or App in macOS) and run it

## Through Python:
1. Download pyhton 3.6+
2. install the following packages, from the command line:
```
  pip install numpy
  pip install scipy
  pip install matplotlib
  pip install sympy
  pip install pandas
```
 3. Download this repo 
 4. Run the python file named App.py
  
# Author:
    Abdulaziz Alqasem
    Aziz_Alqasem@hotmail.com

# Credit:
Thanks to all developers at: Python, Numpy, SciPy, Matplotlib, SymPy, Pandas, re, and Openpyxl
