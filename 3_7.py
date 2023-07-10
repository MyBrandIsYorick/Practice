def isVowel(ch):
    st = "аеёиоуэюяАЕЁИОУЭЮЯ"
    return st.find(ch) != -1


s = list(str(input()))
print({l: True if isVowel(l) else False for l in s})
