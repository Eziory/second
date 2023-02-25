weight = input('请输入你的体重：')
weight = float(weight)

height = input('请输入你的身高(公尺哦)：')
height = float(height)

bml = weight / (height * height)

if bml < 18.5:
    print('你的体重过轻')
elif bml >= 18.5 and bml < 24:
    print('正常')
elif bml >= 24 and bml < 28:
    print('轻度肥胖')
elif bml >= 28 and bml < 30:
    print('中度肥胖')
else:
    print('重度肥胖')