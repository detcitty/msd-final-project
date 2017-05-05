# starter code for reading in audio features
import numpy as np
import pandas as pd

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

print list(audio_features)
print audio_features[:1] 
