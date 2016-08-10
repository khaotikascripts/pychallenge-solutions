import pickle

f = open('ch5.p', 'rb')
banner = pickle.load(f)
f.close()

for i in banner:
    line = ""
    for j in i:
        line = line + (p[0] * p[1])
        #this replaces a 3rd for loop:
        #for k in range(j[1]):
        #    line = line + j[0]
    print line
#Answer: channel
