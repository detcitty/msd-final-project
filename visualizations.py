#################
# exploratory
# visualizations
#################


## imports
from sets import Set
import csv
import numpy as np
import pandas as pd
from ggplot import *
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # put column into string, generate word cloud
matplotlib.style.use('ggplot')


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
song_total_weeks = dict()
total_weeks_by_year = dict() 
songs_launched_by_year = dict()
seen_songs = Set()
genre_counter = [['genre', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]]

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
   # total weeks
   if isinstance(col[9],int):
      # total_weeks_by_year
      date = col[6].split("-")
      year = date[0]
      if not year in total_weeks_by_year: 
         total_weeks_by_year[year] = [col[9]]
         seen_songs.add(str(col[4])+str(col[5]))
      elif not col[4] in seen_songs: 
         total_weeks_by_year[year].append(col[9])
         seen_songs.add(str(col[4]) + str(col[5]))

      # song_total_weeks
      if not col[4] in song_total_weeks:
         song_total_weeks[col[4]] = col[9]
      else: 
         if song_total_weeks[col[4]] < col[9]:
            song_total_weeks[col[4]] = col[9]
   
   raw_data.append(r)

song_title_string = ""
#print "seen_songs", seen_songs

for i in range(len(raw_data)):
   title = raw_data[i][4]
   song_title_string += " "
   song_title_string += str(title)


## visualizations
# artist vs. number of songs on the charts 

df = pd.DataFrame(artist_dict.items())
df.columns = hd
df = df.sort_values(by=['title', 'artist'], ascending=False)
df = df.head(n=50)

df.loc[:,'artist'] = df.loc[:,'artist'].str.slice(0,15)

p = df.plot(x = 'artist', y = 'title', kind = 'bar', title = 'artist vs. number of weeks on chart', fontsize = 6, legend = False);

plt.tight_layout()
plt.show()
# artist vs. number of weeks on the charts 

#g = ggplot(aes(x="artist", weight="title"), data=df) +\
#    geom_bar() + \
#    theme(axis_text_x  = element_text(angle = 30, hjust=1)) + \
#    ggtitle('artist vs. number of weeks on the charts') +\
#    scale_x_continuous(labels= 'artist')

#g.show()

# song title vs. number of times it's been on the charts

df = pd.DataFrame(song_dict.items())
df.columns = ["title", "weeks"] 
df = df.sort_values(by=["weeks", "title"], ascending=False)
df = df.head(n=50)

p = df.plot(x = 'title', y = 'weeks', kind = 'bar', title = 'song title vs. number of weeks on chart', fontsize = 6, legend = False)
plt.tight_layout()
plt.show()

#g = ggplot(aes(x="title", weight="weeks"), data=df) + \
#    geom_bar() +\
#    theme(axis_text_x = element_text(angle=30, hjust=1))+\
#    ggtitle('song vs. number of weeks on the charts')

#g.show()

# unique song vs. number of weeks on charts
df = pd.DataFrame(song_total_weeks.items())
df.columns = ["title", "total_weeks"]
df = df.sort_values(by=["total_weeks", "title"], ascending=False)
df = df.head(n=50)

p = df.plot(x = 'title', y = 'total_weeks', kind = 'bar', title = 'unique song vs. number of weeks on the chart', fontsize = 6, legend = False)
plt.tight_layout()
plt.show()

# popularity of genres over time -- year vs. genre distribution
# line chart -- different lines = different "popular" genres 


# number of songs launched per year



# average time spent on the charts, by year ..... i don't think this is for unique songs
for key in total_weeks_by_year: 
   weeks = total_weeks_by_year[key]
   avg = sum(weeks) / float(len(weeks))
   total_weeks_by_year[key] = avg
df = pd.DataFrame(total_weeks_by_year.items())
df.columns = ["year", "avg_weeks"]
df = df.sort_values(by=["avg_weeks", "year"], ascending=False) 
df = df.head(n=50)
p = df.plot(x = 'year', y='avg_weeks', kind = 'bar', title= 'average time songs spend on charts, by year', fontsize=6, legend=False)
plt.tight_layout()
plt.show()


# most popular words in song title
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", max_words=2000,
               stopwords=stopwords, max_font_size=40, collocations=False)

wc.generate(song_title_string.lower())

plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
