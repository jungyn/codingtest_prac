li = [int(input()) for i in range(5)]

li.sort()
print(sum(li) // len(li)) # 평균값
print(li[len(li) - (len(li) // 2) - 1]) # 중앙값