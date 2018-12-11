import random                                       #导入random模块

secret = random.randint(1,3)                         #随机生成一个整数

count = 0                                           #设置个次数，次数从0开始
while count < 4:                                    #循环次数小于一个数
    count = count + 1                               #次数按照+1递增
    guess=int(input('你猜猜这个数字是多少？:'))     #输入一个数字，并将这个数字设为整数
    
    if guess > secret:                              #条件判断
        print('大了，再小点试试')
    elif guess < secret:
        print('小了，再大点试试')
    else:
        print('牛批！猜对了')

print('cishu yongwanl')                             #循环结束
