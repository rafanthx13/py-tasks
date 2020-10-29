# Rename files in sorted order put a new prefix (name) with numbers
# Is necessary: the files was in same directory; pass a valid prefix;

# Cratede: 28/10/2020

import os

def get_extension(afile):
	return os.path.splitext(afile)[1]

prefix = input('Input the prefix: ')

if(prefix == None or prefix == ''):
	exit()

count = 1

list_files = [f for f in os.listdir() if get_extension(f) != '.py']
list_files.sort()

for afile in list_files:
	extension = get_extension(afile)
	new_name = "{}-{:02d}{}".format(prefix, count, extension)
	os.rename(afile, new_name)
	print("rename {} to {}".format(afile, new_name))
	count += 1
