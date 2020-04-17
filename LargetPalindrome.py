# print the largest palindrome possible from two numbers with 3 digits

result=[]
for i in range(100,1000):
    for j in range(100,1000):
        if (i*j)==(j*i):
            result.append(i*j)
print(max(result))

# printing all 3 digit palindrome in python
result=[]
for i in range(100,1000):
    temp=i
    rev=0
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
    if(temp==rev):
        result.append(temp)
print(result)

