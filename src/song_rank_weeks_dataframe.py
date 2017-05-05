import numpy as np
import pandas as pd

infile = open("song_rank_weeks.txt","r")
data = infile.readlines()
infile.close()

songs, ranks, weeks = [], [], []
for i in range(5):
    songs.append(data[i].split('|')[0])
    ranks.append(int(data[i].split('|')[1]))
    weeks.append(int(data[i].split('|')[2].rstrip()))

song_ranks_weeks = pd.DataFrame({'songs':songs, 'ranks':ranks, 'weeks':weeks})
print list(song_ranks_weeks)
print song_ranks_weeks[:2]
