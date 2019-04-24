def sanitize(time_string):
    if '-' in time_string:
        splitize = '-'
        (mins, secs)=time_string.split(splitize)
    elif ':' in time_string:
        splitize = ':'
        (mins, secs)=time_string.split(splitize)
    else:
        return(time_string)
    return(mins+'.'+secs)
'''
#1,2
def get_coach_data(filename):
    try:
         with open (filename) as f:
             data = f.readline()
         return(data.strip().split(','))    
    except IOError as err:
        print('file error :'+str(err))
        return(None)
  '''
def get_coach_data(filename):
    try:
         with open (filename) as f:
             data = f.readline()
             '''#
             student= data.strip().split(',')
             data = {}
             data['Name'] = student.pop(0)
             data['DOB'] = student.pop(0)
             data['Times']= student
             print(data['Name']+'s fastest times are: '+
                    str(sorted(set(sanitize(t) for t in data['Times']))[0:3]))
         return(data)
             '''
             student = data.strip().split(',')
         return({'name':student.pop(0),'DOB':student.pop(0),'times':str(sorted(set(sanitize(t) for t in student))[0:3])})    
    except IOError as err:
        print('file error :'+str(err))
        return(None)      
sarah = get_coach_data('sarah2.txt')
#print(data)
print(sarah['name']+"'s fastest times are : "+sarah['times' ])
james = get_coach_data('james2.txt')
print(james['name']+"'s fastest times are : "+james['times' ])
julie = get_coach_data('julie2.txt')
print(julie['name']+"'s fastest times are : "+julie['times' ])
mikey = get_coach_data('mikey2.txt')
print(mikey['name']+"'s fastest times are : "+mikey['times' ])



'''
#1.处理多类型数据
(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
print(sarah_name+'s fastest times are: '+
        str(sorted(set(sanitize(t) for t in sarah))[0:3]))        
'''
'''
#2.使用字典处理数据
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times']= sarah
print(sarah_data['Name']+'s fastest times are: '+
        str(sorted(set(sanitize(t) for t in sarah_data['Times']))[0:3]))

'''    
