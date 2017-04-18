#!/bin/python/
'''
Devin Etcitty
Modeling Social Data
dce2108
Jacob Hofman

source: https://github.com/plamere/spotipy
'''
import spotipy
sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])
