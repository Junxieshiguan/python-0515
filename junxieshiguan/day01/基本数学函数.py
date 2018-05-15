import math
import random
print((max(1,3,45,2,34,6)))
print(int(min(2,3,4,5,5,6,1,0.1)))
print(pow(3,5))#3^5  3的5次方
print(round(2.5212121))#round四舍五入,后面的是保留的位数函数形式（round(num[,num])）中括号里面是可有可无的
print(round(2.5212121,1))
print(round(2.5212121,2))
print(round(2.5212121,4))
print("----分割线----")
#向上取整
print(math.ceil(18.1))
print(math.ceil(18.8))
print("----分割线----")
#向下取整
print(math.floor(18.1))
print(math.floor(18.8))

print("----分割线----")
#返回整数部分与小数部分
num2 = math.modf(22.4)
print(num2)


#随机数
#1,调用random函数库
print(random.choice([1,3,4,7,10]))
print(random.choice(range(5)))#range(5)==0,1,2,3,4

print("----分割线----")
a2 = random.choice(range(19))+1
print(a2)
print("----分割线----")
#random.randrange(star,stop,n)n是递增的基数，结束值不包含在输出之内，取头 去尾
print(random.randrange(1,100,3))

print("----分割线----")
#产生[0,1）之间随机的浮点数（flat）
print(random.random())




#将序列中得到所有元素随机排列
list = [1,2,3,4,5,6,7,8]
#直接打印
 #print(list)
random.shuffle(list)
print(list)