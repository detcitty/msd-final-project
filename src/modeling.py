import numpy as np
import pandas as pd
from pandas.stats.api import ols
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

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

###############################################################################

infile = open("audio_analysis_uri.txt","r")
audio_analysis = infile.readlines()
infile.close()

features = []
for i in range(18):
    f = []
    features.append(f)

for i in range(len(audio_analysis)):
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

#print audio_analysis_df.dtypes
#print list(audio_analysis_df)

###############################################################################


from lyric2vec import get_lyric_dict

lyric_dict, names= get_lyric_dict()
#print type(lyric_dict)
lyric_dict_df = pd.DataFrame.from_dict(data=lyric_dict,orient='index')

indices = lyric_dict_df.index.values.tolist()
indices = [i.rstrip() for i in indices]
lyric_dict_df['song'] = indices

##############################################################################


uri_songs_weeks_df = pd.merge(track_uri_df, song_ranks_weeks, on='song', how='inner')
print 'uri_song_weeks_df: ', len(uri_songs_weeks_df)
temp_df = pd.merge(uri_songs_weeks_df, lyric_dict_df, on="song", how="inner")
print 'temp_df: ', len(temp_df)
final_df = pd.merge(temp_df, audio_features, on='uri', how='inner')
print 'final_df', len(final_df)
final_analysis_df = pd.merge(final_df, audio_analysis_df, on='uri', how="inner")
print 'final_analysis_df', len(final_analysis_df)
#Removing week to predict rank, will remove rank to predict week later
final_analysis_df.drop('week', axis=1, inplace=True)
print list(final_analysis_df)

cols = [col for col in final_analysis_df.columns if col not in ['rank']]
for i in range(1,18):
    cols.append(header_names[i])
print cols

#Changing datatypes of dataframe columns
drop_columns = ['song','uri','danceability','speechiness','instrumentalness','valence','liveness']
final_analysis_df.drop(drop_columns, axis=1, inplace=True)
final_analysis_df = final_analysis_df.apply(pd.to_numeric, errors="ignore")
print final_analysis_df.dtypes
print len(final_analysis_df)

predictor_columns = ['acousticness','energy','key','loudness','mode','tempo']
#scaler = MinMaxScaler()
#final_analysis_df[predictor_columns] = scaler.fit_transform(final_analysis_df[predictor_columns])
for i in range(1,18):
    predictor_columns.append(header_names[i])
print final_analysis_df[predictor_columns]
for col in list(lyric_dict_df):
    if col != "song": 
        predictor_columns.append(col)


#for i in range(5000):
#    predictor_columns.append(lyric_dict_df.columns.values)
res = ols(y=final_analysis_df['rank'], x=final_analysis_df[predictor_columns])
print res

#msk = np.random.rand(len(final_analysis_df)) < 0.8
#dftrain = final_analysis_df[msk]
#dftest = final_analysis_df[~msk]
#
#ytrain = dftrain["rank"].values
#xtrain = dftrain[predictor_columns].values
#
#ytest = dftest["rank"].values
#xtest = dftest[predictor_columns].values
#
#reg = linear_model.RidgeCV(cv=5)
#reg.fit(xtrain, ytrain)
#ypred = reg.predict(xtest)
#mse = mean_squared_error(ytest, ypred)
#print("MSE:", mse)
#print("Coefficients:", reg.coef_)
#print("Intercepts:", reg.intercept_)
#print("Best Alpha:", reg.alpha_)
#print("Model Score:", reg.score(xtest, ytest))
