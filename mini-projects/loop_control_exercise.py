num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,53,67,89,11]
count = 0

for index, number in enumerate(num_list):

    count = count + 1
    print(number)

    if number == 36:
        print(index)
        break

    if number > 45:
        print("Over 45")
    else:
        print("Under 45")

# After loop
print(count)