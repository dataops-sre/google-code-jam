def sol(n):
    n_o = n
    d = 10
    c = 1
    a = 0
    while n != 0:
        r = n % d
        n = n // d
        if r == 4:
            a = a + (r-1) * c
        else:
            a =  a + r * c
        c = c * d

    return (a, (n_o-a))

def test_cases():
    res1 = sol(4)
    assert res1 == (3, 1), f"test case #1 failed with res : {res1}"
    print("test case #1 success")
    res2 = sol(940)
    assert res2 == (930, 10), f"test case #2 failed with res : {res2}"
    print("test case #2 success")
    res3 = sol(4444)
    assert res3 == (3333, 1111), f"test case #3 failed with res : {res3}"
    print("test case #3 success")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        res = sol(n)
        print(f"Case #{i}: {' '.join([str(x) for x in res])}")
