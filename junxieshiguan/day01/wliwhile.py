#name:wliwhile
#author:Yangwenwu
#@Time:2018/3/28 12:59
a = 1
while a <= 4:
    print("win is a good men" )
    a += 1
else:
    print("6666")


print("-----分割线-----")

num1 = int(input("请输入数字："))
if num1 <= 0:
    print("娘胎")
elif num1 <=3:
    print("baby")
elif num1 <=6:
    print("小孩子")
elif num1 <=10:
    print("孩子")
elif num1 >10:
    print("成年")
else:
    print("不是人")








print("-------分割线----------")


num_1 = int(input("请输入第一个值："))
num_2 = int(input("请输入第二个值："))
if num_1 > num_2:
    print("输入的第一个值最大:d%"%num_1)
    #若为字符串那就使用s%
else:
    print("您输入的第二个值最大：",num_2)



