def classify(a, b, c):
    if (a+b) < c or (a-b) > c:
        print("Please enter right triangle")
        return 'none'
        exit()
    c1 = max(a, b, c)
    a1 = min(a, b, c)
    if (a1 == a or a1 == b) and (c1 == a or c1 == b):
        b1 = c
    else:
        if (a1 == a or a1 == c) and (c1 == a or c1 == c):
            b1 = b
        else: b1 = a
    print(a1, b1, c1)
    if a == b and b == c:
        print('Equilateral')
        return 'Equilateral'
    else:
        if a == b or b == c or a == c:
            print('isosceles')
            return 'isosceles'
        else:
            print('scalene')
            return 'scalene'


def ifright(a, b, c):
    if (a**2) + (b**2) == (c**2):
        print('This Triangle is a Right triangle')
    else:
        print('this triangle is not a Right Triangle')
