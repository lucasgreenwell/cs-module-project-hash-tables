def word_count(s):
    # Your code here
    if len(s) < 1:
        return {}

    characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for character in characters_to_ignore:
        s = s.replace(character, "")

    words = s.split()
    words = [word.lower() for word in words]
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

string_file = open('robin.txt', 'r').read()

count_of_words = word_count(string_file)
print(count_of_words['the'])

