# 密码重试程序
# 现在程序中设定好密码 password = 'a123456'
# 让使用者最多输入3次密码
# 不对的话，就打印出"密码错误，还有_次就会"
# 对的话，就引出"登录成功"

x = 4
origin = 'a123456'

while x > 1:
    password = input('请输入密码:')

    if password == origin:
        print('登录成功')
        break
    else:
        x = x - 1
        if x == 1:
            print('你已经输入3次都是错的了，不可以再输入了')
            print('自动退出程序')
            break
        print('密码错误，还有', x - 1, '次机会')