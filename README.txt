-------------------------------------------------------------------------------
PRE-REQUISITES
-------------------------------------------------------------------------------
1) Install python
2) Know how to reference relative paths
   Hint: '.' means this directory, '..' means the parent of this directory.
3) Have sensor data with a consistent number of peaks for each force applied.
   Between each peak, the resistance value must go above a certain threshold
   so that it gets truncated down to 0 by the script for the peak to be 
   detected.

-------------------------------------------------------------------------------
Steps to Use
-------------------------------------------------------------------------------

1. Create a new CSV file that only contains one column with all of the sensor
   readings. This can be done with excel, but make sure to save as CSV and 
   not XLXS.

2. Open Command Prompt (cmd).

3. Navigate to the directory where your file is located.

4. Run 'python cleanup.py <path_to_file> <number_of_peaks>'

-------------------------------------------------------------------------------
Example
-------------------------------------------------------------------------------

Your raw output file is Z:\Projects\Yoda\Mechanical\Raw\test_A.csv

Open this file in Excel (or your favorite text editor) and copy the entire 
column that contains the sensor readings. Create a new Excel file and paste 
this column into column A of the new spreadsheet. Make sure that there are 
no blank rows or rows with text at the top. 

IT SHOULD CONTAIN ONLY ONE COLUMN OF SENSOR READINGS.

Now, you have your nice clean spreadsheet. Save it as a CSV, let's say
Z:\Projects\Yoda\Mechanical\Raw\test_A_clean.csv

Now you open the command prompt and navigate to Z:\Projects\Yoda\Mechanical.
Assuming your cmd opens to "C:\Users\<username>\, this can be accomplished with
z: [enter] -- this will switch you to the Z network drive
cd \Projects\Yoda\Mechanical [enter]

From here, you want to run the following command:
python cleanup.py .\Raw\test_A_clean.csv 3

You should see some output telling you the 3 maximum peak values in each subset 
of test data. If you look in Z:\Projects\Yoda\Mechanical, there should be a new
file called output_test_A_clean.csv

Open this new file in Excel and you should see one column for each subset of 
test data. Each column contains the number of peaks specified when you called
the command, so 3 in this case.

Make pretty graphs.
Profit.