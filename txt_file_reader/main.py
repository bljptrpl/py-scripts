#file reader
file = open('C:\\Users\\dvillalva\Desktop\\scripts\\practice_water_oracle.txt', 'r')

rl = file.readlines()

new = []

for line in rl: 
    new.append(line.strip())

file.close

#convert list into string
k = str(new)
#find "from" in list

num_select = k.find('select')
num_from = k.find('from')
num_tracker = num_from
num_where = k.find('where')
print(f'Select:{num_select} From:{num_from} Where:{num_where}')
#find comma's between from and where 
spaces = []
while (k.find(' ', num_tracker)) < num_where:
    num_tracker = k.find(' ', num_tracker)
    spaces.append(num_tracker)
    print(f'Spaces List:{spaces}')
    num_tracker += 1
i = 0
p = 1
#keyu = []
print(len(spaces))
for i in range(len(spaces)):
    print(k[spaces[i]:spaces[p]])
    #keyu[i] = k[spaces[j]:spaces[p]]
    p += 1
 
 #print(keyu)
# strip() 