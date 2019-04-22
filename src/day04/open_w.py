

man=[]
other=[]
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
           (rloe,line_spoken) = each_line.split(':', 1)
           line_spoken = line_spoken.strip()
           if rloe=='Man':
                man.append(line_spoken)
                
           elif rloe=='Other':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
        print('The data file is missing!')
print(man);print(other)
try:
    man_file = open("man_data.txt",'w')
    other_file = open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
    man_file.close()
    other_file.close()
except IOError:
    print('File error.')
