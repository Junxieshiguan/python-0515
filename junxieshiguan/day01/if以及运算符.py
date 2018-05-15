
import random
print("是否是水仙花数判断")
#num = int(input("请输入三位数"))
num = 153
a = num % 10
b = num % 100//10
c = num//100

if num==a**3+b**3+c**3:
    print("yes")
else:
    print("NO")


#对比三个数的最大值，并输出

'''a = int(input("first"))
b = int(input("second"))
c = int(input("three"))
if a >= b:
    a = a
else: a = b
if a >= c:
    a = a
else:
    a = c
print(a)
'''
''' 
&  和  | 二进制运算
&必须两个是1才是1
|有1就是1
^按位异或运算符，二进制两位相异时，结果是1，否则是0
~按位取反运算符，每个二进制数据位取反，
'''
'''
逻辑与运算符 表达式 and 表达式   真真为真，有假即假
逻辑或运算符 表达式 or 表达式    真真为真，有真即真
逻辑非运算符    not 表达式       假为真，真为假，颠倒黑白

'''
a = int(random.randrange(0,19,1)+1)
b = random.choice([0.12,14,15,2,3,4,17,14,57,21,31,7,8,9,10])

if not a>b:
    print("成功","第一名:",a,"第二名:",b)
else:
    print("不成功", "第一名:", a, "第二名:", b)
'''成员运算符：
in：如果在制定序列中找到值返回TRUE，否则返回False
not in如果在指定序列中找不到值返回True，否则返回False 
'''
'''
身份运算符
is：判断两个标识符是不是引用同一个对象
is not：判断两个标识符是不是引用不同的对象
'''
print(not 3>4)
if 0.00000000:
    print("111")
else:
    print("2222")



print(-2 & 3)
