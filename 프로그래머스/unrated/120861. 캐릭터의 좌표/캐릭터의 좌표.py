def solution(keyinput, board):
    answer = [0, 0]
    x_lim = board[0] // 2
    y_lim = board[1] // 2
    
    for i in keyinput:
        if i == 'up' and answer[1]+1 <= y_lim:
            answer[1] += 1
        elif i == 'down' and answer[1]-1 >= -y_lim:
            answer[1] -= 1
        elif i == 'left' and answer[0]-1 >= -x_lim:
            answer[0] -= 1
        elif i == 'right' and answer[0]+1 <= x_lim:
            answer[0] += 1
    return answer