# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys

# authentification
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

# read file
infile  = open("track_uri.txt","r")
data = infile.readlines()
infile.close()

tids = []

# write to this file
outfile = open("audio_features.txt", "w") 

# for all uris fetch features
for i in range(len(data)):
    track_uri = data[i].split("|")[1].split(":")[-1]
    track_uri = unicode(("spotify:track:" + track_uri).strip('\n'))
    print(track_uri)
    tids.append(track_uri)
    print("line ",str(i) )
    feature = sp.audio_features(str(track_uri))[0]

    feature_elements = [feature["track_href"],
			feature["analysis_url"],
			feature["energy"],
			feature["liveness"],
			feature["tempo"],
			feature["speechiness"],
			feature["uri"],
			feature["acousticness"],
			feature["instrumentalness"],
			feature["time_signature"],
			feature["danceability"],
			feature["key"],
			feature["duration_ms"],
			feature["loudness"],
			feature["valence"],
			feature["type"],
			feature["id"],
			feature["mode"]]
    for e in range(len(feature_elements)):
        feature_elements[e] = str(feature_elements[e])
    feature_string = "|".join(feature_elements)
    feature_string += "\n"
   
    outfile.write(feature_string) 
    
    print(feature_string)
    
outfile.close()

