line = input()

list_old = line.replace("-e ", "").split(" ")

list_final = []

for name in list_old:
    if name.lower() not in list_final:
        list_final.append(name.lower())


for name in list_final:
    print("-e ",name," ",end='')
