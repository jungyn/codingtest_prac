def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i == cards1[0]:  # cards1이나 cards2 중 먼저 빈 인덱스가 나타나면 오류
            cards1.pop(0)
        elif cards2 and i == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"