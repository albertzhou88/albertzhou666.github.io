def yanghui(n):
    L = [1]
    for j in range(n):
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
        print(L)


n = int(input('How many rows? '))
yanghui(n)