def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    return [e for e in candidates if sorted(e.lower()) == word_sorted and e.lower() != word_lower]
