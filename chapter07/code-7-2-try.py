try:
    print('有可能出现异常的代码：')
    # print(1 + '1')
    n = int(input('请输入一个数字'))
    n = int(n)
    n = 5 / n
    print(n)
except ZeroDivisionError as e:
    print('原始报错信息：', e)
    print('除数不能为0')
except:
    print('请输入一个数字')
else:
    print('运行没有被except语句捕获，执行else模块')
finally:
    print('无论如何，都要执行finally模块')