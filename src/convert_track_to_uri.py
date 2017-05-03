import os
import spotipy

spotify = spotipy.Spotify()

infile = open('song_names.txt')
data = infile.readlines()
infile.close()
num_songs = len(data)

outfile = open("track_uri.txt", 'w')

for i in range(num_songs):
    name = data[i].strip()
    results = spotify.search(q='track:'+name, type='track')
    items = results['tracks']['items']
    if not items:
        continue
    track_uri = items[0]['uri']
    print name, track_uri
    outfile.write(name + '|' + track_uri + '\n')

#ADD ERROR HANDLING TO THIS
#WHAT HAPPENDS WHEN WE CANT FIND THE SONG
