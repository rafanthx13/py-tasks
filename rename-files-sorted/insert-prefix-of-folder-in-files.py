# Colocar o nome da pasta como prefixo apra todos os arquivo

## 22/10/2021

import os

def check_os_and_separator():
    """Check if is linux and windows, and retorn separator"""
    separator, op_system = ('\\','windows') if os.name == 'nt' else ('/', 'linux')
    return separator

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

separator = check_os_and_separator()
root_directory = os.getcwd().split(separator)[-1]

all_files_here = list(filter(lambda x: x != './insert-prefix-of-folder-in-files.py', list_files('.')))

for afile in all_files_here:
	os.rename(afile, './' + root_directory + '-' + afile[2:])
