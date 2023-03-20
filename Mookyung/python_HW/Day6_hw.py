import matplotlib.pyplot as plt
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
for i in range(-100,101):
    x1.append(i)
    y1.append(i+50)
    x2.append(i)
    y2.append(i-50)
    x3.append(i)
    y3.append(i*-1+50)
    x4.append(i)
    y4.append(i*-1-50)
plt.figure()
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()