#!/bin/python/
'''
Devin Etcitty
Modeling Social Data
dce2108
Jacob Hofman

source: https://github.com/plamere/spotipy
'''
import spotipy
import csv
import sys
import time

sp = spotipy.Spotify()
limit = 20


if len(sys.argv) > 1:
    csv_file = sys.argv[1]

with open(csv_file, newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        artist = row[0]
        results = sp.search(artist, limit)
        for i, t in enumerate(results['tracks']['items']):
            print(' ', i, t['name'])
        time.sleep(15)
