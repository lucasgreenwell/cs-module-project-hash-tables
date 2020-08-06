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
# print(count_of_words['the'])

#set up final array for histogram print
#loop through wordcounts hash
    #loop through the histogram array until you find the right spot for this item
        #stick it in that spot with however many hashes it needs
#print histogram

hist_list = []
for word in count_of_words:
    hashes = '#' * count_of_words[word]
    if len(hist_list) < 1:
        hist_list.insert(0, (word, hashes))
    else:
        for index in range(len(hist_list)):
            current_word, current_hashes = hist_list[index]
            if (word, hashes) in hist_list:
                continue
            if index == len(hist_list) - 1:
                hist_list.insert(index, (word, hashes))
            #if the count you're sorting is bigger than the index you're at, go ahead and move everything down
            if count_of_words[current_word] < count_of_words[word]:
                hist_list.insert(index, (word, hashes))
            elif count_of_words[current_word] > count_of_words[word]:
                continue
            elif count_of_words[current_word] == count_of_words[word]:
                if current_word > word:
                    hist_list.insert(index, (word, hashes))
                else:
                    continue

for word, hashes in hist_list:
    print(word, ':', hashes)