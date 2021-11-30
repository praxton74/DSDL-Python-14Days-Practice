try:
    def numJewelsInStones(jewels, stones):
        res = 0
        for val in jewels:
            res += stones.count(val)
        return res

    t = int(input())
    while t:
        jewels = input()
        stones = input()
        print(numJewelsInStones(jewels, stones))
        t -= 1

except:
    pass
