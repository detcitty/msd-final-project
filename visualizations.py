#################
# exploratory
# visualizations
#################

import csv

db_path = 'db.csv' # change this once file is uploaded

with open(db_path, 'rb') as f:
   reader = csv.reader(f)
   rows = list(reader)

# row indices
# 0: this week position
# 1: last week position
# 2: this week peak position
# 3: total weeks
# 4: title, artist 
# 5: entry date
# 6: entry position
# 7: peak position
# 8: total weeks

# TODO: visualizations

# artist vs. number of unique songs on the charts 

# song vs. number of weeks it's been on the charts

# popularity of genres over time -- year vs. genre distribution

# number of songs launched per year, and % of those that make it on the charts

# average time spent on the charts, by song, by year
