def sol(n):
    if n == 0:
        return 'INSOMNIA'
    solved = False
    i = 1
    res = set() 
    while (not solved):
        next_n = n * i
        tmp_s = set([int(x) for x in str(next_n)])
        res = res.union(tmp_s)
        if len(res) == 10:
            solved = True
        i = i + 1
    return next_n

def test_cases():
    r1 = sol(0)
    assert r1 == 'INSOMNIA', "WRONG test case 1"
    print("test case 1 sucess")
    r2 = sol(1)
    assert r2 == 10, "WRONG test case 2"
    print("test case 2 sucess")
    r3 = sol(2)
    assert r3 == 90, "WRONG test case 3"
    print("test case 3 sucess")
    r4 = sol(11)
    assert r4 == 110, "WRONG test case 4"
    print("test case 4 sucess")
    r5 = sol(1692)
    assert r5 == 5076, "WRONG test case 5"
    print("test case 5 sucess")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1,t+1):
        n = int(input())
        res = sol(n)
        print(f"Case #{i}: {res}")
