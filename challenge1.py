from string import maketrans

intab = "abcdefghijklmnopqrstuvwxyz"
outab = "cdefghijklmnopqrstuvwxyzab"
trans = maketrans(intab, outab)

message = raw_input("Enter the message: ")
print message.translate(trans)
