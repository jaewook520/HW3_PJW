def reverse_words(words):
    words_list = words.split()
    words_list.reverse()
    new_words=""
    for i in words_list:
        new_words = new_words + i + " "
    new_words.rstrip()
    return new_words

if __name__ == "__main__":
    words = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    words2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print("input strings #1 : {0:s}\n".format(words))
    print("output strings #1: {0:s}\n".format(reverse_words(words)))
    print("input strings #2 : {0:s}\n".format(words2))
    print("output strings #2: {0:s}\n".format(reverse_words(words2)))
