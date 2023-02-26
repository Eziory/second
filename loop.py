x = 5

# while x < 10:
#     print('x小于10哦')
# 上面这一段就会不停的执行x小于10哦这句话
# 因为x等于5时，x < 10永远成立
# 我们简单的来叙述就是
# 当while后面是True的时候，执行里面的block
# 当执行完毕之后，会返回来重新判断while
# 如果判断依旧是True
# 那么就会继续执行while block

while x < 10:
    print('x小于10哦')
    x = 100

# 这边loop循环就会停下来，因为x已经变成100了
# 第二次判断的时候，while的判断会变成False

x = 5

while x < 10:
    print('x小于10哦')
    print('继续循环')
    x = x + 1

# 这样就会循环5次，因为x在5次叠加之后
# x = 10对于x < 10就是False了
# loop就停止了