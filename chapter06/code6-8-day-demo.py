# 题目要求： 输入2024-02-25，输出这天是这一年的第多少天，先不考虑闰年的情况
# 2023-12-21    每个月是多少天，加在一起
date = input('请输入日期：').split('-')
# print(date)
year = int(date[0])
month = int(date[1])
day = int(date[2])

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (not year % 4 and year % 100) or (not year % 400):
    days[2] += 1
# print(sum(days))
result = 0
for i in range(month):
    result += days[i]
result += day
print('这一天是这一年的第%d天' % result)