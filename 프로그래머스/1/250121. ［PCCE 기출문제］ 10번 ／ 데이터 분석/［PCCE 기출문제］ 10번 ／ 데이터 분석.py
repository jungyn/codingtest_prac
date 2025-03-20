def solution(data, ext, val_ext, sort_by):
    answer = []
    col_info={'code':0,
             'date':1,
             'maximum':2,
             'remain':3}
    
    for i in data:
        if i[col_info[ext]] < val_ext:
            answer.append(i)
            answer.sort(key=lambda x : x[col_info[sort_by]])
    return answer