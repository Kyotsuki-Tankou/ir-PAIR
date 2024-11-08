def compare_output(ans_str,res_str):
    ans=[]
    res=[]
    if ans_str.lower()!='null':
        try:
            ans=eval(ans_str)
        except:
            return "ERROR"
    if res_str.lower()!='null':
        try:
            res=eval(res_str)
        except:
            return "ERROR"
    ans_set=set(ans)
    res_set=set(res)
    intersection = ans_set.intersection(res_set)
    union = ans_set.union(res_set)
    if not union:
        jaccard_similarity=1.0
    else:
        jaccard_similarity=len(intersection)/len(union)
    return jaccard_similarity

    
ans="['A','B','A']"
res="['A','B','C']"
print(compare_output(ans, res))