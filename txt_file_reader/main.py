# Daniel Villalva
# Objective: Read file and create strings
# Encoding, Current version, Imports, Date of creation, Complete update history

############# file reader #############
file = open('C:\\Users\\dvillalva\Desktop\\scripts\\practice_water_oracle.txt', 'r')
rl = file.readlines()
new = []
for line in rl: 
    new.append(line.strip())
file.close

############# convert list into string #############
k = str(new)
############# find "from" in list #############

num_select = k.find('select')
num_from = k.find('from')
num_tracker = num_from
num_where = k.find('where')
#print(f'Select:{num_select} From:{num_from} Where:{num_where}')


############# find space between from and where #############
spaces = []
while (k.find(' ', num_tracker)) < num_where:
    num_tracker = k.find(' ', num_tracker)
    spaces.append(num_tracker)
    #print(f'Spaces List:{spaces}')
    num_tracker += 1

############# Store the strings between spaces FROM #############
i = 0
p = 1
keyu = []
for i in range(len(spaces)-1):
    keyu.append(k[spaces[i]:spaces[p]])
    # Trim string 
    keyu[i] = keyu[i].replace(',','')
    keyu[i] = keyu[i].replace('\'','')
    print(keyu[i])
    p += 1

############# Store the strings between spaces Selection #############

############# Diction #############

