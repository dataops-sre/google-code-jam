import math

def sol(d, p):
    m = max(p)
    total = m
    for i in range(1,m):
        tmp = 0
        for j in p:
            tmp = tmp + math.ceil(j/i) - 1 
        tmp = tmp + i
        if total > tmp:
            total = tmp
    return total


def test_cases():
    res1 = sol(1, [1])
    assert res1 == 1, f"test case #1 failed with res : {res1}"
    print("test case #1 success")

    res2 = sol(4, [1,2,1,2])
    assert res2 == 2, f"test case #1 failed with res : {res2}"
    print("test case #2 success")

    res3 = sol(1, [9])
    assert res3 == 5, f"test case #3 failed with res : {res3}"
    print("test case #3 success")

    res4 = sol(3, [8,4,1])
    assert res4 == 5, f"test case #4 failed with res : {res4}"
    print("test case #4 success")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1, t+1):
        d = int(input())
        p = [int(x) for x in input().split()]
        res = sol(d,p)
        print(f"Case #{i}: {res}")

