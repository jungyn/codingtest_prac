def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(num):
        numbers = numbers.replace(num, str(i))
    return int(numbers)