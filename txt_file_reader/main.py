#file reader
file = open('C:\\Users\\dvillalva\Desktop\\scripts\\practice_water_oracle.txt', 'r')

rl = file.readlines()

new = []

for line in rl: 
    new.append(line.strip())

    # if line[-1] == '\n':
    #     new.append(line[:-1])
    # else
    #     new.append(line)
file.close
#print(new)

#convert list into string
k = str(new)

#find "from" in list

num_select = k.find('select')
num_from = k.find('from')
num_tracker = num_from
num_where = k.find('where')
print(f'Select:{num_select} From:{num_from} Where:{num_where}')
#find comma's between from and where 
comma = []
print(num_tracker) #79

while num_tracker < num_where:
    comma.append(k.find(',', num_tracker))
    print(f'Comma List:{comma}')
    num_tracker = k.find(',', num_tracker)
    num_tracker += 1

print(k[90:187])

print("ye")
# strip() 