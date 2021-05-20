import numpy as np

def sol(m):
    l,w = m.shape
    k,r,c = 0, 0, 0
    for x in range(l):
        k = k + m[x][x]
        if len(set(m[x])) != l:
            r = r + 1
        if len(set(m[:,x])) != l:
            c = c + 1
    return (k, r, c)

def test_cases():
    input1 = np.array([[1,2,3,4], [2,1,4,3], [3,4,1,2], [4,3,2,1]])
    res1 = sol(input1)
    assert res1 == (4,0,0), "test case 1 is wrong"
    print("test case 1 is success")

if __name__ == "__main__":
    #test_cases()
    t = int(input())
    for i in range(1, t+1):
        d = int(input())
        inp = []
        for j in range(d):
            l = [int(x) for x in input().split(" ")]
            inp.append(l)
        res = sol(np.array(inp))
        print(f"Case #{i}: {' '.join([str(e) for e in res])}")
