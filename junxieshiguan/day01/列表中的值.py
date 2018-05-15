#假如一个美女的组成部分是这样的
beautiful_gril = ['big_bar','body','soft','face' ]
print(beautiful_gril)
print(beautiful_gril[2])
print(beautiful_gril[0])#排列的起始值是0
beautiful_gril[2] = 'leg'#将列表中beautiful gril的第三个元素更改['leg']更改的时候不要用中括号
print(beautiful_gril[2])#更改成功
print(beautiful_gril)
#删除列表中的第二个元素'body’
del beautiful_gril[1]
print(beautiful_gril)
poped_beautiful_girl = beautiful_gril.pop()#将里面一个列表弹出来，然后储存在里面
print(beautiful_gril)
print(poped_beautiful_girl)