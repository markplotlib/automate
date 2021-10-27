fileName = '../data/inputFile.txt'
f = open(fileName,'r')
output1 = "../data/PassFile.txt"
output2 = "../data/FailFile.txt"
passFile = open(output1,'w')
failFile = open(output2, 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)
passFile.close()
failFile.close()
