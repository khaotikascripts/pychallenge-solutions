#Find rare characters in the junk file
junkfile = open("ch2_junk.txt", "r")
junk = junkfile.read()
junkfile.close()

uniques = ""
for ltr in junk:
    if ltr not in uniques:
        uniques += ltr

for uniq in uniques:
    print uniq + ": " + str(junk.count(uniq))
