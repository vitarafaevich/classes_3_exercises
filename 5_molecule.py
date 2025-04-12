dictt = {}

with open('product_data.txt', 'r', encoding='utf8') as f:
    for line in f:
        line = line.strip().split('; ')
        dictt[line[0]] = line[1:]

print(dictt[line[0]][2])
print(len(dictt))
