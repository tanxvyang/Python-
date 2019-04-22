import tan_sanitize
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