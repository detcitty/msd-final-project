import numpy as np
import pandas as pd
from lyric2vec import get_lyric_dict

lyric_dict, names= get_lyric_dict()
print type(lyric_dict)
lyric_dict_df = pd.DataFrame.from_dict(data=lyric_dict,orient='index')

indices = lyric_dict_df.index.values.tolist()
indices = [i.rstrip() for i in indices]
lyric_dict_df['song'] = indices
#for name in names: 
#    lyric_dict_df.loc[name,'song'] = name

print list(lyric_dict_df)
print lyric_dict_df['song']
#print lyric_dict_df.keys()
