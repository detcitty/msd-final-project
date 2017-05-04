# for reading audio_features.txt
# pass in file path 
# returns list of features dictionaries of string keys and values

def read_audio_features(filename): 
    infile = open(filename, "r") 
    data = infile.readlines()
    infile.close()
    features = []

    for i in range(len(data)): 
        elements = data[i].split("|")
        feature = dict() 
        feature["track_href"] = elements[0]
        feature["analysis_url"] = elements[1]
        feature["energy"] = elements[2]
        feature["liveness"] = elements[3]
        feature["tempo"] = elements[4]
        feature["speechiness"] = elements[5]
        feature["uri"] = elements[6]
        feature["acousticness"] = elements[7]
        feature["instrumentalness"] = elements[8]
        feature["time_signature"] = elements[9]
        feature["danceability"] = elements[10]
        feature["key"] = elements[11]
        feature["duration_ms"] = elements[12] 
        feature["loudness"] = elements[13]
        feature["valence"] = elements[14]
        feature["type"] = elements[15]
        feature["id"] = elements[16]
        feature["mode"] = elements[17].strip()

        features.append(feature) 

    return features
        
    

