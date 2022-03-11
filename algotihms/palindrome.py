def isPalindrome(number):

    # по условию задачи: -121 from right to left reads as 121-.
    if number < 0:
        return False

    revNumber = 0
    x = number

    while x > 0:
        remainder = x % 10
        revNumber = revNumber * 10 + remainder
        # оператор '//' оставляет целую часть от деления, а дробную отбрасывает
        # фактически '//' заменяет выражение x = (x - remainder) / 10
        x = x // 10

    return revNumber == number


number = 14241
print(isPalindrome(number))