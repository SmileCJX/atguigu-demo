def write_txt():
    pass
def read_txt(day=False):
    pass

def quit():
    print('欢迎下次使用！再见！')

def menu():
    print('*' * 30)
    print('''欢迎使用python日记本系统
    1:记日记
    2：阅读日记
    3：退出系统
    ''')
    print('*' * 30)

menu()
while True:
    op = input('请输入你的选择：')
    if op == '1':
        write_txt()
    elif op == '2':
        read_txt()
    elif op == '3':
        quit()
        break
    else:
        print('请重新选择')