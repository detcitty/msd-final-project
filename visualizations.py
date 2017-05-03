#################
# exploratory
# visualizations
#################


## imports
import csv
import numpy as np
import pandas as pd
from ggplot import *
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

# TODO: word cloud


## open file
db_path = 'data/us_billboard_25.psv' # change this once file is uploaded

with open(db_path, 'rb') as f:
   rows = f.readlines()

rows = [x.strip() for x in rows]

## row indices
# 0: this week position
# 1: last week position
# 2: this week peak position
# 3: total weeks
# 4: title
# 5: artist
# 6: entry date
# 7: entry position
# 8: peak position
# 9: total weeks
# 10: unknown date 


## format data
head_data = ["this_week_pos", 
             "last_week_pos",
             "this_week_peak",
             "total_weeks", 
             "title",
             "artist", 
             "entry_date",
             "entry_position",
             "peak_position",
             "total_weeks",
             "unknown_date"]
hd = ["artist", "title"]
raw_data = []

artist_dict = dict()
song_dict = dict()
for row in rows:
   col = row.split('|')
   for c in range(len(col)): 
      if col[c].isdigit():
         col[c] = int(col[c])
   r = [col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10]]
   # artist
   if col[5] in artist_dict:
      artist_dict[col[5]] += 1
   else:
      artist_dict[col[5]] = 1
   # song title
   if col[4] in song_dict: 
      song_dict[col[4]] += 1
   else:
      song_dict[col[4]] = 1
   
   raw_data.append(r)


## visualizations
# artist vs. number of weeks on the charts 

df = pd.DataFrame(artist_dict.items())
df.columns = hd
df = df.head(n=50)
df = df.sort_values(by=['title', 'artist'], ascending=False)
# print df

p = df.plot(x = 'artist', y = 'title', kind = 'bar');
plt.show()
# artist vs. number of weeks on the charts 

g = ggplot(aes(x="artist", weight="title"), data=df) +\
    geom_bar() + \
    theme(axis_text_x  = element_text(angle = 30, hjust=1)) + \
    ggtitle('artist vs. number of weeks on the charts') +\
    scale_x_continuous(labels= 'artist')

g.show()

# song vs. number of weeks it's been on the charts

df = pd.DataFrame(song_dict.items())
df.columns = ["title", "weeks"] 
df = df.head(n=50)
df = df.sort_values(by=["weeks", "title"], ascending=False)
# print df

g = ggplot(aes(x="title", weight="weeks"), data=df) + \
    geom_bar() +\
    theme(axis_text_x = element_text(angle=30, hjust=1))+\
    ggtitle('song vs. number of weeks on the charts')

g.show()

# popularity of genres over time -- year vs. genre distribution
# line chart -- different lines = different "popular" genres 


# number of songs launched per year, and % of those that make it on the charts


# average time spent on the charts, by song, by year


