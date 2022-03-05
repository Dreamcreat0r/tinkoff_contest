a, b, c, d = input().split()
if int(d)-int(b) >= 0:
    s = int(a) + (int(d)-int(b))*int(c)
else:
    s = a
print(s)