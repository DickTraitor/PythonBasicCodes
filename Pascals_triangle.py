'''
In this we are implementing the pascals traingle 
                                1                       0
                            1       1                   1
                        1       2       1               2
                    1       3       3       1           3   
                1       4       6       4       1       4
                                or
                                0!/0!                   0
                            1!/1!   1!/1!               1  
                      2!/2!   2!/1!1!   2!/2!           2
                  3!/3!  3!/2!1!     3!/1!2!  3!/3!     3 
'''
import math
row_num = 5
for row in range(row_num):
    for i in range(row+1):  # number of elements in 1 row are row+1
        # calculate the binomial coefficient
        if row==0:
            print(1,end=" ")
            break
        else:
            print(int(math.factorial(row)/(math.factorial(row-i)*math.factorial(i))),end=" ")
    print("\n")