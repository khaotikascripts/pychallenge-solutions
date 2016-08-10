#Find all occurences of a single lowercase letter inbetween 3 uppercase letters
import re
pattern = re.compile('[a-z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]+')

junkfile = open("ch3_junk.txt", "r")
junk = junkfile.read()
junkfile.close()

result = pattern.finditer(junk)
if result:
    for match in result:
        print match.group()
#Answer: linkedlist.php
