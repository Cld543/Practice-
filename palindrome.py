def reverseNum(num):
    """A helper function to reverse a number without using string manipulation.

    Args:
        num (number): The number to be reverse.

    Returns:
        The reverse of the input number.
    """
    temp = num                  # Make a copy of the input num
    revNum = 0                  # Variable to store the reverse num
    while temp > 0:             
        revNum *= 10            # Multiply by 10 to keep track of which digit you are working with.
        revNum += temp % 10     # Divide tempp by 10 and add remainder to the reversed num
        temp //= 10             # Integer division by 10 to move to next digit
    return revNum

def isPalindrome(num):
    """Check whether or not a number is a palindrome without using string manipulation.

    Args:
        num (number): The number to be checked.

    Returns:
        boolean: Whether or not the number is a palindrome.
    """
    if num >= 0 and num <= 9:
        return True
    return num == reverseNum(num)

print(isPalindrome(12321))
print(isPalindrome(11))
print(isPalindrome(3))
print(isPalindrome(1413))
print(isPalindrome(-656))



