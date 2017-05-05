
infile = open("audio_features.txt")
audio_features = infile.readlines()
infile.close()

infile = open("audio_analysis.txt")
audio_analysis = infile.readlines()
infile.close()

outfile = open("audio_analysis_uri.txt","w")
for i in range(len(audio_analysis)):
    uri = audio_features[i].split('|')[6].split(':')[-1].rstrip()
    outfile.write(uri + '|' + audio_analysis[i])
