import os
import shutil

source_folder = "files"
destination_folder = "organized"

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        ext = filename.split(".")[-1]
        ext_folder = os.path.join(destination_folder, ext)
        
        if not os.path.exists(ext_folder):
            os.mkdir(ext_folder)
        
        shutil.move(file_path, os.path.join(ext_folder, filename))

print("Files organized successfully.")
