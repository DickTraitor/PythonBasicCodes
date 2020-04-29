import json 
counter=0

with open('data.json') as f:
    data=json.loads(f.read())
    for i in data:
        counter=counter+1
    print(counter)
    for i in range(0,counter):
        print(data[i]['work'])