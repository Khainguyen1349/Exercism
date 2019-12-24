def find_anagrams(word, candidates):
    word_sorted = sorted(word.lower())
    return [e for e in candidates if sorted(e.lower()) == word_sorted and e.lower() != word.lower()]
