def count_vowels_and_consonants(input_string):
    vowels = sum(1 for char in input_string.lower() if char in "aeiou")
    consonants = sum(1 for char in input_string.lower() if char.isalpha() and char not in "aeiou")
    return vowels, consonants
