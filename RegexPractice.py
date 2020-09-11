import pandas as pd
with open('university_towns.txt') as file:
        data = []
        for line in file:
            data.append(line[:-1])
print(data)
    state_town = []
    for line in data:
        if line[-6:] == '[edit]':
            state = line[:-6]
            print(state)
        elif '(' in line:
            town = line[:(line.index('(')-1)]
            print(town)
            state_town.append([state,town])
        else:
            town = line.rstrip()
            state_town.append([state,town])
    print(state_town)
    ans = pd.DataFrame(state_town, columns = ['State','RegionName']) 
    return ans
get_list_of_university_towns()