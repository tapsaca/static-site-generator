import os
import shutil
from copystatic import copy_files

dir_path_public = "./public"
dir_path_static = "./static"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    copy_files(dir_path_static, dir_path_public)

main()