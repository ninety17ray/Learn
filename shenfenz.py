# -*- coding:UTF-8 -*-
'''
作者：xiaojun
'''
import random
import datetime

# 功能：从csv文件中读取一个区域编码字典
# 输入：文件名称
def areaCodeDict(fileName):
    dataDict = {}
    key=0
    value=1
    dataLine=open(fileName,encoding="utf-8").read().splitlines()
    for line in dataLine:
        tmpLst=line.split(",")
        dataDict[tmpLst[key]]=tmpLst[value]
    return dataDict

# 功能：随机生产一个区域码

def areaCode(Dict):
    codeList=[]
    for key in Dict.keys():
        codeList.append(key)
    lenth=len(codeList)-1
    i=random.randint(0,lenth)
    return codeList[i]
# 功能：随机生成1930年之后的出生日期
def birthDay():
    d1=datetime.datetime.strptime('1930-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    d2=datetime.datetime.now()
    delta=d2-d1
    dys=delta.days
    i=random.randint(0,dys)
    dta=datetime.timedelta(days=i)
    bhday=d1+dta
    return bhday.strftime('%Y%m%d' )

#功能：随机生成3位序列号

def ordrNum():
    odNum=random.randint(100,999) #随机生成100到999之间的3为数据
    sex=odNum%2
    return (str(odNum),sex)

#功能：生成校验码

def check(id_num):
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
    for i in range(0,len(id_num)):
       count = count +int(id_num[i])*weight[i]
    return checkcode[str(count%11)] #算出校验码


fileName=".\\area.csv"  #区域文件地址
areaCodeDt=areaCodeDict(fileName)   #调用生成字典
areaCd=areaCode(areaCodeDt)     #生成区域码
areaCdName=areaCodeDt[areaCd]   #获取区域名称
birthDy=birthDay()   #生成出生日期
(ordNum,sex)=ordrNum()  #生成顺序号和性别
checkcode=check((areaCd+birthDy+ordNum)) #生产校验码
id_card=areaCd+birthDy+ordNum+checkcode  #拼装身份证号
print(id_card)
