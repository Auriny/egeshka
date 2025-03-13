def autobin(x):
    x_bin = bin(x).removeprefix("0b")
    bin_item = x_bin.__getitem__(1) + x_bin.__getitem__(0)
    a = bin_item + x_bin
    b = a.__getitem__(0) + a
    int_b = int(b, base=2)

    return int_b

bin_list = []

for n in range(2, 5000):
    if autobin(n) > 70:
        bin_list.append(n)
        print(n)