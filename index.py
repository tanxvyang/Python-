# 索引示例


#根据所给定的年月日以数字形式答应出日期

months=[
     'January',
     'February',
     'March',
     'April',
     'May',
     'June',
     'July',
     'August',
     'September',
     'October',
     'Noverber',
     'December'
     ] 
# 以1~31的数字作为结尾的列表

endings = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year =input("year: ")

month =input ("Month (1-12): ")

day =input('Day (1-31):')

month_number = int(month)
day_number = int(day)

#月份和天数减1，已获得正确索引


month_name = months[month_number-1]
ordinal = day+endings[day_number-1]
print (month_name+'  '+ordinal+' ,'+year)
