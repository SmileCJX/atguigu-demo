# 任务1：打印数字
print(2024)

# 任务2： 打印字符串，我是CJX
print("我是CJX")

# 任务3： 创建变量year，值为2024，并打印
year = 2024 #  年
month = 4
day = 18
week = "四"
weather = "晴"
temp = 19.5
print(year)
print(year, "年，我要挣钱", sep="")  # sep: 设置打印多个内容的分隔符
print()
print(year, "年，我要读100本书", sep="")
# end： 设置print执行结束后的操作
print(end='*')
print(year, "年，我要去10个城市旅游", sep="")

print("今天是%d年%02d月%d日，星期%s， 天气%s， 温度%.2f" % (year, month, day, week, weather, temp))