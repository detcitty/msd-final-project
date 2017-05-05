import os

path_name = "db_lyrics/"


numline=3 #3 lines to skip

for (dirpath, dirnames, filenames) in walk("."+path_name):
        
    with open(filenames,"w+") as o:

    for i in range(numline):
    f.next()
    for line in f:
        if p:
            o.write(p)
    p=line
    f.close()
    o.close()
    print(os.listdir("."))
