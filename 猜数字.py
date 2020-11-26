import random
a = int(random.random()*50+1)
b = 0
while b != a:
    c = input('猜数字游戏开始，请输入数字：')
    b = int(c)
    if b > a:
        print('您输入的数字大了！')
    else:
        print('您输入的数字小了！')
if b == a:
    print('恭喜，您猜对了！')