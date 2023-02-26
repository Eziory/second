x = 5

while True:
    print('x小于10哦')
    print('反正也是无限循环，你走不出去的')
    x = x + 1
    break # 中止循环

print('我中止循环了')

# while True的循环一定要加一个break
# 这样才能让循环中止
# 同时教一下如果cmd进入无限循环，使用ctrl + C就可以强制中断


# 那我们举一个while True在真正实际中使用的例子
while True:
    mode = input('请输入游戏模式:')
    if mode == 'q': #quit
        break
    elif mode == '1':
        print('启动模式一')
    elif mode == '2':
        print('启动模式二')
    else:
        print('只能输入 1/2/q')

# 所以while True通常使用方式都是希望让用户不停的进行输入
# 这里1和2都要加''是因为input里面加入的都是string，所以判断一定得是string