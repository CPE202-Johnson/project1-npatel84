def perm_gen_lex(a): 

    if a is 0:
        return []
    
    if len(a) == 1:
        return [a]
    
    a_list = perm_gen_lex(a[1:])
    char = a[0]
    result = []

    for perm in a_list:
        for i in range(len(perm) +1):
            result.append(perm[:i] + char + perm[i:])

    return sorted(result)




 