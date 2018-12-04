with open('./input.txt') as f:
    content = f.readlines()

ids = [x.strip() for x in content]

id_a = ''
id_b = ''
smaller_diff = 9999

def cmp(a,b):
    result = 0
    for l in range(len(a)):
        if a[l] != b[l]:
            result = result + 1
    return result

for i in range(len(ids)):
    next_words = ids[i+1:]
    for j in range(len(next_words)):
        diff = cmp(ids[i], next_words[j])
        if diff < smaller_diff:
            smaller_diff = diff
            id_a = ids[i]
            id_b = next_words[j]

common = ''

for l in range(len(id_a)):
    if id_a[l] == id_b[l]:
        common = common + id_a[l]


print(smaller_diff)
print(id_a)
print(id_b)
print('---------------------------')
print(common)

