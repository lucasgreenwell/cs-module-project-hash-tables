def no_dups(s):
    words = s
    res = s
    if ' ' in s:
        print('anything')
        words = s.split()
        words_seen = {}
        res = ''
        for word in words:
            if word in words_seen:
                continue
            words_seen[word] = word
            res = res + ' ' + word
        if len(words_seen) < 2:
            res = res.strip(' ')
        res = res.lstrip(' ')
    return res



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))