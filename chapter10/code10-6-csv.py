import csv
import random

from my_package import my_tools
# with open('data.csv', mode='r', encoding='utf-8') as f:
#     cf = csv.reader(f)
#     head = next(cf) # 获取表头
#     scores = []
#     for i in cf:
#         scores.append(int(i[2]))
#     print(sum(scores)/len(scores))

lista = []
def random_info(n=100):
    subjects = ['python', 'java', 'C++', 'html']
    for i in range(n):
        name = my_tools.random_string(random.randint(3, 6))
        subject = random.choice(subjects)
        score = random.randint(50, 100)
        lista.append([name, subject, score])

def average():
    pass


with open('data.csv', mode='a', encoding='utf-8') as f:
    cf = csv.writer(f)
    cf.writerow(['tom', 'c', '50'])
    random_info()
    lista = [['lily', 'c', '50'], ['lily', 'python', '60'], ['lily', 'java', '70']]
    cf.writerows(lista)