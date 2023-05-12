from WordCompare import *

def find_anagrams(list):
    x = ""
    for i in list:
        newList = []
        for j in list:
            if i != j:
                if word_compare(i,j) == "Anagram":
                    newList.append(j)
        if i != list[-1]:
            x += f'{i}: {newList}\n'
        else:
            x += f'{i}: {newList}'
    return x
