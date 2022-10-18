#dictionary related questions and answers

#1.Remove duplicates from Dictionary :  Based on keys it is not possible
dict1  = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}
temp = []
result = {}
for key, value in dict1.items():
    if value not in temp:
        temp.append(value)
        result[key]=value

print(result)
dict1 = {'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}

temp = {val: key for key, val in dict1.items()}
res = {val: key for key, val in temp.items()}

print(res)

