cards = []

def menu():
    print('''欢迎使用【名片管理系统】
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统
    ''')
    print('*' * 30)
    pass

def new_card(name, phone, qq, email):
    user = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }
    cards.append(user)
    return True

def show_card():
    for card in cards:
        print(card)

def query_card():
    pass

def quit():
    print('欢迎下次使用【名片管理系统】')

menu()

while True:
    op = input("请输入你要操作的序号：")
    if op == '1':
        name = input('请输入你的姓名：')
        phone = input('请输入你的电话：')
        qq = input('请输入你的qq号：')
        email = input('请输入你的电子邮箱：')
        result = new_card(name, phone, qq, email)
        if result:
            print('成功新建名片')
        else:
            print('请重试')
    elif op == '2':
        show_card()
    elif op == '3':
        query_card()
    elif op == '0':
        quit()
        break
    else:
        print('请重试')