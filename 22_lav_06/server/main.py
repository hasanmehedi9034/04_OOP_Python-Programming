'''object processor'''

import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination/'

postfix = [1, 2, 3]

soruce_object = glob.glob(source_path)

object_path = soruce_object[0]

shutil.copy(object_path, '.')

object_name = object_path.split('\\')[-1].split('.')
prefix = object_name[0]
extension  =  object_name[1]

for item in postfix:
    file_name = prefix + '_' + str(item) + '.' + extension    
    shutil.copy(object_path, f'{destination_path}/{file_name}')

os.remove(object_path)
