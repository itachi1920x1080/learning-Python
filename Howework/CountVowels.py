def Count(text):
    Voweels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in Voweels:
            count += 1
    return count

input_text = input("Enter a string: ")
vowel_count = Count(input_text)
print("input string:", input_text)
print("Number of vowels in the given string:", vowel_count)