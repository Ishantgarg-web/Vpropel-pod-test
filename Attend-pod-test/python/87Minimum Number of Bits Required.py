# problem link: http://www.vpropel.in/code-test/attend-pod-test/87

import math
n=int(input())
li=[]
x=input()
li=x.split()
max1=0
for i in li:
  max1=max(max1,int(i))
  
count=0
while math.pow(2,count)<max1:
  count+=1

print(count)
