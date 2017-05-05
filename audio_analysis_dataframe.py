import numpy as np
import pandas as pd

infile = open("audio_analysis_uri.txt","r")
audio_analysis = infile.readlines()
infile.close()

features = []
for i in range(18):
    f = []
    features.append(f)

for i in range(2):
    temp = audio_analysis[i].split('|')
    for j in range(18):
        features[j].append(temp[j])
print features

#Changing all the column names except uri to float
for i in range(1,18):
    features[i] = [float(f) for f in features[i]]

#Header names for the audio_analysis_dataframe
header_names = []
for i in range(18):
    header_names.append('col_'+str(i))
print header_names

audio_analysis_df = pd.DataFrame()
for i in range(18):
    audio_analysis_df[header_names[i]] = features[i]

#minor changes
audio_analysis_df.rename(columns={'col_0':'uri'}, inplace=True)
#audio_analysis_df['col_17'] = [r.strip() for r in audio_analysis_df['col_17']]

print audio_analysis_df.dtypes
