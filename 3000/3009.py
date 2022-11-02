xindex = []
yindex = []

for i in range(3):
    x, y = map(int, input().split())
    if x in xindex:
        xindex.remove(x)
    else:
        xindex.append(x)
        
    if y in yindex:
        yindex.remove(y)
    else:
        yindex.append(y)
        
print(xindex[0], yindex[0])