import os
import glob
import re

path_name = "./db_lyrics/*.txt"
output_path = "./output_lyrics/"


for f in glob.glob(path_name):
    feat = f.replace("_", "")


    print(feat)
    split_file = [a for a in re.split(r'([A-Z][a-z]*)', f) if a]

    print(split_file)

