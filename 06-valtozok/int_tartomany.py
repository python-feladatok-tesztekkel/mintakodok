a, b, c = 3, 2, 1
while c < 30:
     print(c, b, type(b),sep=':')
     a, b, c = b, a*b, c+1
