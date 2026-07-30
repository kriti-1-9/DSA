def find_position(n):
    if n == 0:
        return 0
    position = 1
    while (n & 1) == 0:
        n >>= 1
        position += 1
    return position