def comparison_algorithm(word1, word2):
    str1_words = word1.split('')
    str2_words = word2.split('')
    res = 1/len([str1_words.index(i) for i in str2_words])