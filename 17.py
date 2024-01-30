def count_words(s: str) -> dict[str, int]:
    return {word: s.split().count(word) for word in set(s.split())}


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eleifend. Lorem"

print(count_words(text))
