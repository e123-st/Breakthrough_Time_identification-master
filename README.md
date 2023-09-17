# Breakthrough_Time_identification_master  
The Breakthrough_Time_identification_master, which is written by Python language, is a software package designed for the high-throughput based analysis of the gas mixture separation performances of porous materials in fixed bed by our group.   

# Installation of Breakthrough_Time_identification_master  
To install this software package, the numpy, pandas, matplotlib, and kneed packages should be firstly installed.  

# Functions of the software package  
For different analysis targets, three modules, BCC, BTI, and BTI2, are built in this package.   
## 1. BCC module  
BCC module is used to calculate the breakthrough time, draw the breakthrough curve, and output the data of breakthrough curve for gas mixtures consisting of no more than four elements. There are three functions in this module, which are  "Breakthrough_times_output", "DATA_output", and "Figure_output".  

### 1.1 Breakthrough_times_output  
This function is used for the breakthrough time calculation, when the input parameter of "Breakthrough Time Calculation" is set as "Yes" in "Parameters.input" file.  

### 1.2 DATA_output  
This function is used to output the data of breakthrough curve. The unit of time can be set as hour, minute, and second via setting the input of "unit_of_time" as "h", "min", or "s".  

### 1.3 Figure_output  
This function is used for the drawing of breakthrough curve figure. For the breakthrough curve figure, the jpg, tif, png, and pdf formats can be chosen for result saving via modifying the "save_type" under the "Figure_output" function. Specially, the output figure will only appear in the interactive interface of python IDE instead of saving in the "FIGURE" folder when the "save_figure = "No"" is set under Windows system. Besides, the dpi of the figure and the style and color of the curve and breakthrough points can also be chosen under the "Figure_output" function.  
To accelerate the output of figure and data, the input parameter of "Breakthrough Time Calculation" can be set as "No" in "Parameters.input" file. Then, the breakthrough times will not be calculated.  

## 2. BTI module  
BTI module is used to calculate the breakthrough time via prolonging the setting time steps with iteration. The BTI module is only use for gas mixtures consisting of no more than four elements.

## 3. BTI2 module  
BTI2 module can also be used to calculate the breakthrough time via prolonging the setting time steps with iteration. Different from the BTI module, the BTI2 module is designed for the calculation of any gas mixtures. The BTI2 module is a developing module, which may take the place of BCC and BTI in the future version.

# Steps to use the software package  
## 1. Input files preparation  
To use this package, the python file, excel file, and "Parameters.input" file should be prepared. After preparing the above files, the python file and the "Parameters.input" file should be placed in the same folder, and the path of this folder should be set as the operation path when the python IDE is used under Windows system. The excel file can be placed in any address. The examples of above three files except script file are provided in the "Example" folder.

▲NOTE: The styles of "Parameters.input" file and excel file for BTI2 module are different from those for the other two modules. The parameters for elements should be not set if they do not exist in gas mixture for BTI2 module, which should be set to 0 for BCC and BTI modules.

### 1.1 Excel file  
The parameters of adsorbent should be written in the excel file, including its name or number, density, the saturation value of adsorbate loading, the equilibrium constant of Langmuir, and the overall mass transfer coefficient. 

▲NOTE: For the high-throughput calculation, the paraments of all adsorbents can be written in different rows of one excel file. 

### 1.2 Parameters.input file  
The other parameters should be written in the "Parameters.input" file, including the time steps, the space steps, the pressure, the temperature, and so on. 

▲NOTE: The value of "Row of Excel Table" is 0 when the parameters of adsorbent are written in the second row of the excel file and the value of "sheet_name" is 0 when the parameters are written in the first sheet. The scientific notation can be used for numbers input in "Parameters.input" file. For example, "1000,000" can be written as 1000000, 1e6, or 1E6.

▲NOTE: Via modifying the value of "Row of Excel Table" in the "Parameters.input" file, the high-throughput calculation can be processed. 

## 2. Output files  
After calculation, the output results can be found in different folders. Three folders will be created in the operation path when one of the modules are used.

### 2.1 OUTPUT  
The breakthrough times and the "C/C0 for Breakthrough Time" for different gas molecules can be found in the "OUTPUT_X.txt" in "OUTPUT" folder. (C is the concentration of gas at breakthrough time, C0 is the initial concentration of gas, X is the name of adsorbent.)

### 2.2 FIGURE  
The breakthrough curve figure can be found in "FIGURE" folder when the "Figure_output" function in BCC module is used.

### 2.3 DATA  
The data for drawing breakthrough curve figure can be found in "DATA" folder when the "DATA_output" function in BCC module is used.

