### 基本
* '' & "" mean the same in python.
* """abc  
      abc""" --- a multiline string **控制缩进格式**，还是会转义;
* **r**"zhaojinzhou\nzhaojinzhou" natural string. '\n' will not be translated，不会转义;
* **print()函数默认加‘\n’ 如果不希望加需要写成print(a,end = '')**
* import sys   
*07.09.12*  
------  
### string 类的方法   
str = "HELLO"

str.lower()  

str.upwer()  

str.swapcase()  

str.capitalize() \# 首字母大写  

str.find("substr") \# 返回index int  

str.count("ds") #返个数 int  

str.replace("to_be_replaced", "replaced") 返回new_str  

-------
  print('I have %d cats' % 6)  
  
  I have 6 cats  
  
  print('I have %3d cats' % 6)  
  
  I have    6 cats  
  
  print('I have %03d cats' % 6)  

  I have 006 cats  

  print('I have %f cats' % 6)  
  I have 6.000000 cats  

  print('I have %.2f cats' % 6)    
  I have 6.00 cats

  
 


