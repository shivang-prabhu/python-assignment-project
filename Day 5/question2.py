a=[10,20,40,60,70,80]
b=[5,15,25,35,45,65]
c=[]
i=0
j=0

while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
       
    else:
        c.append(b[j])
        j=j+1
        
while i<len(a) :
    c.append(a[i])
    i=i+1
    
while j<len(b) :
    c.append(b[j])
    j=j+1
  


print(c)

