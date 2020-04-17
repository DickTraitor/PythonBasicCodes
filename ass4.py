

                            #swap casing in python
for i in word[0::1]:
    if ord(i)>=97 and ord(i)<=123:
        capital_ascii=ord(i)-32
        print(chr(capital_ascii),end="")
    elif ord(i)>=65 and ord(i)<= 91:
        lower_ascii=ord(i)+32
        print(chr(lower_ascii),end="")
    else:
        print(i,end="")
