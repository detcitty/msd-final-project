import numpy as np
import pandas as pd

infile = open("song_rank_weeks.txt","r")
data = infile.readlines()
infile.close()

songs, ranks, weeks = [], [], []
for i in range(len(data)):
    songs.append(data[i].split('|')[0])
    ranks.append(data[i].split('|')[1])
    weeks.append(data[i].split('|')[2].rstrip())

#for i in range(len(data)):
#    print ranks[i], weeks[i]
#    print int(ranks[i]), int(weeks[i])

song_ranks_weeks = pd.DataFrame({'songs':songs, 'ranks':ranks, 'weeks':weeks})
print list(song_ranks_weeks)
print song_ranks_weeks[:2]
