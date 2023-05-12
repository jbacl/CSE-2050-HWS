def constant_function(n):  # runs a function that only needs 1 point to run
    return n + 10          # 1 = O(1)

def line_function(n):       # runs a function that takes n points to run
    total = 0               # 1
    for i in range(n):      # n times
        total += i + 1      # 2 (or 3)
    return total            # 1
                            # + ------
                            # 1 + 2n + 1 = 2n + 2 = O(n)

def quadratic_function(n):  # runs a function that takes n squared points to run (slower)
    total = 0               # 1
    for i in range(n):      # n times
        for j in range(n):      # n times
            total += i + j      # 2 (or 3)
    return total            # 1
                            # + ------
                            # 2n^2 + 2 = O(n^2)
