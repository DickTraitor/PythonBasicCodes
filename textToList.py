'''
This is a program about the creation of list from the words. It takes the inspiration 
from sklearn.count_vectorizer and it's just a small Part of it..
'''
text = "Raghav Narula raghav narula "

# will treat upper and lower words as same
    # my own split function coz it will help me in adding things on my own...

count = 0
list1 = []
list2 = []
for i in range(len(text)):
    if text[i] == " ":
        word = "".join(list1)
        print(word)
        # searching for word that it is present in the list before or not..
        if len(list2)==0:
            list2.append(word)
        elif list2 is not None:
            for element in list2:
                print(element.lower(),"<<<<<<",word)
                if element.lower() != word:
                    list2.append(word)

                    
        list1=[]
    if text[i] != " ":
        list1.append(text[i])
    # for the last word..
    # if i == len(text):
    #     word = "".join(list1)
    #     print(word,"---<<")
print(list2)
# now this is in the list and we want to check wheather the list has the word or not ..
