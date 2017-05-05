import os
import glob


path_name = "./db_lyrics/*.txt"
output_path = "./output_lyrics/"

numline=3 #3 lines to skip

for f in glob.glob(path_name):
    lines = open(f).readlines()
    open(f, 'w').writelines(lines[:-4])
    
    
