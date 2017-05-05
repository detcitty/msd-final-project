import numpy as np
import pandas as pd
from pandas.stats.api import ols
import rpy2

#################################################################################
#TRACK_URI DATAFRAME
infile = open("track_uri.txt","r")
data = infile.readlines()
infile.close()

track_names = []
track_uris = []
for i in range(len(data)):
    track_names.append(data[i].split('|')[0])
    track_uris.append(data[i].split('|')[1].rstrip())

track_uris = [s.split(':')[2] for s in track_uris]
track_uri_df = pd.DataFrame({'uri':track_uris, 'song':track_names})
print track_uri_df.dtypes
#################################################################################

#################################################################################
#SONG_RANKS_WEEKS_DATAFRAME
infile = open("song_rank_weeks.txt","r")
data = infile.readlines()
infile.close()

songs, ranks, weeks = [], [], []
for i in range(len(data)):
    songs.append(data[i].split('|')[0])
    ranks.append(data[i].split('|')[1])
    weeks.append(data[i].split('|')[2].rstrip())

#ranks = [float(r) for r in ranks]
#weeks = [float(w) for w in weeks]
song_ranks_weeks = pd.DataFrame({'song':songs, 'rank':ranks, 'week':weeks})
print song_ranks_weeks.dtypes
################################################################################

################################################################################
#AUDIO_FEATURES DATAFRAME
from audio_features_read import read_audio_features

#Reading audio_features from the file
features = read_audio_features('../audio_features.txt')

#Reading audio features into data frame
audio_features = pd.DataFrame(features)

#Remove unnecessary columns from audio_features
audio_features.drop('analysis_url', axis=1, inplace=True)
audio_features.drop('time_signature', axis=1, inplace=True)
audio_features.drop('track_href', axis=1, inplace=True)
audio_features.drop('type', axis=1, inplace=True)
audio_features.drop('id', axis=1, inplace=True)

audio_features['uri'] = audio_features['uri'].apply(lambda x: x.split(':')[-1])
print audio_features.dtypes
###############################################################################

#track_uri_df
#song_ranks_weeks
#audio_features
uri_songs_weeks_df = pd.merge(track_uri_df, song_ranks_weeks, on='song', how='inner')
final_df = pd.merge(uri_songs_weeks_df, audio_features, on='uri', how='inner')
#Removing week to predict rank, will remove rank to predict week later
final_df.drop('rank', axis=1, inplace=True)
print list(final_df)

cols = [col for col in final_df.columns if col not in ['rank']]
print cols

#Changing datatypes of dataframe columns
final_df.drop('song', axis=1, inplace=True)
final_df.drop('uri', axis=1, inplace=True)
final_df.drop('danceability', axis=1, inplace=True)
final_df.drop('instrumentalness', axis=1, inplace=True)
final_df.drop('speechiness', axis=1, inplace=True)
final_df.drop('valence', axis=1, inplace=True)
final_df.drop('liveness', axis=1, inplace=True)
final_df = final_df.apply(pd.to_numeric, errors="ignore")
print final_df.dtypes

res = ols(y=final_df['week'], x=final_df[['acousticness','energy','key','loudness','mode','tempo']])
print res
