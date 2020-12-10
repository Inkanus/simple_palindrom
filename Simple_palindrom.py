def is_palindrome(str):
    str = ''.join([c for c in str.lower() if c.isalpha()])
    return str == str[::-1]

print(is_palindrome("kobyła, MałY Bok"))