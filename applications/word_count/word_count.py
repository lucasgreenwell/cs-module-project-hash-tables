def word_count(s):
    # Your code here
    if len(s) < 1:
        return {}
    words = s.split()
    characters_remove = ['"', ':', ';', ',', '.', '-', '+', '=', '/',  '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    for removal in characters_remove:
        for word in words:
            if removal in word:
                word.replace(())
                word = "".join(chars)


    words = [word.lower() for word in words]
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))