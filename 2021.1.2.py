A_S = ["C", "J"]

def cost(cj_cost, jc_cost , xx):
    if xx == "CJ":
        return cj_cost
    elif xx == "JC":
        return jc_cost
    else:
        return 0

#print(cost(1,2, "J?"))

def minimum_cost(cj_cost, jc_cost, p):
    hc = 0
    ac = 0
    s = []
    t_c = 0
    while ac < len(p):
        if (p[ac] in A_S):
            if(hc == ac):
                ac = ac + 1
            else:
                t_c = t_c + cost(cj_cost, jc_cost, f"{p[hc]}{p[ac]}")
                hc = ac
        else:
            #s.append(p[ac])
            ac = ac + 1
    return t_c

cases = int(input())
for i in range(cases):
    cj_cost, jc_cost, pattern = input().split()
    cj_cost = int(cj_cost)
    jc_cost = int(jc_cost)
    #print(cj_cost, jc_cost, pattern)
    t_c = minimum_cost(cj_cost, jc_cost, pattern)
    print(f"Case #{i+1}: {t_c}")
