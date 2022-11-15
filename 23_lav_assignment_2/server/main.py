import glob
import shutil
import os
import linecache
import runpy

destination_path = '../destination/'

source_path = '../source/*.txt'
source_file_founded = False
try:
    soruce_object = glob.glob(source_path)[0]
    filename_prefix = soruce_object.split('\\')[1].split('.')[0]
    filename_postfix = soruce_object.split('\\')[1].split('.')[1]
    source_file_founded = True
    
    parent = '.'
    dir_name = 'proceed_files'
    path = os.path.join(parent, dir_name)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    shutil.copy(soruce_object, '.')
except IndexError:
    print('source(.txt) file not found')
    
if source_file_founded:
    for i in range(1, 4):
        filename = f'{filename_prefix}_{i}.{filename_postfix}'
        
        with open(f'{filename_prefix}.{filename_postfix}', 'r') as  f1:
            for j in range(1, (10 * i) + 1):
                x = linecache.getline(f'{filename_prefix}.{filename_postfix}', j)
                
                with open(f'{path}/{filename}', 'a') as f2:
                    f2.write(x)
                f2.close()
        f1.close()
        
    shutil.make_archive(dir_name, 'zip', dir_name)
    shutil.unpack_archive(f'{dir_name}.zip', destination_path)
    
    try:    
        os.remove(f'{dir_name}.zip')
        os.remove(f'{filename_prefix}.{filename_postfix}')
        shutil.rmtree(f'{dir_name}')
    except:
        pass
    
    python_files = glob.glob('../source/*.py')
    for python_file in python_files:
        runpy.run_path(path_name=python_file)


