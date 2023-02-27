# c=[]
# def M(c):
#     for i in range(1,10):
#         c.append(i)
#         c.sort()
#         c.reverrse()
#         print(i*c)
# M(4)
# M(7)

a=[]
a.append(50)
print(a)

b=[1,2,3,4]
b.pop()
print(b)

c=[1,3,4,2]
c.clear()
print(c)

d=[3,2,1,4]
d.sort()
print(d)

e=[1,2,3,4]
e.reverse()
print(e)

f=[1,2,3,4]
print(f[2])
print(f[-3])

g=[1,2,3,4]
print(g.index(2))

h=[1,2,3,4,3,3,4]
print(h.count(3))
print(h.count(4))

j=[1,2,3,4]
j.insert(100,1)
print(j)
j.insert(1,40)
print(j)

k=[4,2,3,1]
k.remove(1)
print(k)
k.remove(2)
print(k)

l=[1,3,4,2]
m=[5,7,6,8]
l.extend(m)
print(l)
m.extend(l)
print(m)

n=[1,2,3,4]
o=[5,6,7,8]
print(n+o)
print(n+[5,6,7,8])

p=[1,2,3,4,5]
print(len(p))
q=[1,1,1,1,1,1,1]
print(len(q))

i=[1,3,5,4,2]
i.sort()
i.reverse()
for i in i:
    print(i)
