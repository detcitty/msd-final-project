# shows audio analysis for tracks for the given artist

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
infile  = open("../audio_features.txt","r")
data = infile.readlines()
infile.close()

tids = []

# write to this file
outfile = open("audio_analysis_3.txt", "w") 


# for all uris, fetch analysis 
#for i in range(1942, len(data)):
#print("8476", len(data))
for i in range(8476, len(data)):
    analysis_url = data[i].split("|")[1]

    
    analysis = sp._get(analysis_url)

    analysis_elements = [
	analysis["track"]["mode_confidence"],
	analysis["track"]["end_of_fade_in"],
	analysis["track"]["key_confidence"],
	analysis["track"]["synch_version"],
	analysis["track"]["duration"],
	analysis["track"]["rhythm_version"],
	analysis["track"]["time_signature_confidence"],
	analysis["track"]["start_of_fade_out"],
	analysis["track"]["analysis_sample_rate"],
	analysis["track"]["tempo"],
	analysis["track"]["offset_seconds"],
	analysis["track"]["tempo_confidence"],
	analysis["track"]["key"],
	analysis["track"]["mode"],
	analysis["track"]["time_signature"],
	analysis["track"]["num_samples"],
	analysis["track"]["loudness"]
]
    for e in range(len(analysis_elements)):
        analysis_elements[e] = str(analysis_elements[e])
    analysis_string = "|".join(analysis_elements)
    analysis_string+= "\n"
    outfile.write(analysis_string)
    print(analysis_string)

outfile.close()


