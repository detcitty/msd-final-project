import os
import glob



output_path = "./output_lyrics/"
path_name = "./output/*.txt"


numline=3 #3 lines to skip

for f in glob.glob(path_name):
    lines = open(f).readlines()
    open(f, 'w').writelines(lines[:-4])


