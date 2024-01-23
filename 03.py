def sort_strings_by_vowels(input_list):
    def count_vowels(s):
        return sum(1 for char in s.lower() if char in "aeiou")

    sorted_list = sorted(input_list, key=lambda x: (count_vowels(x), input_list.index(x)))
    return sorted_list
strings = input().split()

result = sort_strings_by_vowels(strings)
print(result)
