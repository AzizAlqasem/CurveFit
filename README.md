# CurveFit
CurveFit is a Data Analysis software that makes quick and easy fitting using python, the programming langauge. It allows the user to choose a fitting formula, and then get the fitted unknown constants. The Fitting results can be exported and saved in an excel file.


# Quick Tutorial
This Video tutorial takes you through the basic useages of CurveFit:
https://youtu.be/3d7o3ZIqxKY

## How To Use CurveFit
1. Open PeakFit
2. Press Load Data, and select your data from a txt file. Your data should be as a two column of x-axis and y-axis.
3. Write a formula that best describe your data. The constants that you put in your formula are being searched for. The only variable is the letter "x". You can use any math function such as sin, cos, ... etc.
* Note: To watch a constant in the mini-figure, write it in a capital letter. Eg., A or Aa
4. Press ok to start fitting the first file.
5. Guess values for your constants to help CurveFit find them quickly.
6. press Fit to do the fitting.
7. Repeat (5) and (6) if the fitting is not accurate enough.
8. Go to the next file and Fit again, untill you finish them all.
9. Press Save to save your Fitting results in excel file.
10. If you wish to change your fitting formula, press restart.
11. If you wish to start a new fitting with different data and formula, press Load Data



# installation:
## Through The executable file
**Note: The executable file runs at Windows 10, and may run at old windows versions!**
1. Download the executable file package through:
https://github.com/AzizAlqasem/CurveFit/releases/download/v1.0.0/CurveFit.v1.0.0.zip
2. Unzip the file
3. Go to App.exe and run it

## Through python:
1. Download pyhton 3.6+
2. install the following packages, from the command line:
  pip install numpy
  pip install scipy
  pip install matplotlib
  pip install sympy
  pip install pandas
  pip install openpyxl
  pip install re
 3. Download this repo 
 4. Run the python file named App.py
  
# Author:
Abdulaziz Alqasem
Aziz_Alqasem@hotmail.com

# credit:
Thanks to all developers at: Python, Numpy, SciPy, Matplotlib, SymPy, Pandas, re, and Openpyxl
