def count_vowels(s: str) -> set:
    return set(i for i in s.lower() if i in "aeiou")


s = "Lorem ipsum"

print(count_vowels(s))
