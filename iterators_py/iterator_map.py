a = map(lambda x:x*x,range(10))
b = iter(a)
print(b)
c = b.__next__()
d = b.__next__()
e = b.__next__()
print(c)
print(d)
print(e)
print(list(b))