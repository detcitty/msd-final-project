import os
for filename in os.listdir('.'):
    old_name = filename
    new_name = filename.replace('*','')
    os.rename(old_name, new_name)
