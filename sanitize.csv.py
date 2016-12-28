import sys
with open(sys.argv[1]) as csvfile:
    count=0
    columns=[]
    for line in csvfile:
        line = line.rstrip()
        if count==0:
            columns=line.split(',')
            print(line)
        else:
            values = line.split(',')
            if len(values) != len(columns):
                #print(line)
                print(','.join(values[:len(columns)]))
            else:
                print(line)
        count = count + 1
