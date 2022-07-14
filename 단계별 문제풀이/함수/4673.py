def d():
    num_list = list(range(1, 10001))
    selfnum = []
    for num in num_list:
        for _ in str(num):
            num += int(_)
        if num <= 10000:
            del_list.append(num)



