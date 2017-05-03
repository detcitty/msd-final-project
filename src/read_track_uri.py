import spotipy

client_credentials_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
spotify.trace=False

#spotify = spotipy.Spotify()

infile  = open("track_uri.txt","r")
data = infile.readlines()
infile.close()

for i in range(2):
    track_uri = data[i].split("|")[1].split(":")[-1]
    print(track_uri)
    feature = spotify.audio_features(str(track_uri))[0]
    print(feature)
    raw_input()
