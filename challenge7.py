import re, Image

i = Image.open('oxygen.png')
w, h = i.size

#i.getpixel((0,h//2)) = (115, 115, 115, 255) => chr(115) = 's'
row, ords = []
#row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
for x in range(0, w, 7):
    row.append(i.getpixel((x, h//2)))
#ords = [r for r, g, b, a in row if r == g == b]
for r, g, b, a in row:
    if r == g == b:
        ords.append(r)

#smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(map(chr, map(int, re.findall('\d+', ''.join(map(chr, ords))))))
#==> 'integrity'
