
    with open(f,"r+") as o:
    
        x = o.readlines()
        
        with open(f, "w") as me:
            me.writelines(x)
        
        print(x)
        if (len(x) == 0):
            #os.remove(f)
            continue
        else:
            o.writelines(x[:-4])

