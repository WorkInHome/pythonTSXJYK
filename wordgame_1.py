import random
secret = random.randint(1,10)
print('I am tsx小仙女')
temp = input("不妨猜一下tsx小仙女心里想的是哪一个数字：")
guess = int(temp)
while guess != secret:
    temp = input("诶呀，猜错啦，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print ("卧槽，你是本仙女心里的蛔虫吗？！")
        print("哼！你以为猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了！！")
        else:
            print("嘿，小了！小了！！")
print("游戏结束，本仙女要上天啦，拜拜")

    
