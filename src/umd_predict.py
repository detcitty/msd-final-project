import numpy as np
import pandas as pd

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Reading song names file
infile = open("song_names.txt")
song_names = infile.readlines()
infile.close()

#Reading billboard database
infile = open("../data/us_billboard_25.psv")
database = infile.readlines()
infile.close()

#Removing the new line character from end of song names
song_names = [s.rstrip() for s in song_names]

outfile = open("song_rank_weeks.txt", "w")

for i in range(len(song_names)):
    song = song_names[i]
    #print song
    for j in range(len(database)):
        if database[j].find(song) != -1:
            if is_int(database[j].split('|')[-3]) == False or is_int(database[j].split('|')[-2])  == False:
                print 'couldn\'t convert to int'
                break
            line = song + '|' + database[j].split('|')[-3] + '|' + database[j].split('|')[-2]
            print line
            outfile.write(line+'\n') 
            break

