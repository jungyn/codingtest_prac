def solution(str1, str2):
    answer = 0
    str1_set = []
    str2_set = []
    
    for i in range(len(str1)):
        if len(str1[i:i+2]) == 2 and str1[i:i+2].isalpha():     
            str1_set.append(str1[i:i+2].upper())
    for i in range(len(str2)):
        if len(str2[i:i+2]) == 2 and str2[i:i+2].isalpha():     
            str2_set.append(str2[i:i+2].upper())
    
    # 다중 합집합 & 다중 교집합
    from collections import Counter
    
    s1 = Counter(str1_set)
    s2 = Counter(str2_set)
    
    inter = s1 & s2
    union = s1 | s2
    try:
        answer = int(sum(inter.values()) / sum(union.values()) * 65536)
    except:
        answer = 65536
    
    return answer