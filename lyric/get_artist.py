from musixmatch import matcher
import csv

data = "./../data/"
billboard = "us_billboard.psv"
billboard_25 = "us_billboard_25.psv"

file_open = data + billboard

with open(file_open) as f:
    reader = csv.reader(f, delimiter="|")
    file_of_data= [line for line in reader]

    for line in file_of_data:
        track = line[4]
        artist = line[5]

        print(track + " " + artist )


#chart = matcher.track(q_track="LoveGame", q_artist="Lady Gaga")
#print(chart)
#ly = chart.lyrics()
#print(ly['lyrics_body'])
