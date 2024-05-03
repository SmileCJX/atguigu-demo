def f(a, b):
    return a + b

result = f(1, 2)
print(result)

fun = lambda a,b:a + b
result = fun(1, 2)
print(result)

a = [1, 2, 3, 4, 5]
b = []
for i in range(len(a)):
    a[i] = a[i] ** 2
print(a)


a = [1, 2, 3, 4, 5]
def f(x):
    return x ** 2
result = map(f, a)
print(list(result))