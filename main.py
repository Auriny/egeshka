def kv(n):
    if len(str(n ** 0.5)[2:]) == len(str(int(n ** 0.5))):
        return True
    return False

print(kv(4))