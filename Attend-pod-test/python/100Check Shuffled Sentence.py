# problem link: http://www.vpropel.in/code-test/attend-pod-test/100

s1=input()
s2=input()
l1=[]
l2=[]
l1=s1.split(" ")
l2=s2.split(" ")
l1.sort()
l2.sort()
if l1==l2:
  print("Yes")
else:
  print("No")
