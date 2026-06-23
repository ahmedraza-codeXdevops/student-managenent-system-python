data = [1, 2, 2, 3, 1, 4, 2]

frequency = {}

for num in data:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)