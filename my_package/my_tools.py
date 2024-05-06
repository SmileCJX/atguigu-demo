import random
a = []
n = 5

def random_char(upper=True):
    if upper:
        t = random.randint(65, 90)
    else:
        t = random.randint(ord('a'), ord('z'))
    return chr(t)

def random_string(length):
    s = ''
    for i in range(length):
        s += random_char(random.choice([True, False]))
    return s

def qrcode(length):
    return random_string(length)

def main():
    # a = []
    # for i in range(20):
    #     a.append(random_string(random.randint(3, 6)))
    # print(a)
    print(qrcode(8))

# main()