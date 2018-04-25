# 检查用户名和PIN码
#IndentationError: unexpected indent  错误原因，python对语法格式要求严格，在之前出现错误，
# 文件里格式不对了，可能是tab和空格没对齐的问题，你需要检查下tab和空格了
database = [
     ['albert','1234'],
     ['dilbert','4242'],
     ['smith','7524'],
     ['jones','9843']
  ]

username  =  input('user name:')
pin =   input('PIN code: ')
 
if[username,pin] in database:print('Access granted')





