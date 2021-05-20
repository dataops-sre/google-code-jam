def sol(sm, s):
    acc = 0
    sl = [int(x) for x in s]
    res = 0
    c = 0
    for i in sl:
        if c > acc:
            res = res + (c-acc)
            acc = c
        acc = acc + i
        c = c + 1
    return res

def test_cases():
    res1 = sol(4,"11111")
    assert res1==0, f"test case #1 failed with res: {res1}"
    print("test case #1 success")

    res2 = sol(1,"09")
    assert res2==1, f"test case #2 failed with res: {res2}"
    print("test case #2 success")

    res3 = sol(5,"110011")
    assert res3==2, f"test case #3 failed with res: {res3}"
    print("test case #3 success")

    res4 = sol(0,"1")
    assert res4==0, f"test case #4 failed with res: {res4}"
    print("test case #4 success")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1, t +1):
        sm, s = input().split(" ")
        res = sol(int(sm), s)
        print(f"Case #{i}: {res}")
