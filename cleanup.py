import sys
import csv

# Data Processor
# @authors: Peter MacLellan, Nicholas Alekhine
# @date: June 16, 2016

# ----------------
# System Arguments
# ----------------

# @description: Read in command line arguments. First argument should be
#               a local path to a CSV file and the second argument should be
#               the number of peaks for each test.
# @assumption: The CSV file contains a single column of Float values.

if (len(sys.argv) < 3):
	print "usage: python cleanup.py <filepath> <# peaks>"
	exit()

filepath = sys.argv[1]
data = csv.reader(open(filepath, 'rb'), delimiter=",", quotechar='|')
num_peaks = int(sys.argv[2])

sensor_data = []

for row in data:
    sensor_data.append(float(row[0]))


# ---------------------
# Finding Minimum Value
# ---------------------

# @description: Finds the minimum value amongst the first three peaks.

threshold = 200000
local_min = threshold
in_bounds = False
count = 0

for reading in sensor_data:
	if (reading < threshold):
		in_bounds = True
		if (reading < local_min):
			local_min = reading
	elif (in_bounds and reading > threshold):
		count += 1
		in_bounds = False
		if (count > num_peaks - 1):
			break

print "starting resistance: " + str(local_min)
# ----------------
# Normalize Result
# ----------------

# @description: Normalizes the data by setting all values above `local_min` to 0
#               then subtracts all values lower than `local_min` by `local_min`.
#               All values are then inverted to a positive value. 

result = []

for reading in sensor_data:
	if (reading > local_min):
		reading = 0
	else:
		reading -= local_min
		reading *= -1
	result.append([reading])


# -----------------
# List Segmentation
# -----------------

# @description: Segments the main list into sublists that contain 
#               three peaks each. Sublists are also known as "sample sets".

count = 0
in_bounds = False
sublists = []
sublist = []

for val in result:
	sublist.append(val[0])
	if (not in_bounds and val[0] > 0.0):
		in_bounds = True
	elif (in_bounds and val[0] == 0.0):
		count += 1
		in_bounds = False
		if (count > num_peaks - 1):
			sublists.append(sublist)
			sublist = []
			count = 0


# -------------------------
# Local Max for Sample Sets
# -------------------------

# @description: Finds the three maximums for each peak in the sample set.
#               Prints out the findings in a string statement.

print str(len(sublists)) + " sample sets"

index = 1
for sub in sublists:
	peak_count = 0
	local_max = 0
	in_bounds = False
	local_maxes = []
	for value in sub:
		if value > 0:
			in_bounds = True
		
		if in_bounds and (value > local_max):
			local_max = value
		elif in_bounds and value == 0:
			in_bounds = False
			peak_count += 1
			local_maxes.append(local_max)
			local_max = 0

		if peak_count > num_peaks - 1:
			break

	print "Sample Set " + str(index) + ". \nMaximums: " + str(local_maxes)
	index += 1

# -----------
# CSV Builder
# -----------

# @description: Builds the CSV file which contains a column for each sample set.

longest = max(len(sub) for sub in sublists)

finalresult = []
for i in range(longest):
	sub_result = []
	for j in range(len(sublists)):
		sub_result.append(0 if len(sublists[j]) <= i else sublists[j][i])
	finalresult.append(sub_result)

if '/' in filepath:
	subpaths = filepath.split('/')
	subpaths[-1] = 'output_' + subpaths[-1]
elif '\\' in filepath:
	subpaths = filepath.split('\\')
	subpaths[-1] = 'output_' + subpaths[-1]

filepath = '/'.join(subpaths)

f = open(filepath, 'w+b')
writer = csv.writer(f)
writer.writerows(finalresult)

print 'Success! \nOutput file path: ' + filepath