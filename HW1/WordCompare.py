def word_compare(string1, string2 = "steal"):
    if isinstance(string1, str) and isinstance(string2, str):
        if sorted(string1) == sorted(string2):
            return "Anagram"
        else:
            return (string1, string2)
    else:
        return "Those aren't strings!"
