List1=[1,2,3,4,5,6,7,8]
List2=["a","b","c","d","e"]

dic={List2[j]:List1[j] for j in range(len(List2))}
print(dic)
