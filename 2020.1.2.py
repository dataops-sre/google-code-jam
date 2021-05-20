def sol(s):
    p = 0
    res = ""
    i = 1
    l = len(s)
    for x in s:
        n = int(x)
        if n == 0:
            if p != 0:
                res = res + ")" * p
                p = 0
            res = res + str(n)
        else:
            if p == 0:
                res = res + "(" * n + str(n)
                p = n
            elif p == n:
                res = res + str(n)
            elif p < n:
                res = res + (n-p) * "(" + str(n)
                p = n
            #p > n
            else:
                res = res + (p-n) * ")" + str(n)
                p = n
        if i==l:
            if p != 0:
                res = res + ")" * p
        i = i + 1
    return res

def test_cases():
    res1 = sol("0000")
    assert res1 == "0000", f"test case #1 failed with res :{res1}"
    print("test case #1 success")

    res2 = sol("101")
    assert res2 == "(1)0(1)", f"test case #2 failed with res :{res2}"
    print("test case #2 success")

    res3 = sol("111000")
    assert res3 == "(111)000", f"test case #3 failed with res :{res3}"
    print("test case #3 success")

    res4 = sol("1")
    assert res4 == "(1)", f"test case #4 failed with res :{res4}"
    print("test case #4 success")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1, t+1):
        s = input()
        res = sol(s)
        print(f"Case #{i}: {res}")
