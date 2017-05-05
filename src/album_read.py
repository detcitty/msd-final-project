# for reading albums.txt
# pass in file path 
# returns list of albums dictionaries of string keys and values

def read_albums(filename): 
    infile = open(filename, "r")
    data = infile.readlines()
    infile.close()
    albums = []

    for i in range(2): 
        elements = data[i].split("|")
        album = dict() 
        album["album_type"] = elements[0]
        album["available_markets"] = elements[1]
        album["copyrights"] = elements[2]
        album["genres"] = elements[3]
        album["href"] = elements[4]
        album["id"] = elements[5]
        album["popularity"] = elements[6]
        album["release_date"] = elements[7]
        album["release_date_precision"] = elements[8]
        album["type"] = elements[9]
        album["uri"] = elements[10]

        albums.append(album) 

    return albums
        
    

