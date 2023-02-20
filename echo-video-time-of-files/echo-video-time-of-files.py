#!/usr/bin/env python
# coding: utf-8

# # course-file-tree-generator
# 
# Gerar README global e Readme de cada módulo de pastas de um curso
# 
# 
# # Last Update
# 
# + 11/11/2022
#   - Será somente este arquivo
#   - A cada novo curso, que precisar ter um novo script para separar núero de nome do arquivo, SALVE no comentário
#   - Está ordenando tudo

# In[1]:


import os
import json

import moviepy.editor


# In[2]:


# windows :: \\, linux: /
    
from sys import platform
if platform == "linux" or platform == "linux2":
    print('linux')
    separator = '/'
elif platform == "darwin":
    print('OS X')
    separator = '/'
elif platform == "win32":
    print('windows')
    separator = '\\'

separator


# # Snippets

# In[15]:


# Converts into more readable format 
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds

# format: 00h00m00s
def get_convert(hours, mins, secs):
    if(hours == 0):
        return str(mins).zfill(2) + 'min' + str(secs).zfill(2) + 's'
    else:
        return str(hours).zfill(2) + 'h' + str(mins).zfill(2) + 'min' + str(secs).zfill(2) + 's'

# get duraction of video-file
def get_duraction_of_file(filepath):
    video_duration = 6000
    video = moviepy.editor.VideoFileClip(filepath)
    video_duration = int(video.duration)
    hours, mins, secs = convert(video_duration)
    return get_convert(hours, mins, secs), video_duration


# In[4]:


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r


# # Get Root

# In[5]:


# Pga o nome da pasta raiz. Deve ser o nome do curso
root_course = os.getcwd().split(separator)[-1]
print('Nome do curso:\n==>', root_course)


# # Get Folders

# In[9]:


# Get all sub-folders of actual directory
path = '.'
all_directory_files_contents = os.listdir(path)

# Filter Directories Only
all_dirs = list(filter(lambda x: os.path.isdir(x), all_directory_files_contents))
all_dirs

# Remove folders invalids
list_of_exlcude_dirs = ['.ipynb_checkpoints']

for el in list_of_exlcude_dirs:
    if(el in all_dirs):
        all_dirs.remove(el)
        
# Show result
all_dirs


# In[13]:


filter_videos_files = ['mp4','ts', 'MP4']

all_files_here = list(filter(lambda x: x.split('.')[-1] in filter_videos_files, all_directory_files_contents))
all_files_here


# ## Listing Local hours

# In[17]:


print('.')
for el in all_files_here:
    video_name = (os.path.splitext(el)[0]).split(separator)[-1]
#     print(video_name)
    video_tree = {
        'name': '',
        'time_video': '',
        'time_video_seconds': '',
    }
    time_string, video_seconds = get_duraction_of_file(el)
    # save video data
    video_tree['time_video_seconds'] = video_seconds
    video_tree['time_video'] = time_string
    video_tree['name'] = video_name
    print('+', video_name, '(' + time_string + ')\n')
#     # save in module data
#     module_tree['files'].append(video_tree)
#     module_tree['number_of_videos'] += 1
#     module_tree['time_module_seconds'] += video_seconds

# h, m, s = convert(module_tree['time_module_seconds'])
# module_tree['time_module'] = get_convert(h, m, s)


# ## Listing sub-folder

# In[27]:


# list_files(filepath_name)

print('.')
for el in all_dirs:
    list_subfiles = list_files(el)
    list_subfiles.sort()
    print(el)
    for files in list_subfiles:
        video_name = files.split(separator)[-1].replace('.mp4','')
        time_string, video_seconds = get_duraction_of_file(files)
        print('+', video_name, '(' + time_string + ')')
