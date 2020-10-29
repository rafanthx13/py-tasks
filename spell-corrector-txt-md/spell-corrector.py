# Replace Words in a file
# Its necessari pass the file name in arguments. Use TAB
# exec: $ python spell-corrector.py file.ext

# Created: 28/10/2020

import sys
from datadict import dictionary
import re

if(len(sys.argv) != 2):
	exit()
afile = sys.argv[1]

#read input file
fin = open(afile, "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
for wrong, right in dictionary.items():
	data = data.replace(wrong, right)
#close the input file
fin.close()
#open the input file in write mode
fin = open(afile, "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()
