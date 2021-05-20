def sol(n, p):
    res = ""
    for x in p:
        if x == "E":
            res = res + "S"
        else:
            res = res + "E"
    return res

def test_cases():
    res1 = sol(2, "SE")
    assert res1 == "ES", f"test case #1 failed with res: {res1}"
    print("test case #1 success")
    res2 = sol(5, "EESSSESE")
    assert res2 == "SSEEESES", f"test case #2 failed with res: {res2}"
    print("test case #2 success")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        p = input()
        res = sol(n, p)
        print(f"Case #{i}: {res}")
