import random, re, time
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

def is_phone_number(phone):
    result = re.match(r'^1\d{10}$', phone)
    if result == None:
        return '非法手机号!'
    return '正确的手机号'

def is_id_number(idNumber):
    result = re.match(r'^\d{6}((20[012][01234)])|(1[89]\d\d))\d{7}([\dX])$', idNumber)
    if result == None:
        return '非法证件号!'
    return '正确的证件号'

def get_time():
    t = time.localtime() # 结构化的时间
    s = time.strftime('%Y-%m-%d %H:%M:%S', t)
    return s
