       # any repition is been called offf
       # a=hello
        #a=helo

# create a list and then use for loop to see if that
l=[]
no_duplicates=[]
a=input("enter a string:")
for i in a:
    l.append(i)

for i in l:
    if i not in no_duplicates:
        no_duplicates.append(i)
no_duplicates="".join(no_duplicates)
print(no_duplicates)