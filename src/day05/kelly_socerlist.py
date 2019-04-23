import tan_sanitize

'''
#6.将这块代码用函数的方式简化
with open('james.txt') as jaf:
    data=jaf.readline()
james = data.strip().split(',')

with open('julie.txt','r') as juf:
    data = juf.readline()
    julie = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
'''

'''1.
print(james)
print(sarah)
print(mikey)
print(julie)
print('='*len(james))
print(sorted(james))
print(sorted(sarah))
print(sorted(mikey))
print(sorted(julie))
'''


'''2.
new_james=[]
new_sarah=[]
new_mikey=[]
new_julie=[]
for each_t in james:
    new_james.append(tan_sanitize.tan_sanitize(each_t))
for each_t in sarah:
    new_sarah.append(tan_sanitize.tan_sanitize(each_t))
for each_t in mikey:
    new_mikey.append(tan_sanitize.tan_sanitize(each_t))
for each_t in julie:
    new_julie.append(tan_sanitize.tan_sanitize(each_t))
print(sorted(new_james))
print(sorted(new_sarah))   
print(sorted(new_mikey))
print(sorted(new_julie))
'''
'''3.
new_james=[sorted(tan_sanitize.tan_sanitize(t) for t in james)]
new_sarah=[sorted(tan_sanitize.tan_sanitize(t) for t in sarah)]
new_mikey=[sorted(tan_sanitize.tan_sanitize(t) for t in mikey)]
new_julie=[sorted(tan_sanitize.tan_sanitize(t) for t in julie)]

print(new_james)
print(new_sarah)   
print(new_mikey)
print(new_julie)
'''

'''4.

#将原列表中的数据规范化,并排序,赋至新的目标标识中
new_james=sorted(tan_sanitize.tan_sanitize(t) for t in james)
new_sarah=sorted(tan_sanitize.tan_sanitize(t) for t in sarah)

new_mikey=sorted([tan_sanitize.tan_sanitize(t) for t in mikey])
new_julie=sorted([tan_sanitize.tan_sanitize(t) for t in julie])
#print(new_james)
#print(new_sarah)   
#print(new_mikey)
#print(new_julie)

#消除重复的数据,并显示前三个时间   尽管做到了,但这很繁琐,用重复的代码删除了重复的数据
unique_james = []
for each_t in new_james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])

unique_julie = []        
for each_t in new_julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)     
print(unique_julie[0:3]) 

unique_mikey = []        
for each_t in new_mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)  
print(unique_mikey[0:3])   

unique_sarah = []        
for each_t in new_sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t) 
print(unique_sarah[0:3])

'''


'''
# 5.用集合删除重复项, 集合 无序,且唯一   使用函数 set()

print(sorted(set([tan_sanitize.tan_sanitize(t) for t in james]))[0:3])
print(sorted(set([tan_sanitize.tan_sanitize(t) for t in julie]))[0:3])
print(sorted(set([tan_sanitize.tan_sanitize(t) for t in sarah]))[0:3])
print(sorted(set([tan_sanitize.tan_sanitize(t) for t in mikey]))[0:3])
'''
def tan_open(filename):
    try:
         with open (filename) as f:
             data = f.readline()
         return(data.strip().split(','))    
    except IOError as err:
        print('file error :'+str(err))
        return(None)

sarah = tan_open('sarah.txt')
print(sorted(set([tan_sanitize.tan_sanitize(t) for t in sarah]))[0:3])        
sarah = tan_open('miss.txt')
print(sorted(set([tan_sanitize.tan_sanitize(t) for t in sarah]))[0:3])        
