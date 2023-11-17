def generateMatrix(n):
    res = [[0] * (n) for i in range(0, n)]
    # for i in range(0, n):
    left = 0
    right = n - 1
    top = 0
    down = n - 1
    num = 0
    while right >= left:
        for current in range(left, right):
            res[top][current] = num
            num += 1
        for current in range(top, down):
            res[current][right] = num
            num += 1
        if left != right:
            for current in range(right, left, -1):
                res[down][current] = num
                num += 1
            for current in range(down, top, -1):
                res[current][left] = num
                num += 1

        left += 1
        right -= 1
        top += 1
        down -= 1

    if n % 2 == 1:
        res[n//2][n//2] = num
    # print result
    # for i in res:
    #     print(i)
    return res
print(generateMatrix(3))



