# else if 意思就是另外如果
age = input('请输入年龄：')
age = int(age)

if age < 13:
    print('小学')
elif age >= 13 and age <= 18: # elif其实就是多开一个条件进行判断
    print('初中')
else:
    print('高中')


# 这边有一个注意点是
# 记得elif和else后面都要接一个:
# 这个很重要别忘了
# 这边要记住，这里面只算一个if架构，elif，else都是属于这个if架构里面的