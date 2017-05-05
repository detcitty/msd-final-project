
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

# write to this file
outfile = open("albums.txt", "w") 

#album_headers = ["album_type","artists","available_markets","copyrights","external_ids", "external_urls","genres","href","id","popularity","release_date","release_date_precision","type","uri"]
# first two uris, fetch analysis 
for i in range(250,len(data)):
    tid = data[i].split("|")[16] # id
    track = sp.track(tid)
    album = sp.album(track["album"]["uri"])
#    print(album)

    album_elements = [

        album["album_type"],
        album["available_markets"],
        album["copyrights"],
        album["genres"],
        album["href"],
        album["id"],
        album["popularity"],
        album["release_date"],
        album["release_date_precision"],
        album["type"],
        album["uri"]

    ]
    for e in range(len(album_elements)):
        album_elements[e] = str(album_elements[e])
    album_string = "|".join(album_elements)
    album_string+="\n"

    outfile.write(album_string)
    print(album_string) 
    

    
#    print(analysis_url)
#    track_uri = unicode(("spotify:track:" + track_uri).strip('\n'))
#    print(track_uri)
#    tids.append(track_uri)
#    print("line ",str(i) )
#    print(tids)
#    feature = sp.audio_features(str(track_uri))[0]

    
#    analysis = sp._get(analysis_url)
#    print()
#    print(json.dumps(analysis['track'], indent = 4))
#    print()



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
