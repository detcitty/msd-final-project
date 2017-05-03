
infile  = open("track_uri.txt","r")
data = infile.readlines()
infile.close()

for i in range(10):
    print data[i]
