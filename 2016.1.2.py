def sol(s):
    sl = [x for x in s]
    p = []
    ptr_m = 0
    ptr_p = 0
    i = 0
    res = 0
    while len(sl) != 0:
        if i >= len(sl):
            res = res + 1
            break
        elif sl[-1] == '+':
            sl.pop()
        elif sl[i] == '-':
            if ptr_p > 0:
                sl[0:i] = ["-"] * ptr_p
                ptr_p = 0
                i = 0
                res = res + 1
            elif ptr_m >= 0:
                ptr_m = ptr_m + 1
                i = i + 1
        elif sl[i] == '+':
            if ptr_m > 0:
                sl = my_reverse(sl)
                res = res + 1
                ptr_m = 0
                i = 0
            elif ptr_p >= 0:
                ptr_p = ptr_p + 1
                i = i + 1
        print(sl, res)
    return res

def my_reverse(sl):
    sl.reverse()
    def f(i):
        if i == '-':
            return '+'
        else:
            return '-'
    return [f(x)for x in sl]

def test_my_reverse():
    res = my_reverse(['-','+','-','-'])
    assert res==['+','+','-','+'], f"test reverse failed with res: {res}"
    print("test reverse success")

def test_cases():
    res1 = sol("-")
    assert res1 == 1, f"test case #1 failed with res : {res1}"
    print("test case #1 success")
    res2 = sol("-+")
    assert res2 == 1, f"test case #2 failed with res : {res2}"
    print("test case #2 success")
    res3 = sol("+-")
    assert res3 == 2, f"test case #3 failed with res : {res3}"
    print("test case #3 success")
    res4 = sol("+++")
    assert res4 == 0, f"test case #4 failed with res : {res4}"
    print("test case #4 success")
    res5 = sol("--+-")
    assert res5 == 3, f"test case #5 failed with res : {res5}"
    print("test case #5 success")

if __name__ == "__main__":
   #test_cases()
   #test_my_reverse()
   t = int(input())
   for i in range(1, t+1):
      s = input()
      res = sol(s)
      print(f"Case #{i}: {res}")
