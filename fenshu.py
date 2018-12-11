#按照100分制，90分以上成绩为A，80~89为B，60~79为C，60以下为D。
#当用户输入份数，自动转换为A、B、C、D的形式打印

score = int(input('请输入你的分数：'))      #将输入的分数设为整数

if 100 >=score>= 90:                        #条件判断
    if 100>= score >95:                     #嵌套判断
        print('A+')
    else:
        print('A')
elif 90>score>=80:                          #注意条件判断的层级
    print('B')
elif 80>score>=60:
    print('C')
elif 60>score >=0:
    print('D')
else:
    print('请输入正确的分数')
pass


