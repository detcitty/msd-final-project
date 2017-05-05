
# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
from math import ceil
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
outfile = open("albums.txt", "w") 

#album_headers = ["album_type","artists","available_markets","copyrights","external_ids", "external_urls","genres","href","id","popularity","release_date","release_date_precision","type","uri"]
# first two uris, fetch analysis 
#for i in range(2):
# buckets

# tracks limit
limit = 50
start = 0

# intervals 
intervals = int(ceil(len(data)//50))
print ("interv", intervals)
tracks_list = [] 
for i in range(len(data)):
    tid = data[i].split("|")[16] # id
    tids.append(tid)

for i in range(intervals):
    if limit > len(tids):
        limit = len(tids)
    subarray = []
    for j in range(start, limit): 
        subarray.append( tids[j] )
    tracks = sp.tracks(subarray)
    tracks_list.append(tracks) 
    start = limit 
    limit += 50
    
#range(start, limit):
#        sub
#       tracks = sp.tracks(
        
    
track_num = 0

album_ids = []
for i in range(len(tracks_list)): 
    # max 20 ids per album 
    tracks = tracks_list[i]
    for track in tracks["tracks"]: 
        album_ids.append(track["album"]["uri"]) 

intervals = int(ceil(len(album_ids) // 20))

limit = 20
start = 0

albums_list = [] 

for i in range(intervals): 
    if limit > len(album_ids):
        limit = len(album_ids)
    subarray = []
    for j in range(start, limit): 
        subarray.append(album_ids[j])
    albums = sp.albums(subarray)
    albums_list.append(albums) 
    start = limit 
    limit += 20

for i in range(len(albums_list)):
    albums = albums_list[i]

    for album in albums["albums"]: 
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