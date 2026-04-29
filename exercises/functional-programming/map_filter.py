digits = [3,4,8,12]

list_result = []

for number in digits:

 new_value = number * 2
 list_result.append(new_value)

print(list_result)

# map
print([n * 2 for n in digits])