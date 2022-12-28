__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")

 #Part 1

path_cache = base_path +'\\files'
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
def cache_zip(file_name, cache_dir):
    file_name = data_path
    cache_dir = cache_path
    with ZipFile(file_name, 'r') as zip:
        zip.extractall(cache_dir)

#Part 3
def cached_files():
    dir_path = cache_path
    list_of_files = []
    for i in os.listdir(dir_path):
        list_of_files.append(os.path.join(dir_path, i))
    return list_of_files

#Part 4
def find_password(list_of_files):
    for file_name in list_of_files:
        with open(file_name, 'r') as f:
            contents = f.readlines()
            for line in contents:
                if 'password' in line:
                     password = line.split(": ")[1][:-1]
                     print(password)
                     return password
