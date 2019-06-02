'''
num = int(input("请输入一个整数："))
a = 0
b = 1
i = 0
while a<num:
    a,b = b,a+b #赋值运算，先计算赋值号（也就是=号左边的，再赋值）
    i += 1

if a == num:
    print("{}是第{}位斐波那契数".format(num,i))
else:
    print("{}不是一个斐波那契数".format(num))
'''
'''
n=tuple(input(""))
def oddTuples(aTup):
    a=len(aTup)
    for i in range(0,a,2):
        b=aTup[i]
    return b
print(oddTuples(n))
'''
