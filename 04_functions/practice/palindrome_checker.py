def is_palindrome(num):
    reversed_num = 0
    if num < 0: num = num*(-1)
    temp = num
    i = 0
    while temp > 0:
        i +=1
        reversed_num = (reversed_num * 10) + temp % 10
        temp = temp // 10
        
    print(f"It took {i} interations")
    return num == reversed_num


num = int(input("Enter a numtemper: "))

print(f"{num} is palindrome: {is_palindrome(num)}")

