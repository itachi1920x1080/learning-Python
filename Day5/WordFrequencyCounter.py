sentence = input("Enter a sentence: ")

#Split the sentence into words
words = sentence.split()
# Initialize an empty dictionary to store word frequency
word_frequency = {}

#Count the Word
for word in words:
    word = word.lower()#conver  to lowercase
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print(word_frequency)

