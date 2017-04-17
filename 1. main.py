from textblob import TextBlob as tb
import sys
###characteristic of dataline: "," delimited, 
###if in-text includes "," there will be double quotes surrounding the in-text word

def split(input_string):
	result = []
	quote = False
	temp = ""
	for x in input_string:
		if x == "," and quote == False:
			result.append(temp)
			temp = "" 
		elif x == "\"":
			quote = not quote
		else:
			temp += x
	result.append(temp)
	return result


classification = sys.argv[1]
country = sys.argv[2] 

###generate a dictionary to record the imported variable name and index
header = open("%s/%s.csv" %(classification, country)).readline()
temp = split(header.strip())
old_name = {}
for item in temp:
	old_name[temp.index(item)] = item.lower()


###generate old-new name correspondence 
correspondence = open("0. Variable name correspondence.csv").readlines()[1:]
##corr = [x.strip().lower().split(",") for x in corr]
### corr[n][1] is the old name, corr[n][2] is the new name, corr is list of list
corr = [split(x.strip().lower())for x in correspondence]


###output new name header to new csv file (following the order of old name)
outfile = open("cleaned/%s/%s.csv" %(classification, country), "w")
outstring = []

for i in range(len(old_name)):
	for y in corr:
		if old_name[i] == y[1]:
			outstring.append(y[2])

outfile.write(",".join(outstring))
outfile.write("\n")

###read datalines and replace NULL as missing
infile = open("%s/%s.csv" %(classification, country)).readlines()[1:]
infile = [x.strip().lower().split(',') for x in infile]
for x in infile:
	for i in range(len(x)):
		if x[i].lower() in ['null', 'nan']:
			x[i] = ""

for x in infile:
	outfile.write(",".join(x))
	outfile.write("\n")









