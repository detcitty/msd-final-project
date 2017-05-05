import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text

def get_lyric_dict():

    infile = open("../lyric/sorted_union_songs_db.txt","r")
    names = infile.readlines()
    infile.close()

    def get_lyrics(temp):
        for i in range(len(temp)):
            element = temp[i].strip().lower()
            temp[i] = element
        lyric_string = " ".join(temp)
        lyric_string = re.sub(r'[^\w\s]','',lyric_string)
        return lyric_string

    lyrics = []
    for i in range(len(names)):
        print i, names[i].lower().rstrip()
        infile = open("../lyric/backup/output/"+names[i].lower().rstrip()+'.txt',"r")
        if not infile:
            continue
        temp = infile.readlines()    
        lyrics.append(get_lyrics(temp))
        print lyrics[i]

    stop_words = text.ENGLISH_STOP_WORDS
    vectorizer = CountVectorizer(stop_words = stop_words, max_features=5000,strip_accents="ascii")

    #TODO: separate into xtrain and ytrain, corresponding to our xtrain and ytrain
    # or else, do a separate model. 
    dtm = vectorizer.fit_transform(lyrics)
    vocab = vectorizer.get_feature_names()

    # convert to regular arrays for classifier 
    dtm = dtm.toarray()
    vocab = np.array(vocab)

    print dtm.shape

    lyric_dict = dict()

    for i in range(len(names)):
        lyric_dict[names[i]] = dtm[i]

    return lyric_dict
