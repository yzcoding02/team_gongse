import matplotlib.pyplot as plt
x=[]
y=[]
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in range(-100,101):
    x.append(i)
    y.append(i+50)
    x1.append(i)
    y1.append(i-50)
    x2.append(i)
    y2.append(i*-1+50)
    x3.append(i)
    y3.append(i*-1-50)
plt.figure()
plt.plot(x,y,x1,y1,x2,y2,x3,y3)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

