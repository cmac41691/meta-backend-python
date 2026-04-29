digits = [3,4,8,12]
evens = []

for number in digits:
  if number % 2 == 0:

      evens.append(number)

print(evens)  

# filter
print([n for n in digits if n % 2 == 0])