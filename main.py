__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os.path
 #Part 1

path_cache = os.getcwd()+'\\files'
def clean_cache():
    path = path_cache
    if os.path.isdir('files\cache'):
        for file in os.scandir(path+'\cache'):
            os.remove(file.path)
        print('aanwezig')
    else:
        print('niet aanwezig')
        os.mkdir('files\cache')
    return

clean_cache()

#Part 2

from zipfile import ZipFile

def cache_zip(file_name, cache_dir):
    file_name = 'C:\\Users\\localadmin\\Documents\\Documents\\Learning Code\\Winc\\data.zip'
    cache_dir = 'C:\\Users\\localadmin\\Documents\\Documents\\Learning Code\\Winc\\cache'
    with ZipFile(file_name, 'r') as zip:
        zip.extractall(cache_dir)

#Part 3


import os
def cached_files():
    dir_path = 'C:\\Users\\localadmin\\Documents\\Documents\\Learning Code\\Winc\\cache'
    list_of_files = []
    for i in os.listdir(dir_path):
        list_of_files.append(os.path.join(dir_path, i))
    return list_of_files

#Part 4
import os
def find_password(list_of_files):
    for file_name in list_of_files:
        with open(file_name, 'r') as f:
            contents = f.readlines()
            for line in contents:
                if 'password' in line:
                   return line.strip()[10:]