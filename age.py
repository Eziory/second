drive_or_not = input('你有没有开过车？')
age = input('你的年龄是:')
age = int(age)

if drive_or_not == '有':
    if age < 18:
        print('你怎么可能开过车')
    else:
        print('没问题，开车的时候注意安全')
elif drive_or_not == '没有':
    if age < 18:
        print('很好，等你18岁再开车吧')
    else:
        print('你可以开始学车啦，你年龄已经到了')
else:
    print('请回答我问的问题')