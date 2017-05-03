from musixmatch import matcher

chart = matcher.track(q_track="LoveGame", q_artist="Lady Gaga")
#print(chart)
ly = chart.lyrics()
print(ly['lyrics_body'])
