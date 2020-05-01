'''
This is a basic code of exception handling .. It says to stop the loop of taking integers as input when we write done until then we have to take input
after writing done we have to print the maximum number input and the minimum number input
'''

number_list=[]
while True:
    number=(input())
    if number=='done':
        break
    try:      # the operation that you want to try 
        number_int=int(number)
        number_list.append(number_int)
    except: # if that operation fails then what to do ..
        print('Invalid input') 

print("list is :",number_list)
print('Maximum is ',max(number_list))
print('Minimum is ',min(number_list))
        
        
        
        
        
        
        
        
        
        
        
        