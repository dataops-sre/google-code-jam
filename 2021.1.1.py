def inplace_reverse(l, i, j):
	while i < j:
		tmp = l[i]
		l[i] = l[j]
		l[j] = tmp
		i = i + 1
		j = j - 1 	


def reverse_sort(n, l):
	nb_op = 0
	for i in range(n-1):
		sub_l = l[i:n]
		j = l.index(min(sub_l))
		inplace_reverse(l, i, j)
		nb_op = nb_op + (j-i + 1)
	return nb_op

cases = int(input())
for i in range(cases):
    nb_elem = int(input())
    l = [int(j) for j in input().split()]
    nb_op = reverse_sort(nb_elem, l)
    print(f"Case #{i+1}: {nb_op}")


