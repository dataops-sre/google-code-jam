def sol(x, l):
	res = []
	th = 360 * pow(10,10)
	tm = th / 60
	ts = tm / 60
	y = x
	tl = [th, tm, ts]
	res2 = []
	res2.append(y)
	q = [1, 60*12, 12]
	for i in tl:
		tmp = int(y / i)
		y = y % i
		res2.append(int(y * q.pop()))
		res.append(tmp)	
	res.append(int(y))
	if sorted(res2[:-1]) == l:
		return res
	else:
		return []

def solution(l):
	l = sorted(l)
	res = []
	for x in l:
		res = sol(x,l)
		if len(res) > 0:
			break
	return res

cases = int(input())
for i in range(cases):
    l = [int(j) for j in input().split()]
    res = solution(l)
    print(f"Case #{i+1}: {' '.join([str(x) for x in res])}")


