# problem link: http://www.vpropel.in/code-test/attend-pod-test/103

s1=input()
s2=input()
str1=""
for i in s1:
  if i==":":
    str1=str1+"#"
  else:
    str1=str1+i

str2=""
for i in s2:
  if i=="#":
    str2=str2+":"
  else:
    str2=str2+i

print(str2)
print(str1)
