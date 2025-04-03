def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_counts(text):
    d = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in d:
            d[char_lower] = 0
        d[char_lower] += 1
    return d


def sort_character_counts(char_counts):
    records = []
    for char, count in char_counts.items():
        records.append({"char": char, "count": count})
    records.sort(key=lambda x: x["count"], reverse=True)
    return records
