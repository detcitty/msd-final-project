from musixmatch import matcher

chart = matcher.track(q_track="LoveGame", q_artist="Lady Gaga")
print(chart)

if(chart["has_lyrics"]):
    ly = chart.lyrics()
    print(ly['lyrics_body'])
