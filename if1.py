# age = input('请输入年龄：')

# if age >= 20:
    # print('你可以喝酒了')

# 上面这一段就会报错
# 错误讯息是字串没办法和整数进行比较
# 因为在python中，input输入的内容都是以string字串作为保存的

# 这个时候我们就需要casting（类别转换）了

age = input('请输入年龄：') # 这个时候age还是string
age = int(age) # 这个时候就把age转换成了integer

if age >= 20:
    print('你可以喝酒了')