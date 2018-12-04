import sys

with open('./input.txt') as f:
    content = f.readlines()
numbers = [ (int(n[1:]) * (-1 if (n[:1]=='-') else 1))  for n in [x.strip() for x in content]]
frequency_value = 0
frequencies_already_hit = {}
while True:
    for number in numbers:
        frequency_value = frequency_value + number
        if frequency_value in frequencies_already_hit:
            print(frequency_value)
            sys.exit(0)
        frequencies_already_hit[frequency_value] = 1
