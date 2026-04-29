word = input("Enter in a word:")

reversed_string = ""

for character in word[::-1]:
   reversed_string += character

print(reversed_string)

# reverse
print(word[::-1])
