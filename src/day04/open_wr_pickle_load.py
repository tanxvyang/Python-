#优化代码,用finally扩展try
'''
如果遇到这种情况,也就是不论出现什么错误都必须运行某段代码时,可以向finally组中添加

通过with 语句简化代码,with 会自动处理文件的关闭操作

'''
import pickle
import tan_nester
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
                
           elif rloe=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
        print('The data file is missing!')

try:
    with open("man_data.txt",'rb') as man_file, open('other_data.txt','rb') as other_file:
       new_man=pickle.load( man_file)
       new_other=pickle.load( other_file)
       tan_nester.print_lol(new_man)
       tan_nester.print_lol(new_other)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('Pickling err'+str(perr))

    

    
    
