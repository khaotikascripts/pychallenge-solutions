import zipfile
import string

comment = "" #Collect the comments!!
nothing = 90052

with zipfile.ZipFile('./channel.zip', 'r') as z:
    for i in range(len(z.namelist())):
        name = str(nothing) + '.txt' #nothing should be an int
        try:
            comment += z.getinfo(name).comment
        except KeyError:
            break
        f = z.open(name) #If getinfo() works, so will this
        words = string.split(f.readline())
        nothing = words[len(words)-1]
        f.close()

print comment #Answer: oxygen
