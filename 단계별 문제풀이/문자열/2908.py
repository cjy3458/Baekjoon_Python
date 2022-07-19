from imp import NullImporter


a, b = input().split()
c = ''
d = ''

for i in a:
    c = i + c

for _ in b:
    d = _ + d

if c > d:
    print(c)
else:
    print(d)
