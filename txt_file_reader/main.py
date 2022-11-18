#file reader


file = open('C:\\Users\\dvillalva\Desktop\\scripts_from_x\\practice_water_oracle.txt', 'r')

rl = file.readlines()

new = []
#print(rl)

for line in rl: 
    new.append(line.strip())

    # if line[-1] == '\n':
    #     new.append(line[:-1])
    # else
    #     new.append(line)

file.close
file.
print(new)
