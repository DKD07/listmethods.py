l=[11,45,1,2,4,6,1,1]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m=l.copy()
m[0]=0
print(l)
l.insert(1,899)
m=[999,1000,1200]
l.extend(m)
print(l)
k=l+m
print(k)