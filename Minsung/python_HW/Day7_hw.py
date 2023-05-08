import matplotlib.pyplot as plt
x=[]
y=[]
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
figure,axes=plt.subplots(1,2)
fruits=["korean","math","computer"]
counts=[40,30,90]
bar_color=["red","yellow","purple"]
axes[0].bar(fruits,counts,color=bar_color)
for i in range(-100,101):
    x.append(i)
    y.append(5)
    x1.append(i)
    y1.append(-5)
    x2.append(i)
    y2.append(i*1+20)
    x3.append(i)
    y3.append(i*-1+20)
    axes[1].plot(x,y,x1,y1,x2,y2,x3,y3)
plt.show()


# import matplotlib.pyplot as plt
# figure,axes=plt.subplots(1,2)
# subjects=["korean","math","computer"]
# counts=[40,30,90]
# bar_color=["red","green","blue"]
# x=[]
# y1=[]
# y2=[]
# y3=[]
# y4=[]
# for i in range(-10,11):
#     x.append(i)
#     y1.append(5)
#     y2.append(-5)
#     y3.append(i*3+20)
#     y4.append(-i*3+20)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# axes[0].barh(subjects,counts,color=bar_color)
# axes[1].plot(x,y1,x,y2,x,y3,x,y4)
# plt.show()