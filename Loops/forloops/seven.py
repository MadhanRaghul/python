# for loops - break and continue with list

list=['one','two','three','four','five','six','seven']

for x in list:
    if x=='five':
        break
    print(x)

print("----------------------------")

for x in list:
    if x=='five':
        continue
    print(x)