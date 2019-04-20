'''
import os
if os.path.exists('sketch1.txt'):
    data = open('sketch1.txt')
    for each_line in data:
        try:
           (rloe,line_spoken)=each_line.split(':', 1)
           print(rloe, end='')
           print(' said: ', end='')
           print(line_spoken, end='')
        except:
            pass
    
    data.close()
else:
    print('The data file is missing!')
    '''


"""
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
           (rloe,line_spoken)=each_line.split(':', 1)
           print(rloe, end='')
           print(' said: ', end='')
           print(line_spoken, end='')
        except:
            pass
    
    data.close()
except:
        print('The data file is missing!')
"""




try:
    data = open('sketch.txt')
    for each_line in data:
        try:
           (rloe,line_spoken)=each_line.split(':', 1)
           print(rloe, end='')
           print(' said: ', end='')
           print(line_spoken, end='')
        except ValueError:
            pass
    
    data.close()
except IOError:
        print('The data file is missing!')
    
