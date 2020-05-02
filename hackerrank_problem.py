                               # this is not the best solution but worked in my editor
'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N , the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints
2<=N<=5

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
'''

main=[] # the big list 

number_students=int(input(" enter the number of students:"))

for i in range(0,2*number_students,1):
    # take the input in a new list and that list must be appended in the main list
    main.append(input().split())   # split is used to make the text into list format # input simultaneously splitting into the string into list

grades=[]  # a new list of grades
# now we would be picking every marks in the list of main and then we would be putting that in grades list..

for i in range(0,len(main),2):  # iterating over every second item in list as that would be the number
   grades.append(main[i+1])    # appending the marks of students
print('main===>',main)
 # now we have all the list of grades and ow we want to print the list of second lowest grades.
second_lowest=[] 
# we would sort the grades and then see second lowest
grades.sort()
print('grades--->>',grades) 
second_lowest.append(grades[1])
# now we would be checking in duplicies in the list if there are we would be printing them
for i in range(0,len(grades),1):
    if grades[i]==grades[1] and i !=1:
        second_lowest.append(grades[i])
print(second_lowest)
# after this we would be comparing the second_lowest list to the main list and see if the elements in the list matches then we would   putting it in a new list called as final_answer
final_answer=[]

for i in range(0,(2*number_students)-1,2):   # terating over the list of main and selecting just marks out of them 
    for j in range(0,len(second_lowest),1):
        if second_lowest[j]==main[i+1]:
            final_answer.append(main[i])
# now that we may have duplicates in the list in pyhton
# we have to remove the duplicates from the list
print(final_answer)  # when we see the final answer there is one problem repetition now we would be converting the ested list to a flat list and then seeing it
flat_list=[]
for i in range(0,len(final_answer),1):
    flat_list.append(final_answer[i][0])
print(flat_list)
flat_list = list(dict.fromkeys(flat_list))
print(flat_list)
# now we have to name it alpahbetically...
flat_list=sorted(flat_list)
print(flat_list)
