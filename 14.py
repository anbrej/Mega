for x in range(39):
    for y in range(39):
        n = 5 * 39 ** 8 + 8 * 39 ** 7 + 7 * 39 ** 5 + 2 * 39 ** 4 + 3 * 39 ** 3 + 4 * 39 + 9
        n += x*39**6 + y*39**2
        if n % 38 == 0 and ((y*39+x)**0.5) % 1 == 0:
            print((y*39+x), (y*39+x)**0.5)