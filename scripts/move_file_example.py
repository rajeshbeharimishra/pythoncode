import shutil
import os
import glob

source_dir = 'C:\\Users\\rajesh.mishra\\Downloads\\EBB\\'
target_dir = 'C:\\Users\\rajesh.mishra\\Downloads\\EBB\\Processed\\'


file_names = os.listdir(source_dir)
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)

