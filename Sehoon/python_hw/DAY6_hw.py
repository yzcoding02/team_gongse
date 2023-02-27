# method,function,list,for 최소 한번씩 다 사용한 예제 만들어오기

# 1.append,pop,clear
fs=["apple","banana","cherry"]
fs.append("wateremelon")
print(fs)
fs.pop()
print(fs)
fs.clear()
print(fs)

# 2.sort,reverse
fs=["banana","cherry","apple"]
fs.sort()
print(fs)
fs.reverse()
print(fs)

# 3.index,count
fs=["apple","banana","cherry","apple"]
print(fs[0])
print(fs[1])
print(fs[2])
print(fs[-1])
print(fs[-2])
print(fs[-3])
print(fs.count("apple"))
print(fs.count("banana"))
print(fs.count("wateremelon"))

# 4.insert,remove
fs=["apple","banana","cherry"]
fs.insert(1,"wateremelon")
print(fs)
fs.remove("wateremelon")
print(fs)

# 5.extend,+
fs1=["apple","banana"]
fs2=["cherry","wateremelon"]
fs1.extend(fs2)
print(fs1)
fs1=["apple","banana"]
fs2=["cherry","wateremelon"]
print(fs2+fs1)

# 6.그외(len)
fs=["apple","banana","cherry"]
print(len(fs))

# 7.for(ex)
f=["banana","cherry","apple"]
f.append("wateremelon")
f.sort()
f.reverse()
for i in range(len(f)):
    print(f[i])
fs=["banana","cherry","apple"]
fs.sort()
fs.reverse()
for f in fs:
    print(f)