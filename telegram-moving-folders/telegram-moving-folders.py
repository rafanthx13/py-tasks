
# coding: utf-8

# # Agrupar Photos e Videos do Telegram em uma única pasta
# 
# PROCESSO:
# + Inicio: Coloque esse arquivo na pasta raiz onde há pastas como `ChatExport_18_10_2021`
# + Ele fai lsitar cada pasta e mover o arquivo, depois a pasta fica totalmente vazia de '/photos' e '/videos'

# In[1]:


import os


# # Snippets'

# In[2]:


def check_os_and_separator():
    """Check if is linux and windows, and retorn separator"""
    separator, op_system = ('\\','windows') if os.name == 'nt' else ('/', 'linux')
    print(op_system)
    return separator


# In[3]:


def get_all_folders(path='.'):
    """Get all fodelrs, exlude .ipynb_checkpoints"""
    all_directory_files_contents = os.listdir(path)
    all_dirs = list(filter(lambda x: os.path.isdir(x) and x !='.ipynb_checkpoints',
                           all_directory_files_contents))
    return all_dirs


# In[4]:


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r


# # Devolp Process

# In[5]:


separator = check_os_and_separator()

root_directory = os.getcwd().split(separator)[-1]
root_directory


# In[23]:


all_folders = get_all_folders()
all_folders


# In[19]:


all_folders


# In[10]:


nw_folder = './new-folder'
if(not os.path.isdir(nw_folder)):
    os.mkdir(nw_folder)
    os.mkdir(nw_folder + separator + 'videos')
    os.mkdir(nw_folder + separator + 'photos')


# In[ ]:


# os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")


# ## Iterate on each folder

# In[24]:


new_photo_path =  nw_folder + separator + 'photos'
new_videos_path =  nw_folder + separator + 'videos'

all_folders = list(filter(lambda x: x != 'new-folder', all_folders))

for fold in all_folders:
    print('Fold ==>', fold)
    # Photos
    photos_path = './'+ fold + separator + 'photos'
    list_photos = list( filter(lambda file: not 'thumb' in file, list_files(photos_path)) )
    if(len(list_photos) == 0):
        print('\t\tEmpty Photos')
    try:
        for photo in list_photos:
            the_image = photo[2:].split(separator)[-1]
            os.rename(photo, new_photo_path + separator + the_image)
            print('\t', the_image)
    except Exception as err:
        print('ERROR')
        print(err)
    # Videos
    videos_path = './'+ fold + separator + 'videos'
    list_videos = list( filter(lambda file: not 'thumb' in file, list_files(videos_path)) )
    if(len(list_videos) == 0):
        print('\t\tEmpty Videos')
    try:
        for video in list_videos:
            the_video = video[2:].split(separator)[-1]
            os.rename(video, new_video_path + separator + the_video)
            print('\t', the_video)
    except Exception as err:
        print('ERROR')
        print(err)

