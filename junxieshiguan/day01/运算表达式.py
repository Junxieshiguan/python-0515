'''表达式：变量与常量和运算符组成的式子

'''
import random

'''
算术运算符与算术表达式：
运算符
+  - *  /    %       **       //
         取余取模   求幂     取整
算术运算表达式
1-2 1*2
功能：进行相关符号的数学运算，不会会改变变量的值
值：相关的数学运算结果
'''
num1 = 5
num2 = 3
num3 = 2
print(num1+num3)
print(num1-num3)
print(num1*num3)
print(num1%num3)
print(num1**num3)
print(num1/num3)
print(pow(num1,num3))
print((num1+num3)*num2)
print(num1//num3)

print("---我是分割线----")
#赋值运算符
#=
#+=   -=   ==    *=   /=   //=   **=
#都是赋值给左边，都是左边+-*/左边然后赋值给左边
num2 += num3
print(num2)

print("---我是分割线----")
'''
  if语句
  格式
if 表达式：
    语句  
else:
真假：
假：0   0.0  None    False 
真：除了假就是真  
  '''
a = input("输入任意数字：")
a=random.choice([2,3,4,5,6,7])
#b = input("需要比较的第二个值")
b =  random.randrange(1,11,1)
if a>=b:
    print("红方胜","a=",a,"b=",b)
else:
    print("蓝方胜","a=",a,"b=",b)
