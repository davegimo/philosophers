f = open("stringhe_senza_spazio.txt","r")

for line in f:
    l = line.split(",")
    if len(l) == 2:
        print(line, end = '')

        
