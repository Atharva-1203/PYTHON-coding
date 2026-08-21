l=[1,2,3,4,5,6]
print(len(l))

l.append(20)
print(l)

l.extend([9,7,6])
print(l)

l.insert(3,100)
print(l)

l.remove(7)
print(l)

l.pop()
print(l)

l.pop(4)
print(l)

print(min(l))  #O(n)
print(max(l))  #O(n)

print(l.count(100))

l.reverse()    #O(n)
print(l)

l.sort()   #O(nlogn)
print(l)

l.sort(reverse=True)
print(l)

print(l.index(4))

l.clear()
print(l)
