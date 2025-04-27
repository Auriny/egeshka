#       v  [0  1  2  3]
hran = [0] * 4
col_otv = 0

for x in range(1, 10):
    for delit in range(4):
        # пытаюсь узнать сколько не хватает х, чтобы он поделился на 4
        if (x + delit) % 4 == 0:
            col_otv += hran[delit]
            print(x, delit, hran,col_otv)

    # положить число которое я взял на его место
    # его место завист от отсатка от деления
    hran[x % 4] += 1
    print(x, delit, hran, col_otv)
    input()