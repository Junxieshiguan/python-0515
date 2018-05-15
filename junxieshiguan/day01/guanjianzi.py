'''import keyword
print(keyword.kwlist)'''

#定义变量就是直接变量等于一个值
# 为了查看字符类型可以用:输出类型来看
#age = input("年龄：")
#type1 = type(age)
#print ( "age的类型为",type1)
#print ( "age的类型为",type(age))


age = "good"
print ( "age的类型为",type(age))
#这是将上面的整合在一起
print(age)
#输出age的地址
print( id ( age ) )



nul1 = int(input("请输入一个数字"))
#w为了能输入进去值必须用input输入才行
nul2 = int (input("请输入第二个数字"))
print ( nul1 ,"+", nul2 , "=", nul1+nul2 )
#输出的两个字符之间必须用逗号隔开
