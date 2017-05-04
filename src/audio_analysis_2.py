
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
infile  = open("../audio_features.txt","r")
data = infile.readlines()
infile.close()

tids = []

# write to this file
outfile = open("audio_analysis.txt", "w") 


# first two uris, fetch analysis 
for i in range(len(data)):
    analysis_url = data[i].split("|")[1]
#    print(analysis_url)
#    track_uri = unicode(("spotify:track:" + track_uri).strip('\n'))
#    print(track_uri)
#    tids.append(track_uri)
#    print("line ",str(i) )
#    print(tids)
#    feature = sp.audio_features(str(track_uri))[0]

    
    analysis = sp._get(analysis_url)
#    print()
#    print(json.dumps(analysis['track'], indent = 4))
#    print()

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



# raw_input()
outfile.close()

#features = sp.audio_features(tids)
#for f in features:
#    print(f)

#start = time.time()
#features = sp.audio_features(tids)
#for feature in features: 
#    print(json.dumps(feature, indent=4))
#    print()   
#    analysis = sp._get(feature['analysis_url'])
#    print(json.dumps(analysis, indent=4))
    #print(feature)
#raw_input()
#delta = time.time() - start
#for feature in features:
#    print(json.dumps(feature, indent=4))
#    print()
#    analysis = sp._get(feature['analysis_url'])
#    print(json.dumps(analysis, indent=4))
#    print()
#print ("features retrieved in %.2f seconds" % (delta,))
