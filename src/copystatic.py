import os
import shutil

def copy_files(source_path: str, destination_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    for file in os.listdir(source_path):
        from_path = os.path.join(source_path, file)
        dest_path = os.path.join(destination_path, file)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)