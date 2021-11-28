
# coding: utf-8

# # Extrair Arquivos de Pastas
# 
# Criado em: 22/11/2021
#     
# ## Objetivo
# 
# **Problema**
# 
# Certos crusos possuem uma pasta por arquivo. Se os vídeos forem curtos, você caba tendo que trocar de pasta a todo momento.
# 
# **Proposta de soluçâo**
# 
# Esse py-script tem como objetivo: Extrair arquivos de uma pasta, renomealos e colocalos na riz.
#     
# **Justificativa**
# 
# Executando a proposta, os arquivos estarao juntos e dá para assitir as aulas em sequência
# 
# ## Import Libs
# 

# In[10]:


import os
import json


# ## Snippets

# In[11]:


def check_os_and_separator():
    """Check if is linux and windows, and retorn separator"""
    separator, op_system = ('\\','windows') if os.name == 'nt' else ('/', 'linux')
    print(op_system)
    return separator


# In[12]:


def get_all_folders(path='.'):
    """Get all fodelrs, exlude .ipynb_checkpoints"""
    all_directory_files_contents = os.listdir(path)
    all_dirs = list(filter(lambda x: os.path.isdir(x) and x !='.ipynb_checkpoints',
                           all_directory_files_contents))
    return all_dirs


# In[13]:


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r


# ## Start

# In[14]:


separator = check_os_and_separator()

root_directory = os.getcwd().split(separator)[-1]
# root_directory


# In[40]:


all_folders = get_all_folders()
all_folders


# In[48]:


alist = []
for fold in all_folders:
    print('Fold ==>', fold)
    files = list_files(fold)
    files.sort()
    if(len(files) == 0):
        print('\t\tEmpty Files')
    try:
        c = 0
        for afile in files:
            print(afile)
            pure_name = afile[2:].split(separator)[-1] # pega o nome+ext do arquivo
            folder_name = afile[2:].split(separator)[-2]
            extension = afile[2:].split(separator)[-1].split('.')[-1]
            finalize_path_file = str(c) + '-' + folder_name + '.' + extension
            print('to ===', '.' + finalize_path_file, '\n')
            os.rename(afile, finalize_path_file) # poe na raiz
#             print('\t', 'the_image', '\t', finalize_path_file) # print se success
#             alist.append(finalize_path_file)
            c += 1
    except Exception as err:
        print('ERROR')
        print(err)

