T = int(input())
days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for test_case in range(1, T + 1):
    N = str(input())
    year = N[:4]
    month =  N[4:6]
    day = N[6:]
    fail = -1
    
    if 0 < int(month) <= 12 and int(day) <= days[int(month)]:
	    print("#{} {}/{}/{}".format(test_case, year, month, day))
    else:
        print("#{} {}".format(test_case, fail))