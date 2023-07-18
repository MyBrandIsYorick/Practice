def Is_Palindrome(st):
    rev_st = st[::-1]
    return st == rev_st


s = str(input("Введите строку "))
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        if Is_Palindrome(s[i:j]):
            print(s[i:j])
