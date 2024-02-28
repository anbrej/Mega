with open ("24.txt") as f:
    s = f.readline()
    n = []
    ans = 0
    counter = 0
    c_counter = 0
    d_counter = 0

    for i in range(len(s)):
        if s[i] == "C" or s[i] == "D":
            n.append(i+1)

    for i in n:
        for j in range(i, len(s)):
            if s[j] != "C" and s[j] != "D":
                counter += 1
            else:
                if s[j] == "C":
                    c_counter += 1
                    if c_counter > 2:
                        ans = max(ans, counter)
                        counter = 0
                        c_counter = 0
                    else:
                        counter += 1
                elif s[j] == "D":
                    d_counter += 1
                    if d_counter > 2:
                        ans = max(ans, counter)
                        counter = 0
                        d_counter = 0
                    else:
                        counter += 1

print(ans)