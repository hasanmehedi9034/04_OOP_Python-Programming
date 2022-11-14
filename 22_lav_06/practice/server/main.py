import glob
import shutil
import os

source_path = '../source/*'
source_files = glob.glob(source_path)
source_file = source_files[0]

destination_path = '../destination/'

shutil.copy(source_file, '.')

filename_prefix = source_file.split('\\')[1].split('.')[0]
filename_postfix = source_file.split('\\')[1].split('.')[1]

for i in range(1, 5):
    filename = f'{filename_prefix}_{i}.{filename_postfix}'
    shutil.copyfile(source_file, f'{destination_path}/{filename}')

os.remove(source_file)
os.remove(f'{filename_prefix}.{filename_postfix}')
 