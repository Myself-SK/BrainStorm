s = "babad"

def check_palindrome(s:str)->bool:
    if s[::-1] == s:
        return True
    else:
        return False

def longest_palindrome_substring(s:str)->str:
    longest_palindrome = s[0]
    for i in range(len(s)):
        for j in range(len(s)):
            if check_palindrome(s[j:j+i]) and len(longest_palindrome)<len(s[j:j+i]):
                longest_palindrome=s[j:j+i]
    return longest_palindrome

longest_palindrome_str = longest_palindrome_substring(s)
print(longest_palindrome_str)