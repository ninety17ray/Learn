def discount(price,rate):
    final_price = price * rate
    old_price = 50      #这里试图修改全局变量
    print('在局部变量中修改了的全局变量old_price的值是：',old_price)
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣:'))
new_price = discount(old_price,rate)
print('全局变量old_price现在的值是：',old_price)
print('打折后的价格是：',new_price)
