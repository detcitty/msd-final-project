import os
import glob
import re

path_name = "./db_lyrics/*.txt"
output_path = "./output_lyrics/"


for f in glob.glob(path_name):
    feat = f.replace("_", "")
    first = f.split("/")

    art_song = first[-1]
    
    split_file = [a for a in re.split(r'([A-Z][A-Z])', art_song) if a]
    track = split_file[0]
    track = track.rstrip('_') 
    word_space = track.replace("_", " ")
    #word_space = word_space.lower()
    print(word_space)
    #print(split_file)

