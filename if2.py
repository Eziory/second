age = input('请输入年龄：')
age = int(age)

if age >= 20:
    print('你可以喝酒了')
else:
    print('你还不能喝酒哦')

# else就是否则的意思，当if的判断条件是False的时候，那么就会执行else的内容
# else的block和if的block是绝对不可能同时执行的