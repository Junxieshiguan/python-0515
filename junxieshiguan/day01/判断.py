a = 3#判断合数（除了1和本身还有其他因数）以及质数（除了被自己本身以及1整除），除了1,0均不是质数也不是合数
if a > 2:
  while a%2==0 and  a%3==0 and a%5==0 and  a%7==0 and  a%11==0 and  a%13==0 and  a%17==0:
        print("此数是和数%d"%a)
        a += 1
  else:
        print("此数是质数%d"%a)
        continue

else:
    print("此数即不是合数也不是质数")


