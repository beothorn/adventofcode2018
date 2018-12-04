with open('./input.txt') as f:
    content = f.readlines()
content = sum([ (int(n[1:]) * (-1 if (n[:1]=='-') else 1))  for n in [x.strip() for x in content]])
print(content)
