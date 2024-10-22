#string word and returns a dictionary where the keys are the letters in the word, and the values are the number of times each letter appears.



def letter_histogram(word):
    out = {}
    for letter in word:
        if letter in out:
            out[letter]+=1
        else:
            out[letter] = 1
    return out

word = "banana"
print(f"The Result of letter histogram  for a given word is {letter_histogram(word)}")