# Checking for sorting input  
n=int(input())
while n>0:
  s=input()
  li=[]
  li=s.split(" ")
  li.sort()
  str=""
  for i in range(0,len(li)-1):        
    str=str+li[i]+" "    
  str=str+li[len(li)-1]        

  # Checking for reverse sorted         
  str1=""    
  for i in range(len(li)-1,0,-1):        
    str1=str1+li[i]+" "    
  str1=str1+li[0]    

  if str==s or str1==s:        
    print(s)
