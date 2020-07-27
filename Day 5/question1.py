a=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
a.sort()

for each in a:
        if(each==0):
            a.remove(each)
            a.append(0)

print(a)

