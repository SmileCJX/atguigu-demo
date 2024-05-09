import csv
with open('data.csv', mode='r', encoding='utf-8') as f:
    cf = csv.reader(f)
    head = next(cf) # 获取表头
    scores = []
    for i in cf:
        scores.append(int(i[2]))
    print(sum(scores)/len(scores))