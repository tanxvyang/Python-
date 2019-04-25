import pickle
from tan_AthleteList import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        templ = data.strip().split(',')
        #return(Athlete(templ.pop(0),templ.pop(0),templ))
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('datafile error : '+str(ioerr))
        return(None)

def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error(put_to_store):'+str(ioerr))
    return(all_athletes)
        #return(all_athetes)     #Pyhon中使用缩进来确定语句块,就是因为这个缩进没有在它该对应的位置,从而导致该函数没有返回值
                                    #以后要注意,一一对应

def get_form_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_to_store):'+str(ioerr))
        return(all_athletes) 
