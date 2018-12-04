with open('./input.txt') as f:
    content = f.readlines()

ids = [x.strip() for x in content]

def count_repetitions(word):
    letters = {}
    for letter in word:
        if letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1

    two = 0
    three = 0
    for _,count in letters.items():
        if count == 2:
            two = 1
        elif count == 3:
            three = 1
    return (two, three)

print('------------------------')
print('ff')
print(count_repetitions('abcdef'))
print('tt')
print(count_repetitions('bababc'))
print('tf')
print(count_repetitions('abbcde'))
print('ft')
print(count_repetitions('abcccd'))
print('tf')
print(count_repetitions('aabcdd'))
print('tf')
print(count_repetitions('abcdee'))
print('ft')
print(count_repetitions('ababab'))
print('------------------------')

count_rep_file = [count_repetitions(id_str) for id_str in ids]
sums = [sum(x) for x in zip(*count_rep_file)]
print(sums[0] * sums[1])
