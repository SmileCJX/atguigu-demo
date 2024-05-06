# import my_module
# result = my_module.add(3, 4)
# print(result)
# print(my_module.author)
# my_module.author = 'tom'
# print(my_module.author)


# 不导入所有的内容, *代码所有
# from my_module import add, author
# result = add(3, 4)
# print(result)
# print(author)

# 别名调用
from my_package.my_math import add as f
result = f(3, 4)
print(result)
