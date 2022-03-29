##Mackenzie Bishop
##Sorter for out01.txt

input = open("out01.txt","r")  # open file, read-only
output = open("sort02.txt", "w") # open file, write

lines = input.readlines()
lines.sort()

for line in lines:
	output.write(line)

input.close()
output.close()