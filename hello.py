print 'hello,worlde!'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello,worlde!')?
>>> print 'h'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('h')?
>>> print"h"
SyntaxError: invalid syntax
>>> print(hello)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined
>>> print("hello")
hello
>>> 
#在Python3中print 需要使用  print（）来表示

>>> 
2**3     #x**y   表示x的y次幂
8
>>> pow(2,3)  #函数pow（x,y）表示x的y次幂
8
>>> abs(-10)    #abs()  函数表示取绝对值
10

>>> round（1.0/2.0）   # round()   函数会把浮点数四舍五入为最接近的整数值
>>> import math
>>> math.floor(32.9)   #  impor 模块名   导入模块    模块.函数  应用函数
32
>>> int (math.floor(32.9))
32
>>> from math import sqrt
>>> sqrt(9)
3.0
>>>    #  在使用from模块import函数 命令后，可以直接使用函数，不需要模块名做前缀


>>> import cmath
>>> cmath.sqrt(-1)
1j
>>>     #cmath 模块可以处理负数开方，形成虚数>>> 

（1+3j）*(9+4j)
SyntaxError: invalid character in identifier 
 #错误表示标识符中的无效字符”,检查下有没有字符是中文的,把中文字符改成英文字符再运行
>>> (1+3j)*(9+4j)
  (-3+31j)




  >>> "hello,world"
'hello,world'
>>> "Let's go!"
"Let's go!"
>>> 'let's go!'        
SyntaxError: invalid syntax   #出现错误的原因是因为python不知道如何处理后面的‘s

>>> "Let\'s go!"   #使用反斜杠（/）对字符串中的引号进行转义
"Let's go!"

 #拼接字符串
>>> 
>>> 
>>> 
>>> "Let's say"'"hello world!"
SyntaxError: EOL while scanning string literal   #错误原因 字符串符号没有成对出现
>>> "Let's say"'"hello world!"'
'Let\'s say"hello world!"'


>>> "hello"+"world!"  #使用类似加法将字符串链接
'helloworld!'
>>> x="hello"   
>>> y="world!"
>>> x+y
'helloworld!'
>>> 


>>> temp = 42
>>> print("The temperture is :"+ str(temp))   # str是一种类型 把值转换成一种合理形式的字符串，以便用户理解
The temperture is :42
>>> print("The temperture is :"+ repr(temp))  #repr函数会创建一个字符串以python合法的表达方式来表示值
The temperture is :42


>>> print("hello,\nworld!")  #\n换行
hello,
world!


########使用\\    反斜杠对其本身转义，从而解决路径输入时可能出现的换行
>>> path='c:\nwhere'
>>> print(path)
c:
where
>>> path='c:\\nwhere'
>>> print(path
	  )
c:\nwhere




#######原生字符串  原生字符串以r 打头  并且不会将反斜线当做特殊字符
>>> print ('c:\nwhere')   
c:
where
>>> print (r'c:\nwhere')
	   
c:\nwhere

>>>  print (r'c:\nwhere\')
	    
SyntaxError: unexpected indent
>>> print (r'c:\nwhere\')
	   
SyntaxError: EOL while scanning string literal
>>> print (r"c:\nwhere\\" )
	   
c:\nwhere\\
>>> print (r'c:\nwhere\'')
	   
c:\nwhere\'
>>>  print (r'c:\nwhere''\\')
	   
SyntaxError: unexpected indent

#####原生字符串最后一个字符不能是反斜杠 如果有，则要以如下形式输出

>>> print (r'c:\nwhere''\\')
	   
c:\nwhere\