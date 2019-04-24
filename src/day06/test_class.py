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
class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        #the code to initialize a 'Athlete object '
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,time_list):
        self.times.extend(time_list)
        '''
#重写这个类,让他继承内置的list类,
class AthleteList (list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        templ = data.strip().split(',')
        #return(Athlete(templ.pop(0),templ.pop(0),templ))
        return(AthleteList(templ.pop(0),templ.pop(0),templ))

    except IOError as ioerr:
        print('file error : '+str(ioerr))
        return(None)
        


james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are : " +str(james.top3()))
julie = get_coach_data('julie2.txt')
print(julie.name + "'s fastest times are : " +str(julie.top3()))
mikey = get_coach_data('mikey2.txt')
print(mikey.name + "'s fastest times are : " +str(mikey.top3()))
sarah = get_coach_data('sarah2.txt')
print(sarah.name + "'s fastest times are : " +str(sarah.top3()))
