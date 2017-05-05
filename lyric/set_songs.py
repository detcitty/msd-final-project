
data_lyrics = "song_names.txt"
songs = "songs.txt"

with open(data_lyrics, "r") as s:
    with open(songs, "r") as to:
        dic = s.readlines()
        set_names = to.readlines()
        
        #print(dic)
        #print(set_names)
        
        union = set(dic) & set(set_names)
        print(union)

        s = open("union_songs_db.txt", "w+")
        s.writelines(union)
        s.close()
