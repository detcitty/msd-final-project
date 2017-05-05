from musixmatch import matcher
import csv
import os

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

        file_lyrics = track.lower() +"*"+ ".txt"

        if(os.path.isfile(file_lyrics)):
            continue
        else:
            try:
                chart = matcher.track(q_track=track, q_artist=artist)
                ly = chart.lyrics()

                with open("./output/" + file_lyrics, "w+") as s:
                    lyric = ly['lyrics_body']

                    s.write(lyric.encode('utf-8'))
            except Exception as e:
                continue

        print(track + " " + artist )


