N = int(input()) # 시험장 개수
A = list(map(int, input().split())) # 각 시험장에 있는 응시자의 수
B, C = map(int, input().split()) # 총감독관, 부감독관

answer = 0
for i in range(N):
    A[i] -= B
    answer += 1
    if A[i] > 0:
        if A[i] % C == 0:
            answer += A[i] // C
        else:
            answer += A[i] // C + 1
print(answer)