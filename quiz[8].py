def a(number):
    if len(number) != 13:
        return False

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = sum(int(r_num[i]) * weights[i] for i in range(12))
    x = (11 - (total % 11)) % 10
    y = int(r_num[12])

    return x == y

number = input('주민번호를 입력하세요:')
if a:
    print('유효합니다')
else:
    print('유효하지 않습니다')
