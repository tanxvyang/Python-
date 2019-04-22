'''
#show01.py

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


'''

'''
#+

#优化代码,用finally扩展try
finally:
    man_file.close()
    other_file.close()


'''