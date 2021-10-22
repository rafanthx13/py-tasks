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

def get_all_folders(path='.'):
    """Get all fodelrs, exlude .ipynb_checkpoints"""
    all_directory_files_contents = os.listdir(path)
    all_dirs = list(filter(lambda x: os.path.isdir(x) and x !='.ipynb_checkpoints',
                           all_directory_files_contents))
    return all_dirs


# Busca SO, separador, raiz
separator = check_os_and_separator()
root_directory = os.getcwd().split(separator)[-1]

# Busca todas as pastas
all_folders_here = get_all_folders()
print(all_folders_here)

# Executa para cada pasta
for folder in all_folders_here:
	all_files_here = list_files('./' + folder)
	for afile in all_files_here:
		# afile == './round-6/round-6-Screenshot_20211010-200938.png'
		os.rename(afile, './' + folder + '/' + folder + '-' + afile.split('/')[-1])
	
	




