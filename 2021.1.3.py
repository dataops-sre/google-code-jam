def inplace_reverse(l, i, j):
	while i < j:
		tmp = l[i]
		l[i] = l[j]
		l[j] = tmp
		i = i + 1
		j = j - 1 	


def get_min_max_op(n):
	max_op = (n*(n+1)/2) - 1
	min_op = n -1
	return (min_op, max_op) 

def get_rev_op_list(_sum, op_list, minimum_additions):
	res = []
	nb_additions_last = minimum_additions
	while len(res) < minimum_additions :
		tmp = _sum - (nb_additions_last - 1)
		top_queue = op_list[-1]
		if tmp >= top_queue:
			res.append(top_queue)
			_sum =  _sum - top_queue
			nb_additions_last = nb_additions_last - 1
			if len(op_list) != 1:
				op_list.pop()	
		else:
			op_list.pop()
	#print(res)
	return res

#print(get_rev_op_list(5,list(range(1, (4 +1))), 3))

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

def generate_fit_list_from_op_list(op_list):
	sorted_list = list(range(1, len(op_list) + 2))
	#for i in range(len(sorted_list) - 1)
	#	inplace_reverse(l, i, (op_list.pop()-1))

	res = sorted_list
	#op_list.reverse()
	print("op_list: ", op_list)
	#print("res: ", res)
	i = len(sorted_list) - 2
	while i >= 0 and len(op_list) > 0:
		jx = op_list.pop()
		#print(f"log=======i:{i}, jx: {jx}, inplace_reverse_j: {(i+(jx-1))}")
		inplace_reverse(res, i, (i+(jx-1)))	
		#print("log====", res)
		i = i - 1
	#for x in op_list:
	#print("res: ", res)
	return sorted_list
"""
for each list to do the reverse sort 
minimum get n - 1 times one operation
so we need to find combinaision of numbers sums
take n-1 numbers to get to the sum
maxi number can get is n-1, minimum is 1
in decreasing order
"""

def reverse_eng_sort(n, sum_op):
	min_op, max_op = get_min_max_op(n)
	if (sum_op < min_op) or (sum_op > max_op):
		return "IMPOSSIBLE" 

	minimum_additions = n - 1
	op_list = list(range(1, (n +1)))
	reverse_eng_op_list = get_rev_op_list(sum_op, op_list, minimum_additions)
	
	res = generate_fit_list_from_op_list(reverse_eng_op_list)
	fit_list = res
	return " ".join(map(str, fit_list)) 

cases = int(input())
for i in range(cases):
    nb_elem, nb_op = [int(j) for j in input().split()]
    print(nb_elem, nb_op)
    fit_list = reverse_eng_sort(nb_elem, nb_op)
    print(f"Case #{i+1}: {fit_list}")


