import numpy as np
import pandas as pd

infile = open("track_uri.txt","r")
data = infile.readlines()
infile.close()

track_names = []
track_uris = []
for i in range(5):
    track_names.append(data[i].split('|')[0])
    track_uris.append(data[i].split('|')[1].rstrip())

track_uri_df = pd.DataFrame({'track_uri':track_uris, 'track_name':track_names})
print list(track_uri_df)
print track_uri_df[:2]
