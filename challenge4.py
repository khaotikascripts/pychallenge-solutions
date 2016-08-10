#Title: follow the chain
#Hint: urllib may help. DON'T TRY ALL NOTHINGS, since it will never end.
#      400 times is more than enough.
import urllib
import string

nothing = urllib.urlencode({'nothing':12345})

for i in range(400):
    f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % nothing)
    response = f.readline() #Response: and the next nothing is xxxxx
    print response
    words = string.split(response)
    nothing = urllib.urlencode({'nothing':words[len(words)-1]})
#Answer: peak.html
