# 用户名、密码、黑名单
# users = ['小红', 'mia', 'jack']
# password  =['123', '456', '789']
# not_allowed = ['jack']
users = [
    {'name': '小红', 'password': '123', 'status': True},
    {'name': 'mia', 'password': '456',  'status': True},
    {'name': 'jack', 'password': '789', 'status': False},
]

print(users)
flag = False
for i in range(3):
    user = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')

    for i in users:
        if user == i['name']:
            if pwd == i['password']:
                if i['status'] == True:
                    print('登录成功!')
                    flag = True
                    break
                else:
                    print('账号失效，请联系管理员！')
            else:
                print('密码输入错误，请重试！')
            break
    else:
        print('用户不存在，请先注册！')
    if flag:
        break

