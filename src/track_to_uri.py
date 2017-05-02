import spotipy

spotify = spotipy.Spotify()
name = "shape of your machine learning"
results = spotify.search(q='track:'+name, type='track')
items = results['tracks']['items']
song = items[0]
track_uri = song = items[0]['uri']
print track_uri

#ADD ERROR HANDLING TO THIS
#WHAT HAPPENDS WHEN WE CANT FIND THE SONG
