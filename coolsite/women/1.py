def get_stepen(n):
    y = 0
    while y < 1000:
        print(y, "в степени", n, '=', y**n)
        y += 1

get_stepen(20)