# 浮点数的计算
num1 = 0.1
num2 = 0.2
print(num1 + num2)
print(type(num1))
print(num1)

# 四舍五入
num3 = round(num1 + num2, 2)
print(num3)

# 取整
import math
# 向上取整
num4 = math.ceil(num1 + num2)
print("向上取整的结果是：", num4)
# 向下取整 floor
num5 = math.floor(num1 + num2)
print("向下取整的结果是： ", num5)